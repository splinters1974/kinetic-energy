#!/usr/bin/env python3
"""
Fetch all Squarespace-hosted assets and update HTML files to use local copies.

Run from the repo root:
    python3 scripts/fetch-squarespace-assets.py

Requires: Python 3.7+, curl or urllib (stdlib)
"""

import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ASSETS_CSS = REPO_ROOT / "assets" / "css"
ASSETS_JS  = REPO_ROOT / "assets" / "js"
ASSETS_IMG = REPO_ROOT / "assets" / "images"

for d in [ASSETS_CSS, ASSETS_JS, ASSETS_IMG]:
    d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Static assets to download
# ---------------------------------------------------------------------------

# Pull exact URLs from index.html at runtime so the script stays in sync
def extract_urls_from_html(pattern, files):
    found = set()
    for f in files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        found.update(re.findall(pattern, text))
    return found

html_files = list(REPO_ROOT.glob("*.html")) + list((REPO_ROOT / "insight").glob("*.html"))

# CSS files
css_urls = extract_urls_from_html(
    r'href="(https://(?:static1|assets)\.squarespace\.com/[^"]+\.css[^"]*)"',
    html_files
)

# JS files (site bundle + assets.squarespace scripts we want to keep)
site_bundle_urls = extract_urls_from_html(
    r'src="(https://static1\.squarespace\.com/[^"]+site-bundle[^"]*\.js[^"]*)"',
    html_files
)

# Favicons
favicon_urls = extract_urls_from_html(
    r'href="(https://images\.squarespace-cdn\.com/[^"]+favicon\.ico[^"]*)"',
    html_files
)

# Images — base URLs (no ?format=... suffix)
all_img_urls = set()
for f in html_files:
    text = f.read_text(encoding="utf-8", errors="ignore")
    # Match full squarespace image URLs including optional ?format= suffix
    for m in re.finditer(
        r'https://images\.squarespace-cdn\.com/content/v1/[^\s"\'&<>]+',
        text
    ):
        url = m.group(0).rstrip('",\'')
        # Strip ?format=... to get base URL
        base = re.sub(r'\?.*$', '', url)
        if re.search(r'\.(jpg|jpeg|png|gif|webp|svg|ico)$', base, re.I):
            all_img_urls.add(base)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def download(url, dest_path, retries=3):
    """Download url to dest_path. Returns True on success."""
    if dest_path.exists() and dest_path.stat().st_size > 0:
        print(f"  [skip] {dest_path.name} (already exists)")
        return True
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; site-migration/1.0)"
    }
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            dest_path.write_bytes(data)
            print(f"  [ok]   {dest_path.name} ({len(data):,} bytes)")
            return True
        except urllib.error.HTTPError as e:
            print(f"  [err]  {url} → HTTP {e.code}", file=sys.stderr)
            return False
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"  [err]  {url} → {e}", file=sys.stderr)
                return False
    return False


def url_to_local_path(url):
    """
    Map a Squarespace image/favicon URL to a local assets path.
    Uses the unique hash segment (second-to-last path component) as filename.
    """
    base_url = re.sub(r'\?.*$', '', url)
    parts = base_url.rstrip('/').split('/')
    filename = parts[-1]           # e.g. unsplash-image-rRWiVQzLm7k.jpg
    hash_seg = parts[-2] if len(parts) >= 2 else ''

    ext = Path(filename).suffix.lower() or '.jpg'
    # Clean filename for filesystem
    clean_name = re.sub(r'[^a-zA-Z0-9._-]', '-', filename)

    # Prefix with hash segment to guarantee uniqueness when filenames repeat
    local_name = f"{hash_seg}--{clean_name}" if hash_seg else clean_name
    # Decide subdirectory
    if 'favicon' in filename.lower():
        return ASSETS_IMG / local_name
    else:
        return ASSETS_IMG / local_name


# ---------------------------------------------------------------------------
# Build replacement map: squarespace_base_url → local_web_path
# ---------------------------------------------------------------------------
url_map = {}  # base_url (no ?format) → /assets/... web path

# CSS
print("\n=== Downloading CSS ===")
for url in sorted(css_urls):
    filename = url.split('/')[-1].split('?')[0] or 'squarespace.css'
    # Distinguish site.css vs static.css by filename
    if 'site.css' in url:
        dest = ASSETS_CSS / 'site.css'
    elif 'static.css' in url:
        dest = ASSETS_CSS / 'static.css'
    else:
        dest = ASSETS_CSS / filename
    if download(url, dest):
        url_map[url] = f"/assets/css/{dest.name}"

# Also handle user-account-core CSS
user_css_urls = extract_urls_from_html(
    r'href="(https://assets\.squarespace\.com/[^"]+user-account-core[^"]+\.css[^"]*)"',
    html_files
)
for url in sorted(user_css_urls):
    dest = ASSETS_CSS / 'user-account-core.css'
    if download(url, dest):
        url_map[url] = "/assets/css/user-account-core.css"

# Site bundle JS
print("\n=== Downloading JS ===")
for url in sorted(site_bundle_urls):
    dest = ASSETS_JS / 'site-bundle.js'
    if download(url, dest):
        url_map[url] = "/assets/js/site-bundle.js"

# Favicons
print("\n=== Downloading favicons ===")
favicon_list = sorted(favicon_urls)
favicon_names = ['favicon-light.ico', 'favicon-dark.ico']
for i, url in enumerate(favicon_list[:2]):
    name = favicon_names[i] if i < len(favicon_names) else f'favicon-{i}.ico'
    dest = ASSETS_IMG / name
    base = re.sub(r'\?.*$', '', url)
    if download(url, dest):
        url_map[base] = f"/assets/images/{name}"

# Images
print(f"\n=== Downloading {len(all_img_urls)} images ===")
for url in sorted(all_img_urls):
    if 'favicon' in url.lower():
        continue  # handled above
    dest = url_to_local_path(url)
    # Download at 1500w for good quality
    download_url = url + "?format=1500w"
    if download(download_url, dest):
        url_map[url] = f"/assets/images/{dest.name}"

# ---------------------------------------------------------------------------
# Update HTML files
# ---------------------------------------------------------------------------
print("\n=== Updating HTML files ===")

def replace_in_html(text, url_map):
    # Sort by length descending so longer URLs are replaced first
    for sq_url, local_path in sorted(url_map.items(), key=lambda x: -len(x[0])):
        # Replace bare base URL (no query string)
        text = text.replace(sq_url, local_path)
        # Replace URL with any ?format=... suffix
        text = re.sub(
            re.escape(sq_url) + r'\?[^\s"\'&<>]*',
            local_path,
            text
        )
    return text

updated = 0
for f in html_files:
    original = f.read_text(encoding="utf-8", errors="ignore")
    updated_text = replace_in_html(original, url_map)
    if updated_text != original:
        f.write_text(updated_text, encoding="utf-8")
        updated += 1
        print(f"  [ok]   {f.relative_to(REPO_ROOT)}")

print(f"\nDone. Updated {updated} HTML files.")
print("\nNext steps:")
print("  1. Review the changes in your browser to confirm the site looks correct")
print("  2. git add -A && git commit -m 'Self-host all Squarespace assets'")
print("  3. git push")

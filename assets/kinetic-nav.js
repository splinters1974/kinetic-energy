/* =============================================
   Kinetic Strategy Consulting – Navigation JS
   Fallback for Squarespace burger & folder menus
   ============================================= */
(function () {
  'use strict';

  function init() {

    /* ── Burger / mobile overlay ─────────────── */
    var burger = document.querySelector('[data-test="header-burger"]');
    var overlay = document.querySelector('.header-menu-overlay');

    if (burger && overlay) {
      burger.addEventListener('click', function () {
        var isOpen = overlay.classList.contains('header-menu-overlay--open');
        if (isOpen) {
          overlay.classList.remove('header-menu-overlay--open');
          burger.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        } else {
          overlay.classList.add('header-menu-overlay--open');
          burger.setAttribute('aria-expanded', 'true');
          document.body.style.overflow = 'hidden';
        }
      });
    }

    /* ── Desktop: folder dropdown on hover/focus ─ */
    var folderItems = document.querySelectorAll('.header-nav-item--folder');
    folderItems.forEach(function (item) {
      var btn = item.querySelector('.header-nav-folder-title');
      var content = item.querySelector('.header-nav-folder-content');
      if (!btn || !content) return;

      // Desktop hover
      item.addEventListener('mouseenter', function () {
        btn.setAttribute('aria-expanded', 'true');
      });
      item.addEventListener('mouseleave', function () {
        btn.setAttribute('aria-expanded', 'false');
      });

      // Keyboard / click (mobile overlay)
      btn.addEventListener('click', function (e) {
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      });
    });

    /* ── Mobile overlay back buttons ────────────── */
    var backBtns = document.querySelectorAll('[data-test="header-back-btn"], .header-nav-folder-back');
    backBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var parentFolder = btn.closest('.header-nav-folder-content');
        if (parentFolder) {
          var folderTitle = parentFolder.previousElementSibling;
          if (folderTitle) folderTitle.setAttribute('aria-expanded', 'false');
        }
      });
    });

  }

  /* ── Squarespace native video backgrounds ─── */
  function initVideoBackgrounds() {
    var containers = document.querySelectorAll('.sqs-video-background-native');
    containers.forEach(function (container) {
      var configStr = container.getAttribute('data-config-native-video');
      if (!configStr) return;
      try {
        var config = JSON.parse(configStr);
        var url = config.alexandriaUrl;
        var variants = config.systemDataVariants ? config.systemDataVariants.split(',') : [];
        if (!url || variants.length === 0) return;
        var videoUrl = url.replace('{variant}', variants[0]);
        var player = container.querySelector('.sqs-video-background-native__video-player');
        if (!player) return;
        var video = document.createElement('video');
        video.src = videoUrl;
        video.autoplay = true;
        video.muted = true;
        video.loop = true;
        video.playsInline = true;
        video.setAttribute('playsinline', '');
        video.style.cssText = 'position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;';
        var speed = parseFloat(container.getAttribute('data-config-playback-speed') || '1');
        video.addEventListener('loadedmetadata', function () { video.playbackRate = speed; });
        player.appendChild(video);
        video.play().catch(function () {});
      } catch (e) {}
    });
  }

  /* ── Squarespace lazy-loaded images ─────────── */
  function initLazyImages() {
    var imgs = document.querySelectorAll('img[data-load="false"]');
    imgs.forEach(function (img) {
      img.setAttribute('data-load', 'true');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { init(); initVideoBackgrounds(); initLazyImages(); });
  } else {
    init();
    initVideoBackgrounds();
    initLazyImages();
  }

})();

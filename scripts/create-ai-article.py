#!/usr/bin/env python3
"""
Create new insight article and update listing page.
Run from repo root:  python3 scripts/create-ai-article.py
"""
import re, json, html as html_module
from pathlib import Path

REPO = Path(__file__).parent.parent

# ── Article text ─────────────────────────────────────────────────────────────
ARTICLE_RAW = json.loads('"The Salesperson, the Algorithm, and the Energy Bill. How AI Is Reshaping B2B Energy Sales\\n\\nA quick word before we start - and I will be upfront about this because I think it matters.\\nAfter 30 years in sales leadership and the best part of two decades working in and around the energy sector, I have watched this industry go through more reinventions than I care to count. Deregulation. Smart metering. The renewables revolution. The net zero pivot. Each one changed how we sell, who we sell to, and what we are actually selling. This latest shift - AI - has the potential to be the most disruptive of the lot. Not because it is the most technically complex, but because it moves faster than anything that has come before it.\\nNow, given that this article is about AI, it would have been frankly a bit daft not to use it in writing it. I did. Mostly for fact-checking - there are statistics and market figures in here that needed verifying against current sources, not just my memory of a conference I attended two years ago. A little grammar tidying too, because my written English occasionally wanders off without permission. But the substance of this article - the perspective, the commercial context, the view from the ground - that is mine. Thirty years of selling, managing sales teams, and watching energy businesses succeed and fail has a way of forming opinions. What follows is an honest attempt to share them.\\nOne final note before we get into it: although this article is rooted in the energy sector, the themes here apply across every industry where human beings sell things to other human beings. If you are reading this from financial services, manufacturing, professional services, or anywhere else - the disruption is coming for you too. Energy just happens to be where I sit, and where the examples are sharpest.\\nHow We Sold Before - The Craft and the Grind\\nThere is a version of this article that begins with \\"AI is coming for your job.\\" You have probably read three of them already this week. This is not that article.\\nI started my career in sales before email. Let that sink in for a moment. The CRM system came on a CD-ROM. Signed orders arrived by fax. The working week had a rhythm that feels almost quaint by today\'s standards - Monday morning was spent on the phone building your diary for the week ahead, because without face-to-face contact you were not really selling. You shook hands. You built trust over a coffee in someone\'s office. You earned the right to come back.\\nI am not raising any of that to sound nostalgic or archaic. I raise it because it illustrates something important: sales has evolved enormously over the past three decades, and the people who thrived were the ones who moved with it. Email did not kill sales - it changed how we opened doors. CRM systems did not dehumanise relationships - they helped us manage more of them. Video calling did not replace the site visit - it added another touchpoint. Each wave of technology felt disruptive at the time and became standard practice within a few years.\\nWhat is different about AI is not that it changes the tools - it is that it compresses the timeline. Changes that once took a decade to embed will happen in two or three years. That is the bit that should focus the mind.\\nIf you have been in B2B energy sales for more than five years, you will remember - or still be living - a very particular rhythm. Prospecting from directories or bought-in data lists. Cold calls in the morning, site visits mid-week, proposals that took days to build from scratch. Account management driven largely by relationship, intuition, and the occasional reminder alarm in your CRM that said \\"follow up - urgent\\" in angry red text.\\nIn complex energy solutions - solar, CHP, battery storage, LED lighting, BMS retrofits - the sales cycle was long, technical, and relationship-heavy. The good salespeople were not just closers; they were quasi-consultants who could walk a site, read a half-hourly data download, and come back two days later with a credible business case. That combination of technical credibility and human trust was the competitive differentiator. In many cases, it still is. And I\\u2019ve got to work with some of the best.\\nThe supply side was not dramatically different. Brokers and direct suppliers competed on margin, relationships, and timing - catching a client at contract renewal with a better rate and a warm conversation. The sharpest people used data well, but it was mostly manual. Pull the client\'s ECOES data, cross-reference with market prices, build a matrix, try and differentiate by selling a different kind of supply structure, send a quote. Repeat. It worked. It was not, however, especially efficient.\\nMy Relationship With AI - and Why I Think It Matters for All of Us\\nMy interest in AI began in earnest around 2022, which in AI terms is practically the Stone Age. Since then I have made it a deliberate part of my own professional development - researching tools, testing them in practice, and where businesses I have worked in have been willing, implementing them into sales and marketing workflows.\\nI say \\"where businesses have been willing\\" with purpose. Resistance to AI is everywhere. It comes in different forms - scepticism from leadership about ROI, IT teams not allowing integration, wariness from sales teams who fear what it means for their roles, and a general institutional inertia that treats new technology as a project to be managed rather than an opportunity to be seized. I understand all of that. I have sat in those conversations.\\nBut I have also seen what happens when you do embrace it properly. Prospecting that used to take hours compressed into minutes. Proposals that once required a full day of modelling generated in a fraction of the time. Sales coaching insights that no manager could have produced manually, surfaced automatically from call recordings.\\nMy belief is straightforward: AI can meaningfully elevate our profession. It can make good salespeople excellent and give excellent salespeople room to operate at a level that simply was not possible before. But it can also systematically damage the profession if used carelessly - stripping out the human elements that make complex B2B sales work, producing a race to the bottom in outreach quality, and eroding the judgement and expertise that clients actually pay for. With great power, as the saying goes, comes great responsibility. That is not a cliche in this context - it is a commercial reality.\\nA Note on Marketing - Because Sales Cannot Afford to Ignore It\\nThroughout my career I have operated at the intersection of sales and marketing - as Sales and Marketing Director in several roles, and with a consistent view that treating the two as separate functions is one of the most expensive mistakes a business can make. AI has transformed marketing perhaps faster than any other commercial discipline. Content generation, campaign personalisation, SEO, lead nurturing, social selling - the tools available now would have seemed extraordinary five years ago.\\nThe relevance for sales professionals is direct: the boundary between marketing and selling is blurring further. The modern energy salesperson needs to understand how they are being found, how their company is positioning itself digitally, and how AI-driven marketing can warm up conversations before the first call is ever made. Sales and marketing as one cohesive department is not a radical idea - it is increasingly the only structure that makes sense.\\nThe Last Two Years - What Has Actually Changed\\nThe pace of AI adoption in sales has been genuinely striking. According to Salesforce and Sopro research, 81% of sales teams are already experimenting with or have fully deployed AI tools - a reflection that AI integration has effectively reached table-stakes status in modern B2B selling. Whether UK energy businesses are at the leading edge of that curve is debatable, but the tools are here, they are accessible, and some of your competitors are already using them.\\nIn practical terms, what has changed for energy sales professionals?\\nThe most immediate shift is in prospecting and pre-call intelligence. AI-powered platforms can now cross-reference company profiles, energy consumption signals, planning applications, sustainability commitments, and even hiring patterns to identify which businesses are most likely to be in-market for solar, EV charging infrastructure, or an energy efficiency review. A field sales rep who once spent two hours building a prospect list for a day\'s calls can now have that work done before they have finished their coffee. LinkedIn found that sellers using AI for research save around 1.5 hours per week, while HubSpot reports 64% of reps save one to five hours weekly through automation - time that, if used well, goes back into actual selling.\\nProposal generation and financial modelling are also being transformed. In the solutions space - where a solar or CHP proposal once meant hours of manual calculation, site data entry, and layout design - AI-assisted tools can now produce credible first-draft financial models far faster. This does not eliminate the need for engineering input or commercial judgement, but it accelerates the journey from site visit to boardroom presentation considerably.\\nPerhaps less visible but equally significant is what AI is doing for post-call intelligence. Tools like Gong are now widely used to analyse sales conversations, flag objection patterns, score calls against best-practice criteria, and feed insights back to managers in near real-time. For sales directors trying to coach teams across a large patch, this is genuinely powerful - a level of pipeline visibility and coaching feedback that simply did not exist before.\\nOn the energy systems side, AI is also reshaping what we are actually selling. The UK flexibility market contracted 9GW of capacity in 2024, delivering an estimated \\u00a3300m in consumer savings, with AI-driven platforms increasingly central to how commercial and industrial businesses participate in demand-side response, load shifting, and battery optimisation. The proposition you are taking to a multi-site manufacturer or a cold storage operator today is not just \\"here is a cheaper unit rate.\\" It is \\"here is how your assets can generate revenue from grid services while cutting your bills.\\" That is a fundamentally more complex, and more valuable, conversation - and AI is what makes the modelling and dispatch behind it possible.\\nMcKinsey\'s B2B energy research notes that energy is no longer treated as a back-office commodity but as a core lever for resilience, cost control, and decarbonisation. If your sales approach is still purely cost-led, that is worth reflecting on.\\nThe Risks: Where AI Can Actually Harm Your Sales Effort\\nIt would be dishonest not to acknowledge the downsides, and there are real ones.\\nThe most immediate risk is the commoditisation of outreach. When every SDR on every team is using the same AI tools to generate the same personalised-but-not-really email sequences, the signal-to-noise ratio in a prospect\'s inbox collapses. Energy buyers - procurement managers, finance directors, sustainability leads - are already drowning in outreach. AI-generated drip campaigns that use a prospect\'s company name and LinkedIn headline to simulate personalisation will, over time, become as easy to ignore as any other spam. Research shows that 82% of consumers want more human interaction as technology advances - a reminder that the pendulum can swing too far.\\nThere is also a real risk of capability atrophy. If junior sales professionals learn to rely on AI to do their research, write their emails, and script their objection handling, they may never develop the deep product knowledge and commercial instinct that makes a great energy salesperson in the first place. The tools should accelerate competence, not replace the development of it. A rep who cannot explain why a client\'s half-hourly profile makes them a good candidate for battery storage - without asking ChatGPT - is not someone you want presenting to a CFO.\\nData quality is another unglamorous but critical issue. AI tools rely on clean, connected data. Without it, even sophisticated platforms will produce unreliable results. Many energy businesses still operate with CRM data that is, charitably, patchy - outdated contacts, incomplete consumption records, pipelines that have not been updated since the previous quarter. Feeding poor data into AI systems does not give you intelligence; it gives you confident nonsense, faster.\\nAnd then there is the thornier question of trust. B2B energy deals - particularly in the solutions space - are often signed on the back of a relationship built over months. A business committing to a 20-year solar PPA or a significant energy efficiency programme needs to trust the individual and the business behind it. AI excels at data-driven tasks and pattern recognition, but human judgement remains crucial for authentic relationships, complex negotiations, and strategic decisions. No algorithm has yet worked out how to have a decent pint with a facilities director and talk honestly about what is actually going wrong with their energy costs.\\nWill There Be Fewer Sales Jobs? The Question Nobody Wants to Answer Directly\\nHere is the honest, uncomfortable bit: probably yes - in some areas, eventually. But the picture is more nuanced than the headlines suggest, and it is worth working through it rather than pretending it does not exist.\\nThe roles most immediately at risk are those built almost entirely on volume and repetition - high-frequency outbound calling, manual prospecting, transactional renewal chasing. These tasks are precisely what AI agents are being designed to handle, and they will handle them cheaper and faster than a human being. If your sales team\'s primary activity is doing things a well-configured piece of software could do in its sleep, that is a business model under pressure.\\nBut the energy sector - particularly in solutions, flexibility services, and complex supply - has never been primarily that. The roles that command real value here are advisory: understanding a client\'s energy strategy, navigating procurement committees, structuring a deal that works commercially for both sides. AI does not replicate that. What it can do is remove the administrative burden from the people doing that work - freeing them to do more of it, better.\\nThe more interesting question is not whether headcounts will fall but whether the shape of a sales team changes. Fewer junior reps doing manual groundwork. More senior people operating with AI-powered leverage across a broader account base. New hybrid roles - part commercial, part technical, part data-literate - that do not have a job title yet but are clearly emerging. The World Economic Forum projects that while AI will displace some roles, 78 million new jobs are expected globally despite automation by 2030. Sales will not disappear. It will reorganise.\\nThis is worth a conversation in your own organisation. Not a defensive one, but a strategic one. What are your people\'s most valuable hours spent on? And what is consuming the rest?\\nBuilding Your Own Tools: Why the Best Salespeople Will Start Creating, Not Just Using\\nHere is something that would have sounded like science fiction five years ago: you do not need to be a software developer to build your own sales tools anymore.\\nA movement has emerged - sometimes called \\"vibe coding\\" - that describes the process of building functional software applications by describing what you want in plain English and letting AI write the code for you. You do not need to understand programming languages. You do not need a technical team. You describe the problem, iterate with the AI until it works, and end up with something genuinely useful. It is not always perfect, and complex systems still need proper engineering - but for a motivated sales professional who wants a bespoke prospecting tool, a customised proposal calculator, or an automated reporting dashboard, the barrier to entry is now remarkably low.\\nFor individual salespeople, this is liberating. The good ones - the ones who have always sought an edge - can now build systems tailored precisely to how they work, at relatively low cost and in a matter of days rather than months. A solar sales specialist could build a site screening tool that flags planning applications for commercial rooftops within their territory. A flexibility broker could automate their market intelligence feed. A BDM could create a dashboard that surfaces their highest-priority accounts every morning without them touching a spreadsheet.\\nFor organisations, the implications are equally significant. Bespoke internal tools that once required a software development budget and a six-month project timeline can now be prototyped in days. Competitive advantage through custom technology - previously the preserve of large businesses with large IT departments - is becoming accessible to ambitious SMEs. Energy businesses that embrace this will be able to move, iterate, and innovate at a speed that their slower competitors will struggle to match.\\nThis is not a call for every salesperson to become a developer. It is a call for the best among us to stay curious, stay hands-on, and not assume that the tools we need already exist.\\nWhere This Is Heading: The Energy Sales Professional of 2027\\nThe honest answer is that the sales roles most at risk are the ones that were always thin on value-add. High-volume, low-complexity, outbound-only roles where the rep\'s job was essentially to dial, pitch, and close on price - those will increasingly be handled, or at least initiated, by AI.\\nBut the energy sector, particularly in solutions and services, is not mostly that. The best roles in this sector have always been advisory in nature. And that is where the opportunity lies.\\nBain and Company concluded that AI could effectively double active selling time by eliminating routine tasks - not by replacing salespeople, but by removing the administrative overhead that was eating into their day. For an experienced energy solutions specialist who should be spending their time with clients and prospects rather than building spreadsheet models from scratch, that is an enormous opportunity.\\nThe emerging picture is of a genuinely augmented sales professional. Someone who uses AI to identify the right prospects before picking up the phone, who can walk into a first meeting already understanding a client\'s energy profile, sustainability commitments, and likely pain points. Who uses AI-assisted modelling to turn around a credible solar or CHP proposal in hours rather than days. Who lets AI handle follow-up sequencing and CRM hygiene, so their time goes to the conversations that actually move deals forward.\\nGartner projects that by 2027, 95% of seller research workflows will begin with AI, up from less than 20% in 2024. That is not a distant future. That is two years away. The energy businesses and the individual sales professionals who are building those habits now will have a measurable advantage over those who are not.\\nThere is also a broader commercial point worth making for anyone in a leadership role. The energy transition itself is creating genuinely new sales territories. Data centres, EV fleets, heat pump programmes, industrial electrification - all of this represents new commercial opportunity for businesses that can position themselves as energy partners, not just suppliers. The salesperson who understands battery storage, demand flexibility, and on-site generation - and who can articulate their combined value to a business customer - is not being automated out. They are becoming more valuable.\\nThe Uncomfortable Bit Nobody Wants to Say\\nAI will not eliminate great energy salespeople. But it will make average ones redundant faster than anything that has come before it.\\nThe middle of the pack - the reps who coasted on a decent contacts book and a familiar face - will find that comfort shrinking. The tools available to a motivated competitor are now too powerful to ignore. If you are not using AI to sharpen your prospecting, accelerate your proposals, and free up your time for genuine client engagement, someone else is.\\nThe good news - and it is genuinely good news - is that the energy sector rewards people who know their stuff and can be trusted with a significant commercial decision. Those fundamentals have not changed. But the wrapper around them has. Learn the tools. Use them. Do not let them think for you.\\nThe algorithm is not your replacement. It is your new junior colleague. Treat it accordingly.\\nI have spent the best part of two decades in B2B energy sales, and I have rarely seen a period of change this significant - or this full of genuine opportunity for the people willing to move with it. I would be genuinely interested in what you are seeing on the ground. Are you using AI in your sales process? Is it helping, or is it just noise? Have you started building your own tools? Drop a comment below - I read every one.\\nMartyn Sheridan"')

# ── Make new article HTML ─────────────────────────────────────────────────────
template_path = REPO / "insight" / "overcoming-barriers-to-fully-funded-solar-in-large-businesses.html"
html = template_path.read_text(encoding="utf-8")

new_title   = "The Salesperson, the Algorithm, and the Energy Bill. How AI Is Reshaping B2B Energy Sales"
new_slug    = "the-salesperson-the-algorithm-and-the-energy-bill"
new_date    = "24 Mar"
new_desc    = "After 30 years in sales leadership and the best part of two decades working in and around the energy sector, I have watched this industry go through more reinventions than I care to count. This latest shift - AI - has the potential to be the most disruptive of the lot."
new_img     = "/assets/images/ai-b2b-energy-sales.jpg"
new_img_abs = "https://www.kinetic-energy.co.uk/assets/images/ai-b2b-energy-sales.jpg"

old_title_text = "Sun on the Horizon: Overcoming Barriers to Fully Funded Solar in Large Businesses"
old_title_html = "Sun on the Horizon: Overcoming Barriers to Fully Funded Solar in Large Businesses &mdash; Kinetic Strategy Consulting"
old_slug       = "overcoming-barriers-to-fully-funded-solar-in-large-businesses"
old_date       = "8 Apr"
old_img_base   = "https://static1.squarespace.com/static/6908923037c260059da997b5/69089a0befd47b7e019874cc/6912172ae5f2c232a8865560/1762794190217/unsplash-image-_h0xG4s6NFg.jpg"

html = html.replace(f"<title>{old_title_html}</title>",
                    f"<title>{new_title} &mdash; Kinetic Strategy Consulting</title>")
html = html.replace(f'href="https://www.kinetic-energy.co.uk/insight/{old_slug}"',
                    f'href="https://www.kinetic-energy.co.uk/insight/{new_slug}"')
html = html.replace(f'content="https://www.kinetic-energy.co.uk/insight/{old_slug}"',
                    f'content="https://www.kinetic-energy.co.uk/insight/{new_slug}"')
html = html.replace(f'content="{old_title_html}"', f'content="{new_title} &mdash; Kinetic Strategy Consulting"')
html = html.replace(f'content="{old_title_text}"', f'content="{new_title}"')
html = html.replace(old_img_base + "?format=1500w", new_img_abs)
html = html.replace(old_img_base, new_img_abs)

html = re.sub(r'<meta property="og:description" content="[^"]*"/>',
              f'<meta property="og:description" content="{new_desc}"/>', html)
html = re.sub(r'<meta itemprop="description" content="[^"]*"/>',
              f'<meta itemprop="description" content="{new_desc}"/>', html)
html = re.sub(r'<meta name="twitter:description" content="[^"]*"/>',
              f'<meta name="twitter:description" content="{new_desc}"/>', html)
html = re.sub(r'<meta name="description" content="[^"]*(?:\n[^"]*)*" />',
              f'<meta name="description" content="{new_desc}" />', html)
html = html.replace(f'>{old_title_text}</h1>', f'>{new_title}</h1>')
html = html.replace(f'datetime="{old_date}" pubdate', f'datetime="{new_date}" pubdate')
html = html.replace(f'<span>{old_date}</span>', f'<span>{new_date}</span>')

# Build content HTML
lines = ARTICLE_RAW.split("\n")
paras = []
first = True
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    is_heading = False
    if len(line) < 120 and not line.endswith(".") and not line.endswith("?") and i > 0:
        nxt = i + 1
        while nxt < len(lines) and not lines[nxt].strip():
            nxt += 1
        if nxt < len(lines) and len(lines[nxt].strip()) > 100:
            is_heading = True
    esc = html_module.escape(line)
    if is_heading:
        paras.append(f'<p class="" style="white-space:pre-wrap;"><strong>{esc}</strong></p>')
    elif first:
        paras.append(f'<p class="" style="white-space:pre-wrap;"><strong>{esc}</strong></p>')
        first = False
    else:
        paras.append(f'<p class="" style="white-space:pre-wrap;">{esc}</p>')

content_html = "\n".join(paras)
old_pat = r'<div class="sqs-html-content" data-sqsp-text-block-content>.*?</div>\n\n  \n<style id="container-styles"'
new_cnt = f'<div class="sqs-html-content" data-sqsp-text-block-content>\n{content_html}\n</div>\n\n  \n<style id="container-styles"'
html, n = re.subn(old_pat, new_cnt, html, flags=re.DOTALL, count=1)
print(f"  Content replaced: {n}")

# Fix pagination
old_pag = r'<section\s+id="itemPagination"[^>]*>.*?</section>'
new_pag = """<section
  id="itemPagination"
  class="item-pagination item-pagination--prev-next"
  data-collection-type="blog-basic-grid"
>

    <a href="overcoming-barriers-to-fully-funded-solar-in-large-businesses.html" class="item-pagination-link item-pagination-link--prev">
      <div class="item-pagination-icon icon icon--stroke">
        <svg class="caret-left-icon--small" viewBox="0 0 9 16">
          <polyline fill="none" stroke-miterlimit="10" points="7.3,14.7 2.5,8 7.3,1.2"/>
        </svg>
      </div>
      <span class="pagination-title-wrapper">
        <div class="visually-hidden">Previous</div>
        <div class="item-pagination-prev-next">Previous</div>
        <h2 class="item-pagination-title">Sun on the Horizon: Overcoming Barriers to Fully Funded Solar in Large Businesses</h2>
      </span>
    </a>


</section>"""
html, n2 = re.subn(old_pag, new_pag, html, flags=re.DOTALL, count=1)
print(f"  Pagination replaced: {n2}")

out = REPO / "insight" / f"{new_slug}.html"
out.write_text(html, encoding="utf-8")
print(f"  Written: {out}")

# ── Update insight.html listing ───────────────────────────────────────────────
listing = REPO / "insight.html"
listing_html = listing.read_text(encoding="utf-8")

new_card = """    <article class="blog-basic-grid--container entry blog-item">

        <div>
          <a href="insight/the-salesperson-the-algorithm-and-the-energy-bill.html" class="image-wrapper" data-animation-role="image">
<img src="/assets/images/ai-b2b-energy-sales.jpg" alt="The Salesperson, the Algorithm, and the Energy Bill" width="1280" height="720" class="image" style="display:block;position: absolute; height: 100%; width: 100%; object-fit: cover; object-position: 50% 50%;" loading="lazy" decoding="async">
</a>
        </div>
        <div class="blog-article-spacer"></div>

      <div class="blog-basic-grid--text">
        <div class="blog-meta-section">
  <span class="blog-meta-primary">
      <span class="blog-author">Martyn Sheridan</span>
    <time class="blog-date" pubdate data-animation-role="date">24/03/2026</time>
  </span>
  <span class="blog-meta-delimiter"></span>
  <span class="blog-meta-secondary">
      <span class="blog-author">Martyn Sheridan</span>
    <time class="blog-date" pubdate data-animation-role="date">24/03/2026</time>
  </span>
</div>
<h1 class="blog-title">
    <a href="insight/the-salesperson-the-algorithm-and-the-energy-bill.html" data-no-animation>
    The Salesperson, the Algorithm, and the Energy Bill. How AI Is Reshaping B2B Energy Sales
  </a>
</h1>
<div class="blog-excerpt">
  <div class="blog-excerpt-wrapper"><p class="" style="white-space:pre-wrap;">After 30 years in sales leadership and the best part of two decades working in and around the energy sector, I have watched this industry go through more reinventions than I care to count. This latest shift - AI - has the potential to be the most disruptive of the lot.</p></div>
</div>
<a class="blog-more-link" href="insight/the-salesperson-the-algorithm-and-the-energy-bill.html" data-animation-role="content">Read More</a>
      </div>
    </article>

    <article class="blog-basic-grid--container entry blog-item">"""

# Insert before the first article (the-rising-tide)
marker = '    <article class="blog-basic-grid--container entry blog-item">\n      \n        <div>\n          <a href="insight/the-rising-tide-of-non-commodity-costs.html"'
if marker in listing_html:
    listing_html = listing_html.replace(marker,
        new_card + '\n      \n        <div>\n          <a href="insight/the-rising-tide-of-non-commodity-costs.html"', 1)
    print("  insight.html updated")
else:
    print("  WARNING: insight.html marker not found - may already be updated or needs manual edit")

listing.write_text(listing_html, encoding="utf-8")

# ── Update overcoming-barriers Next link ──────────────────────────────────────
ob_path = REPO / "insight" / "overcoming-barriers-to-fully-funded-solar-in-large-businesses.html"
ob_html = ob_path.read_text(encoding="utf-8")

next_link = """

    <a href="the-salesperson-the-algorithm-and-the-energy-bill.html" class="item-pagination-link item-pagination-link--next">
      <span class="pagination-title-wrapper">
        <div class="visually-hidden">Next</div>
        <div class="item-pagination-prev-next">Next</div>
        <h2 class="item-pagination-title">The Salesperson, the Algorithm, and the Energy Bill. How AI Is Reshaping B2B Energy Sales</h2>
      </span>
      <div class="item-pagination-icon icon icon--stroke">
        <svg class="caret-right-icon--small" viewBox="0 0 9 16">
          <polyline fill="none" stroke-miterlimit="10" points="1.7,1.3 6.5,8 1.7,14.7"/>
        </svg>
      </div>
    </a>

</section>"""

if 'the-salesperson' not in ob_html:
    ob_html = ob_html.replace('\n  \n</section>\n\n            \n          \n        \n      </main>',
                              next_link + '\n\n            \n          \n        \n      </main>', 1)
    ob_path.write_text(ob_html, encoding="utf-8")
    print("  overcoming-barriers.html updated with Next link")
else:
    print("  overcoming-barriers.html already has Next link")

print("\nDone! Now run:")
print("  git pull origin main")
print("  git add insight/the-salesperson-the-algorithm-and-the-energy-bill.html insight.html insight/overcoming-barriers-to-fully-funded-solar-in-large-businesses.html assets/images/ai-b2b-energy-sales.jpg")
print('  git commit -m "Add AI article and image"')
print("  git push")

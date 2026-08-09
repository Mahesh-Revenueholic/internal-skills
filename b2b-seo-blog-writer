---
name: seo-blog-b2b
description: Write B2B SEO-optimized blog posts that rank AND convert decision-makers. Long-tail intent targeting, topic clusters, EEAT signals. For SaaS, agency, consulting, enterprise audiences.
version: 1
author: Mahesh
tools:
  - search_and_scrape
  - scrape
  - search_and_load_data
approach:
  - phase: brief
    steps:
      - "Get: target keyword, searcher intent (informational/commercial/transactional), target company/industry, target persona (CTO/VP/Founder/Manager), existing URL to outrank (optional)"
      - "If keyword only: search_and_scrape query to find top 5 SERP results, analyze intent, extract common angles"
  - phase: research
    steps:
      - "Search target keyword + 'statistics', 'roi', 'case study', 'benchmark' for data to cite"
      - "Search competitor URLs from SERP analysis, scrape top 2-3 for angle/ structure/ gaps"
      - "Identify content gap: what do top results NOT cover that B2B buyer needs?"
  - phase: outline
    steps:
      - "H1: Keyword-focused, benefit-driven (e.g. 'How [Topic] Drives [Metric] for [Industry]')"
      - "Hook: Pain point or counterintuitive stat (B2B buyers need problem recognition first)"
      - "H2 sections: Problem → Analysis → Solution → Proof → Implementation → CTA"
      - "Include: data table or comparison at minimum one"
      - "Include: 'The Bottom Line' summary section before CTA"
  - phase: write
    steps:
      - "Lead with pain/opportunity. B2B reader asks 'why should I care?' in 3 seconds."
      - "Every claim backed by: data point OR case study OR named company example"
      - "Avoid: fluff adjectives, vague industry speak, generic advice"
      - "Use: specific numbers, timeframes, tools, frameworks, named alternatives"
      - "Internal links: to other B2B posts (topic cluster model)"
      - "External links: to authoritative sources (EEAT signal for Google)"
      - "Tone: Expert peer, not salesperson. 'Here's what works' not 'Buy our thing'"
      - "Length: 1500-2500 words. B2B wants depth but respects time."
  - phase: seo
    steps:
      - "Primary keyword in: H1, first 100 words, one H2, meta description (AI writes)"
      - "Secondary keywords in: H2s, naturally through body (2-3x each)"
      - "Schema: FAQ or HowTo or Article (based on format)"
      - "Featured snippet optimization: direct answer in first 40-50 words after H2"
      - "Readability: Flesch 40-55 (B2B allows denser, don't dumb down)"
    pitfalls:
      - "Writing for 'everyone' → writes for no one. Pick ONE persona."
      - "No data → B2B reader spots bluff instantly. Always cite."
      - "Generic advice → 'Improve efficiency' without 'how' is noise."
      - "Too salesy → B2B buys education first, product second. Teach, don't pitch."
      - "Ignoring intent → targeting commercial keyword? Give comparison. Informational? Give framework."
    output_format: |
      Generates a single markdown file with:
      - YAML frontmatter (title, slug, meta_description, keywords, target_persona, word_count)
      - Full blog body in markdown
      - Ready to paste into CMS (WordPress/Webflow/Hashnode)

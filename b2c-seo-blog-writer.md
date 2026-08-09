---
name: seo-blog-b2c
description: Write B2C SEO-optimized blog posts that rank for informational and commercial keywords. Question-based targeting, featured snippet optimization, readability-first. For D2C, ecommerce, service businesses.
version: 1
author: Mahesh
tools:
  - search_and_scrape
  - scrape
  - search_and_load_data
approach:
  - phase: brief
    steps:
      - "Get: target keyword, intent (informational/commercial/comparison), target audience (age/concern/desire), product/category (if commercial)"
      - "If keyword only: search_and_scrape to find 'People Also Ask' questions, top 5 SERP, featured snippet style"
  - phase: research
    steps:
      - "Scrape top 3 SERP results, analyze: hook style, structure pattern, featured snippet format"
      - "Search 'keyword + vs', 'keyword + best', 'keyword + how to' for commercial intent angles"
      - "Search Reddit Quora for real consumer questions/ pain points around keyword"
  - phase: outline
    steps:
      - "H1: Question-based or benefit direct (e.g. '[Topic]: Complete Guide for [Audience]' or 'Best [Product] for [Need] in 2026')"
      - "Hook: Relatable pain, surprising fact, or direct question to reader"
      - "H2 sections: What → Why → How → Compare → Choose → FAQs"
      - "Include: comparison table if commercial intent"
      - "Include: 'Key Takeaways' box (bullet summary for skimmers)"
  - phase: write
    steps:
      - "Lead with reader's pain/desire, not product. They clicked for THEM, not you."
      - "Use: short paragraphs (2-3 sentences max), conversational tone, 'you' throughout"
      - "Benefits over features. 'Saves 2 hours/week' > 'Has batch processing'"
      - "Social proof: numbers, reviews, ratings, user count (even unnamed)"
      - "Comparison: neutral. Give pros/cons. B2C trusts honesty over hype."
      - "Internal links: to product pages, category pages, related guides"
      - "External links: to reputable reviews, studies, authorities"
      - "Tone: Smart friend who did the research. Not professor, not used car salesman."
      - "Length: 1000-2000 words. B2C reads on phone. Respect attention span."
  - phase: seo
    steps:
      - "Primary keyword in: H1, first 100 words, one H2, meta description"
      - "Question keywords in: FAQ schema. Each Q&A pair targets 'People Also Ask'"
      - "Featured snippet: format list/bold answer in first paragraph after H2"
      - "Image alt text: keyword-rich but natural"
      - "Readability: Flesch 60-75. B2C needs skimmable. Bullets, bold, short sentences."
      - "Mobile first: every subheading visible without scroll-scroll-scroll"
    pitfalls:
      - "Feature dumping → B2C doesn't care what it DOES. Cares what it DOES FOR THEM."
      - "Too technical → Jargon loses the reader in 5 seconds. Explain like they're 15."
      - "Hiding downsides → 'This product is perfect' kills trust. Be real."
      - "No structure → Wall of text = bounce. Every paragraph must earn its place."
      - "Weak CTA → 'Click here' is dead. Give them a reason: 'See why 5000 people switched'"
    output_format: |
      Generates a single markdown file with:
      - YAML frontmatter (title, slug, meta_description, keywords, audience, word_count)
      - Full blog body in markdown
      - Readability score note
      - Ready for CMS paste

---
name: seo-blog-pipeline
description: "Full SEO blog pipeline: 7-phase workflow from research to publish-ready content. Auto-resolves secondary keywords, audience, tone, and competitors via SERP analysis."
version: 3.0
tools:
  - web search
  - web scrape
  - memory recall
  - file save
approach:
  - "Phase 1: Context - check memory, match skills, scrape client site, auto-research optional fields"
  - "Phase 2: SERP - search keyword, scrape top 5, identify gaps, choose differentiation format"
  - "Phase 3: MCQ - hard gate, present foundational questions, wait for answers before proceeding"
  - "Phase 4: Draft - first draft using B2B/B2C skill, 2000-3500 words, grade 5 reading level"
  - "Phase 5: Review - anti-slop checks in a loop (minimum 5 runs), literal-match banned patterns"
  - "Phase 6: Polish - address all issues, engagement pass, write meta assets, re-verify"
  - "Phase 7: Deliver - final blog post with all meta assets and auto-field report"
pitfalls:
  - "Don't skip the review stage (Phase 5)"
  - "No fabrication of data, quotes, or statistics"
  - "Compliant-but-boring = failed draft"
  - "If blocked: self-diagnose and continue (don't stop and wait)"
  - "Target: 10-15 minutes per blog, zero revision rounds"
output_format: "blog post + title tag + meta description + URL slug + editor's note + internal links + FAQ section + auto-field report"
---

# SEO Blog Pipeline

## Required Inputs

These four fields must be provided by the user. Everything else is auto-resolved.

| Field | Description |
|-------|-------------|
| `client` | Client name |
| `client_website` | Client website URL |
| `primary_keyword` | Target keyword |
| `b2b_or_b2c` | B2B or B2C |

**Auto-resolved fields** (via SERP analysis and web research):
secondary keywords, search intent, audience, word count, tone, competitor URLs, internal links, CTAs, FAQ, meta title, meta description.

---

## Phase 1: Context

**Goal:** Understand the client and load relevant skills.

1. Check memory for brand voice, prior posts, and client-specific context.
2. Match installed skills to the pipeline requirements.
3. Scrape the client website for voice, topics, and CTAs.
4. Auto-research any optional fields that can be resolved from the client site.

**Quality gate:** Client voice and context documented before proceeding.

---

## Phase 2: SERP

**Goal:** Understand the competitive landscape and find the gap.

1. Search the primary keyword.
2. Scrape the top 5 ranking pages.
3. Assess competitors: format, depth, angles, gaps.
4. Identify SERP gaps — what's missing or undercovered.
5. Choose a differentiation format.
6. Resolve auto-fields: secondary keywords, search intent, audience, word count, tone, competitor URLs.

**Quality gate:** SERP gap analysis complete. Differentiation angle chosen.

---

## Phase 3: MCQ (Hard Gate)

**Goal:** Confirm direction before drafting. No auto-answering.

Present foundational multiple-choice questions:

1. Topic angle / approach
2. Target audience
3. Goal of the post
4. Length
5. Tone
6. Key points to cover
7. Data or evidence to include
8. CTA

**Must receive answers before proceeding to Phase 4.** This is a hard gate. Do not skip. Do not auto-answer.

**Quality gate:** All MCQ answers received and acknowledged.

---

## Phase 4: Draft

**Goal:** First draft using the appropriate B2B or B2C skill.

### Writer Rules
- 2000–3500 words
- Grade 5 reading level
- Third person
- 3+ engagement techniques (see below)
- Every tool mentioned must be verified via web search
- No fabricated data, quotes, or statistics

**Quality gate:** Draft meets word count, reading level, and engagement minimums.

---

## Phase 5: Review

**Goal:** Run anti-slop checks until the draft is clean.

### Reviewer Rules
- Minimum 5 review runs
- Literal-match against all 14 banned patterns
- Rate every criterion: **Strong / Needs Work / Weak** — with evidence
- Rewrite any section rated Needs Work or Weak
- Loop until all criteria are Strong or explicitly justified

**Quality gate:** All criteria rated Strong or justified. Zero banned pattern matches.

---

## Phase 6: Polish

**Goal:** Address all remaining issues and prepare meta assets.

### Polisher Rules
1. Address all Critical and Needs Work items from review.
2. Engagement pass — ensure 3+ engagement techniques are present and effective.
3. Write title tag (≤60 characters).
4. Write meta description (≤155 characters).
5. Write URL slug.
6. Write editor's note.
7. Re-verify everything: links, facts, tools, formatting.

**Quality gate:** All review items resolved. Meta assets written. Full re-verification complete.

---

## Phase 7: Deliver

**Goal:** Final delivery with all assets.

### Deliverables
- Final blog post
- Title tag
- Meta description
- URL slug
- Editor's note
- Internal links
- FAQ section
- Auto-field report (what was auto-resolved and how)

---

## Banned Patterns (14)

Literal-match these. Any match = rewrite.

1. Confrontational openings
2. Wall-of-text paragraphs
3. Comparison tables instead of H3s
4. Generic H2s
5. Repetitive closings
6. "Not X, but Y" assessments
7. Generic capability assessments
8. Self-announced honesty
9. Manufactured emphasis
10. Buzzwords
11. Em dashes
12. 20+ word sentences
13. Above grade-5 reading level
14. Unauthorized first-person

---

## Engagement Techniques (8)

Use at least 3 per blog.

1. Named frameworks
2. Specific numbers / thresholds
3. Blunt skip recommendations
4. Surprising openings
5. Threaded narrative
6. Sticky closings
7. Tradeoffs as practical implications
8. Varied tool section structure

---

## Guardrails

- Minimum 1500 words per blog
- No fabrication of data, quotes, or statistics
- Don't skip the review stage (Phase 5)
- If blocked: self-diagnose and continue (don't stop and wait)
- Target: 10–15 minutes per blog, zero revision rounds
- Compliant-but-boring = failed draft

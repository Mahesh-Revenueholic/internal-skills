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
  - "Phase 3: MCQ - hard gate, present questions, wait for answers before proceeding"
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
 
Goal: Confirm direction before drafting. No auto-answering.
 
Present multiple-choice questions to the user to extract advanced and extreme 
level of detail and information before going through for the experience part 
in EEAT. The goal is to make sure whatever we write is unique and helpful, 
but not unique just for the sake of it.
 
DO NOT ASK vague basic questions that you can already answer from memory or 
a web search. This should be drilling into the user's brain.
 
### Question Requirements (MANDATORY)
 
Every MCQ question MUST include three components:
 
1. **Why this question is being asked**
   What specific decision does the answer inform? What goes wrong if we 
   guess wrong here? One or two sentences. No fluff.
 
2. **Claim verification table**
   Any factual claim made within a question ,  about the competitor, the 
   client, the market, user behavior, feature existence ,  MUST be tagged 
   with:
   - **Source**: Where did this claim come from? 
     (client site scrape / SERP analysis / competitor site scrape / 
      general knowledge / assumption)
   - **Confidence**: Verified | Likely | Unverified assumption
   - **Needs user confirmation**: Yes or No
 
   If a question contains zero factual claims (pure strategy/preference 
   questions), state: "No claims in this question."
 
3. **Impact of the answer**
   One sentence: what concretely changes in the draft based on which 
   option the user picks.
 
### Format (use for every question):
 
---
**Q1. [Question text]**
 
*Why we're asking:* [What decision this informs + what breaks if wrong]
 
*Impact:* [What changes in the draft based on the answer]
 
- A) [Option]
- B) [Option]  
- C) [Option]
- D) Something else ,  tell me
 
*Claims in this question:*
| Claim | Source | Confidence | Needs your confirmation? |
|-------|--------|------------|------------------------|
| [claim text] | [source] | [level] | [yes/no] |
---
 
### Rules:
- NEVER present an unverified claim as a fact inside a question.
- If a claim is unverified, the question should explicitly flag it: 
  "We're assuming [X] ,  is this true?"
- If you cannot verify a claim about a competitor, say so. Do not 
  bluff. The user needs to know what's research vs. what's guessing.
- Maximum 8 questions per keyword. Quality over quantity.
- Every question must pass: "Would the user understand WHY I'm asking 
  this and trust the basis of the question?" If no, rewrite.

**Must receive answers before proceeding to Phase 4.** This is a hard gate. Do not skip. Do not auto-answer.

**Quality gate:** All MCQ answers received and acknowledged.

---

## Phase 4: Draft

**Goal:** First draft using appropriate B2B or B2C copywriting skills. Use conversational direct response copywriting practices.

### Writer Rules
- Grade 5 reading level
- Third person
- Every tool, statistic or another company or claims mentioned must be verified via web search
- No fabricated data, quotes, or statistics
- Do not make TYPE I OR TYPE II errors. Check for false positive or false negative claims.
- Do not undersell (for example, state an important feature but not actually make it sound important)
- Do no oversell
- When comparing competitors, run every claim to make sure it is not a false negative (eg. a competitor has a feature but you wrote as if they didn't) or a false positive (eg. a competitor does not have a feature but you said they do) 

**Quality gate:** Draft meets above standards
---

## Phase 5: Review

**Goal:** Run /fuck-slop skill until no flag

---

## Phase 6: Polish

**Goal:** Address all remaining issues and prepare meta assets.

### Polisher Rules
1. Address all Critical and Needs Work items from review.
3. Write title tag (≤60 characters).
4. Write meta description (≤155 characters).
5. Write URL slug.
6. Write editor's note.
   
**Quality gate:** All review items resolved. Meta assets written. 

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

## Guardrails

- Minimum 1500 words per blog
- No fabrication of data, quotes, or statistics
- Don't skip the review stage (Phase 5)
- If blocked: self-diagnose and continue (don't stop and wait)
- Target: 10–15 minutes per blog, zero revision rounds
- Compliant-but-boring = failed draft

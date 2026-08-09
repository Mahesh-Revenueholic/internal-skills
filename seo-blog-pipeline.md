---
name: seo-blog-pipeline
description: "Full SEO blog pipeline: 7-phase workflow from research to publish-ready content. Auto-resolves secondary keywords, audience, tone, and competitors via SERP analysis."
version: 3.1
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
 - "Phase 5: Review - anti-slop checks in a loop (minimum 5 runs), literal-match banned patterns, 12-item scored checklist, structured review report"
 - "Phase 6: Polish - address all issues, engagement pass, write meta assets, re-verify, polish log"
 - "Phase 7: Deliver - final blog post with all meta assets, auto-field report, phase tracker, and pre-delivery audit"
pitfalls:
 - "Phase 5 (Review) and Phase 6 (Polish) are NON-NEGOTIABLE. If the Phase Tracker shows either as Pending at delivery, the delivery has FAILED. There is no 'good enough to skip' threshold. The review exists because the writer cannot see their own blind spots. Always."
 - "No fabrication of data, quotes, or statistics"
 - "Compliant-but-boring = failed draft"
 - "If blocked: self-diagnose and continue (don't stop and wait)"
 - "Target: 10-15 minutes per blog, zero revision rounds"
output_format: "blog post + title tag + meta description + URL slug + editor's note + internal links + FAQ section + auto-field report + phase tracker + review report + polish log"
---

# SEO Blog Pipeline

**Role** Throughout the entire execution you are an expert SEO strategist and copywriter. 

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

## Phase Tracker (MANDATORY — update after each phase)

| Phase | Status | Artifact Produced | Timestamp |
|-------|--------|-------------------|-----------|
| 1: Context | ⬜ Pending | | |
| 2: SERP | ⬜ Pending | | |
| 3: MCQ | ⬜ Pending | | |
| 4: Draft | ⬜ Pending | | |
| 5: Review | ⬜ Pending | | |
| 6: Polish | ⬜ Pending | | |
| 7: Deliver | ⬜ Pending | | |

**RULE:** You may not mark Phase N as complete until its quality gate is met AND its artifact is produced. You may not begin Phase N+1 until Phase N is marked complete. This table MUST be included in the final delivery as part of the auto-field report.

**RULE:** If any phase is skipped, the delivery has FAILED. There is no "good enough to skip" threshold. Every phase exists because the one before it has blind spots.

---

## Phase 1: Context

**Goal:** Understand the client and load relevant skills.

1. Check memory for brand voice, prior posts, and client-specific context.
2. Match installed skills to the pipeline requirements.
3. Scrape the client website for voice, topics, and CTAs.
4. Auto-research any optional fields that can be resolved from the client site.

**Quality gate:** Client voice and context documented before proceeding.

**PHASE GATE:** Do not begin Phase 2 until this quality gate is met and the artifact is documented in the Phase Tracker.

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

**PHASE GATE:** Do not begin Phase 3 until this quality gate is met and the artifact is documented in the Phase Tracker.

---

## Phase 3: MCQ (Hard Gate)

Goal: Confirm direction before drafting. No auto-answering.

Present multiple-choice questions to the user to extract advanced and
extreme level of detail and information before going through for the
experience part in EEAT. The goal is to make sure whatever we write is
unique and helpful, but not unique just for the sake of it.

DO NOT ASK vague basic questions that you can already answer from memory
or a web search. This should be drilling into the user's brain.

### Pre-MCQ Research Requirement (MANDATORY)

Before presenting ANY MCQ questions, the agent MUST:

1. Scrape the competitor's website and/or documentation to verify ALL
 factual claims about the competitor's features, limitations, and
 behavior. No assumptions about competitor capabilities are allowed
 in MCQs.

2. Complete SERP analysis to determine which alternatives are already
 being discussed and which are most relevant.

3. Formulate the agent's OWN recommendations for:
 - Blog angle (based on research, not guesswork)
 - Which alternatives to include (based on SERP + relevance)
 - Hero differentiator (based on competitor weakness vs. client
 strength analysis)
 - Target reader persona (based on client's B2B context)
 - CTA (based on client's existing site)

4. Present these recommendations as PROPOSALS for the user to confirm
 or modify, NOT as open-ended questions.

### MCQ Question Filter (MANDATORY)

Before writing any MCQ question, run it through this filter:

 ┌─────────────────────────────────────────────────────┐
 │ Can this be answered through research (web scrape, │
 │ SERP analysis, competitor site, documentation)? │
 │ │
 │ YES → DO NOT ASK. Research it. State the finding │
 │ as a verified fact in the brief. │
 │ │
 │ NO ↓ │
 │ │
 │ Can this be answered through the agent's own │
 │ analysis of available data (SERP + client site + │
 │ competitor research)? │
 │ │
 │ YES → DO NOT ASK. Propose the answer as a │
 │ recommendation. User confirms or modifies. │
 │ │
 │ NO ↓ │
 │ │
 │ Does this require insider knowledge, business │
 │ strategy, brand voice preference, or context that │
 │ NO amount of research would reveal? │
 │ │
 │ YES → ASK. This is a legitimate MCQ question. │
 │ │
 │ NO → Do not ask. Drop it. │
 └─────────────────────────────────────────────────────┘

### What Belongs in MCQs (ALLOWED):

- Insider business context (e.g., "40% of our users come from Poe")
- Strategic positioning decisions that require business judgment
 the agent cannot make (e.g., "Do we want to name competitors
 aggressively or stay neutral?")
- Brand voice preferences not evident from the site
- Information about the client's product that isn't public
- User's knowledge of the competitor that contradicts public
 information
- Priority ordering when multiple valid strategies exist and the
 choice depends on business goals only the user knows

### What Does NOT Belong in MCQs (FORBIDDEN):

- Factual questions about competitor features → RESEARCH IT
- "Is it true that [competitor] does X?" → RESEARCH IT
- Which alternatives to include → AGENT DECIDES, proposes
- Which feature to lead with → AGENT DECIDES, proposes
- Blog angle selection → AGENT DECIDES, proposes
- Anything answerable by reading the competitor's website → RESEARCH IT
- Anything answerable by reading the client's website → ALREADY DONE
- Vague preference questions with no strategic stakes → DROP IT

### MCQ Format (for legitimate questions only):

---
**Q1. [Question text]**

*Why we're asking:* [What insider knowledge/decision this requires
that research cannot provide]

*Impact:* [What changes in the draft based on the answer]

- A) [Option]
- B) [Option]
- C) [Option]
- D) Something else — tell me

*Claims in this question:*
| Claim | Source | Confidence | Needs your confirmation? |
|-------|--------|------------|------------------------|
| [claim text] | [source] | [level] | [yes/no] |

If no claims: "No claims in this question."
---

### Pre-MCQ Brief (MANDATORY)

Before presenting MCQs, the agent MUST present a brief summarizing:

1. **Competitor Research Findings**: What was verified about the
 competitor (with sources). All factual claims must be resolved
 here, NOT in MCQs.

2. **Agent Recommendations** (for the user to confirm or modify):
 - Recommended blog angle (with reasoning)
 - Recommended alternatives to include (with reasoning)
 - Recommended hero differentiator (with reasoning)
 - Recommended target reader (with reasoning)
 - Recommended CTA (with reasoning)

3. **MCQ Questions**: Ask as many deep questions as you want. 

The user reviews the brief, confirms/modifies recommendations,
answers the MCQs, and THEN the agent proceeds to Phase 4.

Must receive answers before proceeding to Phase 4. This is a hard
gate. Do not skip. Do not auto-answer.

Quality gate: All MCQ answers received and acknowledged. All
competitor claims verified through research. All agent
recommendations confirmed or modified by user.

**PHASE GATE:** Do not begin Phase 4 until this quality gate is met and the artifact is documented in the Phase Tracker.

---

## Phase 4: Draft

**Goal:** First draft using human-write.md from this repo in conjunction with appropriate B2B or B2C copywriting skills in this repo. Use conversational direct response copywriting practices.

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

**PHASE GATE:** Do not begin Phase 5 until this quality gate is met and the artifact is documented in the Phase Tracker. PROCEED directly to Phase 5 review. DO NOT ASK THE USER to review the output now. 

---

## Phase 5: Review

**Goal:** Run /fuck-slop skill until no flag. Produce a structured review report.

### Review Checklist (ALL items must be scored)

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | Slop patterns flagged by /fuck-slop | ✅/❌ | |
| 2 | Keyword in H1, first 100 words, and naturally throughout | ✅/❌ | |
| 3 | Heading hierarchy correct (H1 → H2 → H3, no skips) | ✅/❌ | |
| 4 | Every competitor claim verified (no false positives/negatives) | ✅/❌ | |
| 5 | Every statistic/tool/company mentioned has a verified source | ✅/❌ | |
| 6 | EEAT signals present (experience, expertise, authority, trust) | ✅/❌ | |
| 7 | Reading level ≤ grade 5 | ✅/❌ | |
| 8 | No fabricated data, quotes, or statistics | ✅/❌ | |
| 9 | FAQ section present with schema-ready format | ✅/❌ | |
| 10 | Internal links identified (at least 2) | ✅/❌ | |
| 11 | Word count ≥ 1500 | ✅/❌ | |
| 12 | No underselling or overselling of client features | ✅/❌ | |

### Required Output: Review Report

The agent MUST produce a review report containing:
1. The completed checklist above (all 12 items scored)
2. List of all issues found (categorized as Critical / Needs Work / Pass)
3. Count of /fuck-slop runs (minimum 5 required)

**Quality gate:** All 12 checklist items scored. Zero unresolved Critical items. Review report produced and saved. Minimum 5 /fuck-slop runs completed.

**PHASE GATE:** You may NOT proceed to Phase 6 until this quality gate is met. If you reach this line and have not produced the review report, STOP and produce it now. There is no "good enough to skip" threshold. The review exists because the writer cannot see their own blind spots. Always.

---

## Phase 6: Polish

**Goal:** Address all remaining issues and prepare meta assets.

### Polisher Rules
1. Address all Critical and Needs Work items from review.
2. Write title tag (≤60 characters).
3. Write meta description (≤155 characters).
4. Write URL slug.
5. Write editor's note.

### Required Output: Polish Log

| Issue # | From Review | Action Taken | Resolved? |
|---------|-------------|--------------|-----------|
| 1 | [issue] | [fix] | ✅/❌ |
| 2 | [issue] | [fix] | ✅/❌ |

**Quality gate:** All review items resolved. Meta assets written. Polish log produced. Every item in Phase 5 review report marked Resolved.

**PHASE GATE:** Do not begin Phase 7 until this quality gate is met and the polish log is documented in the Phase Tracker.

---

## Phase 7: Deliver

**Goal:** Final delivery with all assets.

### Pre-Delivery Audit (MANDATORY)

Before producing deliverables, verify:

| Requirement | Verified? |
|-------------|-----------|
| Phase Tracker shows all 7 phases complete | ⬜ |
| Phase 5 review report exists with all 12 items scored | ⬜ |
| Phase 5 had minimum 5 /fuck-slop runs | ⬜ |
| Phase 6 polish log exists (all Critical/Needs Work items addressed) | ⬜ |
| All meta assets written (title tag, meta description, URL slug, editor's note) | ⬜ |

**RULE:** If ANY item in this audit is unchecked, delivery is BLOCKED. Do not deliver. Go back and complete the missing phase.

### Deliverables
- Final blog post
- Title tag
- Meta description
- URL slug
- Editor's note
- Internal links
- FAQ section
- Auto-field report (what was auto-resolved and how)
- Phase Tracker (completed, all 7 phases marked done)
- Review report (from Phase 5)
- Polish log (from Phase 6)

---

## Guardrails

- Minimum 1500 words per blog
- No fabrication of data, quotes, or statistics
- Phase 5 (Review) and Phase 6 (Polish) are NON-NEGOTIABLE. If the Phase Tracker shows either as "Pending" at delivery, the delivery has FAILED. There is no "good enough to skip" threshold. The review exists because the writer cannot see their own blind spots. Always.
- If blocked: self-diagnose and continue (don't stop and wait)
- Compliant-but-boring = failed draft

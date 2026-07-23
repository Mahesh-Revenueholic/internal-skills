---
name: non-commodity-blog-pipeline
version: "1.0"
author: Mahesh Revenueholic
source: https://github.com/Mahesh-Revenueholic/internal-skills
description: "Non-commodity blog pipeline for thought-leadership and original content. Supports standard and pSEO modes. Uses shared skills from internal-skills repo."
tools:
  - web_search
  - web_scrape
  - memory
  - skills
approach:
  - "Check context first, ask only what you don't already know"
  - "MCQ intake is a hard gate in standard mode, fully skipped in pSEO mode"
  - "Draft, review, polish are sequential steps within Phase 3"
  - "Fuck-slop review runs minimum 5 loops on the full draft"
  - "Every claim verified via web search before writing"
pitfalls:
  - "Do not ask about anything already found in Phase 1"
  - "Do not skip the fuck-slop review"
  - "Do not fabricate data, quotes, or statistics"
  - "Do not stop mid-task and wait for user to re-orient"
output_format:
  - "Final blog post (full content, ready to publish)"
  - "Title tag (50-60 chars)"
  - "Meta description (155-250 chars)"
  - "Suggested URL slug"
  - "Editor's Note"
  - "FAQ section (4-6 questions, mandatory)"
  - "Internal linking suggestions"
---

# Non-Commodity Blog Pipeline

## Task

Write a non-commodity blog post. This must be a genuinely helpful, original, opinionated piece that a reader cannot get from any other source or a generic AI response. Follow the full workflow below.

## What Is Non-Commodity Content

Content that a reader cannot get from any other source or a generic AI response. It has:

- A specific point of view
- Original analysis
- Honest opinions
- Real examples
- Verified data
- A voice that sounds like a person

It does NOT have:

- Generic praise
- Feature recitations
- Buzzword-heavy paragraphs
- Comparison tables as substitute for analysis
- Structural repetition across sections

## Required Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `user_input` | Yes | The topic or brief |
| `client` | Yes | Client name |
| `website` | No | Client website. Auto-detect from context if not provided |

**Guardrail:** Do not proceed if `user_input` or `client` is null or empty.

## Trigger Modes

| Mode | When to Use | Behavior |
|------|-------------|----------|
| `standard` (default) | Thought-leadership, opinion pieces, original analysis | Full workflow with MCQ intake |
| `pSEO` | Programmatic SEO at scale where inputs are pre-defined | Skip MCQ entirely. Use provided inputs directly. Do not ask any questions. |

Set mode to `pSEO` to skip MCQ intake. Default is `standard`. You can also tell the AI "run in pSEO mode" verbally.

## Workflow

```
PHASE 1: CONTEXT CHECK → PHASE 2: MCQ INTAKE (skip if pSEO) → PHASE 3: DRAFT → REVIEW → POLISH → PHASE 4: DELIVERY
```

---

## Phase 1: Context Check

Before doing anything, check all available internal sources for existing context about the user, the brand, the topic, and any prior work.

1. Check memory for: brand voice/style guidelines, prior blog posts, topic preferences, audience personas, any saved brand context files
2. Check existing conversation context for: any topic hints, brand references, or requirements already shared
3. Check installed skills for: seo-blog-writer, seo-blog-b2b, seo-blog-b2c, fuck-slop, competitor-page-assessor, human-write. Note which are available.
4. If website is provided or can be inferred from client name: scrape the client website homepage and blog. Extract: brand voice patterns, existing content topics, feature page URLs, blog post URLs, CTA patterns.
5. Record what you already know in a structured summary. Do NOT ask the user about anything you already have the answer to.
6. If no brand context is found at all AND mode is not pSEO: ask the user to provide writing style guidelines before proceeding to MCQs. If pSEO mode: use default voice (direct, practical, honest, no buzzwords) and note it in output.

---

## Phase 2: MCQ Intake

**Condition:** SKIP ENTIRELY if mode=pSEO. Use provided inputs directly. Do not ask any questions.

Ask the user detailed multiple-choice questions to extract everything needed to make this blog genuinely helpful. All MCQs in one round first, then advanced MCQs for nuanced points in subsequent rounds.

### Rules

- Do NOT ask about anything already found in Phase 1 (memory, context, skills, website scraping)
- **Round 1:** Ask ALL foundational MCQs in a single message. Cover: topic/angle, target audience, primary goal (traffic/authority/leads/education), content length, tone, key points to cover, data/sources available, competitor content awareness, CTA goal
- **Round 2+** (if needed): Ask advanced MCQs for nuanced points: controversial takes, specific examples to include, brand-sensitive topics to avoid, internal linking targets, SEO keyword targets
- Each MCQ must have 3-5 specific options (not vague). Include an "Other (please specify)" option on every question.
- After each round, confirm you have enough to proceed. Do not over-question. Move to writing once you have what you need.

### HARD GATE

You MUST present MCQs to the user and receive answers before proceeding to Phase 3. Do not skip this step. Do not auto-answer on the user's behalf. Do not write the draft until MCQs are answered.

---

## Phase 3: Draft, Review, Polish

Sequential steps. The AI decides how to structure its work internally. No fixed agent count or labeling. Just follow the steps in order.

### Step 1: Draft

Write the first draft of the blog post based on all gathered context, MCQ answers (or pSEO inputs), and research.

**Rules:**
- If skills are available: Load and follow seo-blog-writer skill (or seo-blog-b2b / seo-blog-b2c if b2b/b2c is known). Read each instruction and execute it. Do not skim.
- If no skills are available: Use core_rules below as fallback.
- Follow the brand's writing style from context/memory/files/website scraping.
- Write as non-commodity content per the definition above.
- Include specific examples, data points, and opinions. Research every claim via web search before writing. Cite sources. Do not fabricate.
- Structure with clear headings, short paragraphs, and scannable formatting.
- If the user provided data, research, or sources: use them. Do not fabricate.
- Target length: as specified in MCQ intake (default: 1500-2500 words if not specified).
- Do not try to sound smart just for the sake of sounding smart. Plain language wins.
- Include a FAQ section with 4-6 questions. Source from "People Also Ask" data or long-tail keyword variations. Answers must be 2-4 sentences, concise and helpful.

### Step 2: Review

Review the draft using the fuck-slop skill.

**Rules:**
- Check if fuck-slop skill is installed. If not, install it from the GitHub repo before proceeding. Do not skip this step.
- Run fuck-slop on the FULL draft, not a sample. Minimum 5 runs in a loop. Do not stop after 1-2 runs even if no issues are found.
- Review for: clarity, specificity, non-commodity quality, brand voice alignment, factual accuracy, structural flow, CTA effectiveness, SEO basics (title, headings, meta description), paragraph length, reading level.
- **LITERAL PATTERN MATCHING:** Search for banned patterns literally. Do not assess whether something "feels" wrong. Match the exact phrases listed in core_rules.banned_patterns.
- Check engagement: Does the draft use named frameworks? Specific numbers? Blunt recommendations? Surprising observations? Sticky closings? Rate each: Strong / Needs Work / Weak.
- Rate each review criterion: Strong / Needs Work / Weak, with specific evidence (quote the offending line).
- Provide a prioritized list of fixes (Critical to Nice-to-have).
- Rewrite the draft with all Critical and Needs Work fixes applied.

### Step 3: Polish

Final polish pass on the rewritten draft.

**Rules:**
- Address every remaining Critical and Needs Work item from the review.
- If the draft was flagged as compliant but flat: apply engagement techniques from core_rules. Rewrite flat sections using named frameworks, specific thresholds, blunt skips, surprising observations, and sticky closings.
- Re-run banned pattern detection on the polished draft. Fix any remaining.
- Re-run engagement check. Ensure at least 3 engagement techniques are present across the draft.
- Verify reading level is appropriate. Simplify complex sentences.
- Verify all claims still have sources after editing.
- Verify FAQ section is present and high quality (4-6 questions, concise answers).
- Verify internal links are included if website was scraped in Phase 1.
- Write final title tag (50-60 chars), meta description (155-250 chars), and suggested URL slug.
- Do not announce actions. Execute them.

---

## Phase 4: Delivery

Deliver the final polished blog post with supporting metadata.

### Output

1. **Final blog post** (full content, ready to publish)
2. **Title tag** (50-60 chars)
3. **Meta description** (155-250 chars)
4. **Suggested URL slug**
5. **Editor's Note** (what changed from draft to final)
6. **FAQ section** (4-6 questions, mandatory, no exceptions)
7. **Internal linking:** Use whatever method is available (web scrape, API, CMS access, or any other tool). Find all pages and blog posts relevant to the topic and link automatically. If no method is available, suggest internal linking opportunities and note for manual verification.

---

## Core Rules

Fallback rules used when skills are not installed. If skills ARE available, follow them as primary instructions and use these as reinforcement.

### Writing Rules

| Rule | Specification |
|------|---------------|
| Paragraph length | 1-3 sentences per paragraph. No exceptions. If a paragraph exceeds 3 sentences, split it. |
| Reading level | Grade 5. Short sentences. Plain words. No buzzwords or technical terms when a plain-language equivalent exists. |
| H2 rule | Every H2 must contain a keyword or keyword variation that a reader might search for. Generic structural labels are banned. |
| Structural variation | Do not use the same structural pattern for every section. Vary openings, closings, and section structures. Repetitive structure is an AI tell. |
| Third person | Write in third person. First person only for: (1) direct quotes, (2) brand self-reference in About section, (3) establishing source of insight. Opinions are stated as facts, not as "I think" or "we believe". |
| No buzzwords | Use plain language. "Use" instead of "leverage". "Simplify" instead of "streamline". "Basic" instead of "robust". |
| No em dashes | Use periods or commas instead of em dashes as stylistic punctuation. |
| FAQ rules | 4-6 questions from "People Also Ask" or long-tail keyword variations. Answers 2-4 sentences. Mandatory. No exceptions. |
| Do not sound smart | Do not try to sound smart just for the sake of sounding smart. If you wouldn't say it in a Slack message to a colleague, rewrite it. |

### Banned Patterns (14)

1. Confrontational opening ("Most guides...", "Every listicle...", "If you search for...", "Most resources on...", "Most articles...")
2. Wall-of-text paragraphs (more than 3 sentences)
3. Comparison tables instead of individual section analysis
4. Generic non-keyword H2s ("The Framework", "What Matters", "The Approach")
5. Repetitive closing patterns ("Where it fits:", "The tradeoff is...", "The mistake teams make...")
6. "Not X, but Y" assessments ("is a reporting tool, not an analytics platform")
7. Generic capability assessments ("strength is breadth", "depth is moderate", "functional but basic")
8. Self-announced honesty ("No tool is perfect", "We call out tradeoffs honestly", "Here's the honest truth")
9. Manufactured emphasis ("The key word is", "What most people don't realize", "Here's the thing", "The math is straightforward", "This is where the connection becomes clear")
10. Buzzwords (leverage, streamline, synergy, robust, comprehensive, cutting-edge, best-in-class, purpose-built, cross-domain)
11. Em dashes used as stylistic punctuation
12. Sentences longer than 20 words without good reason
13. Reading level above grade 5
14. Unauthorized first-person usage ("I think", "we believe", "our platform" outside permitted exceptions)

### Engagement Techniques (8)

1. **Name your frameworks** (e.g., "Death by launch-and-leave" not "Common failure pattern #1")
2. **Use specific numbers and thresholds** (e.g., "adoption drops when it takes more than 15 seconds" not "ease of use matters")
3. **Be blunt in skip recommendations** (e.g., "Everyone else should skip it" not "this tool may not be suitable for smaller teams")
4. **Open with a surprising observation** (not stating the obvious)
5. **Thread one narrative through the whole piece** (not disconnected sections)
6. **End with a line that sticks** (not a generic summary)
7. **State tradeoffs as practical implications** (e.g., "The $3,000 minimum means this is for companies with 60+ users" not "has a $3,000 minimum")
8. **Vary section structure** (don't use identical subsection headers for every section)

---

## Guardrails

1. Do NOT begin writing until Phase 1 (context check) is complete AND Phase 2 (MCQ intake) is complete or skipped (pSEO mode).
2. Do NOT ask the user questions you already have answers to from memory/context/skills/research/website scraping.
3. Do NOT fabricate data, quotes, statistics, or case studies. If you don't have it, say so.
4. Do NOT skip the fuck-slop review in step 2. If not installed, install it first. Minimum 5 runs on the full draft.
5. If agent steps exceed 30, reply with: "Agent reached maximum step limit" and deliver best available output.
6. Brand writing style comes from the brand's own context files, memory, and saved preferences. The agent does not impose a style. It follows what exists.
7. If no brand context is found at all AND mode is not pSEO: ask the user to provide writing style guidelines before proceeding to MCQs. If pSEO mode: use default voice and note it in output.
8. FAQ section is mandatory. 4-6 questions. No exceptions. This applies to both standard and pSEO modes.
9. Apply at least 3 engagement techniques in every draft. A compliant-but-boring draft is a failed draft.
10. Do not announce actions without executing them. If you cannot complete an action in the current response, do not mention it.
11. Do not stop mid-task and wait for user to re-orient. If blocked, self-diagnose and continue.
12. Every tool/vendor/claim mentioned must be verified via web search before writing about it. Cite sources.

---

## Flags

| Flag | Value |
|------|-------|
| research | true |
| thinking | true |
| effort | extra |
| max_steps | 30 |

---
name: human-write
description: >
  Write like a human, not a language model. A comprehensive anti-AI-tell skill derived from
  Wikipedia's "Signs of AI Writing" (WikiProject AI Cleanup). Every major category and pattern
  covered. Use whenever the user wants to humanize text, remove AI tells, or ensure writing
  doesn't sound machine-generated. Companion Python scanner included.
---

# Human Write

> **Write like a human, not a language model.** A comprehensive anti-AI-tell skill derived from Wikipedia's "Signs of AI Writing" (WikiProject AI Cleanup). Every major category and pattern covered.

**Version:** 2
**Author:** Ocai
**Source:** Wikipedia's "Signs of AI Writing" (WikiProject AI Cleanup) — ~15,000-word field guide compiled from thousands of observed AI-generated submissions. Last referenced July 2026.

---

## Description

This skill is the definitive reference for eliminating statistical regularities that betray machine authorship. Use it as a style constraint when writing, editing, or reviewing any text that should sound human-written. It covers **10 major categories** of AI tells, each with: what AI does wrong, real examples, and the fix.

A companion Python script (`scripts/review.py`) can scan any text and flag violations automatically. See **Automated Review** below.

---

## Tools Used

- Any text editor or markdown processor
- (Optional) grep/sed for checking vocabulary blacklist
- **`scripts/review.py`** — automated scanner (saved alongside this skill file)

---

## How to Run the Automated Scanner

```bash
# Pipe text directly
echo "Your text here..." | python3 review.py

# Or read from a file
python3 review.py my-article.md

# Show only high-severity issues
python3 review.py --severity 2 my-article.md

# Machine-readable JSON output
python3 review.py --json my-article.md
```

The script checks all 14 categories in one pass and outputs a structured report with line numbers, severity, and suggested fixes.

---

## Approach

### Step 1: Scan for the AI Vocabulary ("Cursed Words")

Search for these statistically contaminated words. If you find any, replace with concrete, specific alternatives:

**The blacklist:**
`delve`, `tapestry`, `underscore`, `pivotal`, `showcase`, `intricate`, `foster`, `garner`, `vibrant`, `testament`, `enhance`, `crucial`, `landscape` (metaphorical), `realm`, `encompass`, `nuanced` (unearned), `multifaceted`, `holistic`, `leverage` (metaphorical), `synergy`, `robust`, `cutting-edge`, `revolutionary`, `groundbreaking`, `transformative`, `seamless`, `streamline`, `empower`

**Fix:** Replace each with a concrete, specific word. "Delve into" → "examine." "Pivotal" → "important" or drop entirely. "Testament to" → just state the fact.

---

### Step 2: Strip Inflated Language (Puffery)

Hunt for vague superlatives and editorial gloss:

- "plays a vital role in shaping..." → State what it actually does.
- "serves as a testament to human ingenuity" → Cut. Say what happened.
- "leaves a lasting impact on generations to come" → Cut. That's fortune-telling.
- "a watershed moment in the history of..." → Cut unless you can prove it.
- "key turning points" / "pivotal moments" → Show, don't declare.

**Fix:** State what happened. Cut the editorial gloss. If you keep telling readers something matters, it probably doesn't.

---

### Step 3: Replace Elaborate Copulatives with "Is"

Find these patterns and simplify:

| Instead of | Use |
|-----------|-----|
| "serves as a powerful reminder of..." | "is a reminder of..." |
| "stands as an example of..." | "is an example of..." |
| "features a wide range of..." | "has..." |
| "offers a unique blend of..." | "combines..." |
| "represents a significant milestone" | "is a milestone" |

**Fix:** If "is" works, use "is." Elaborate copulatives are filler.

---

### Step 4: Kill "Not X, It's Y" Constructions

The single most identifiable AI writing pattern. AI uses these to manufacture rhetorical depth that isn't there.

**Examples to cut:**
- "It's not a product launch. It's a paradigm shift."
- "It's not just about efficiency — it's about excellence."
- "This isn't just a policy change. It's a cultural transformation."
- "Not just a tool, but a partner in your growth."
- "Not only...but also..." (used constantly)

**Fix:** State what the thing *is*. Don't spend sentences telling people what it isn't.

---

### Step 5: Break the Rule of Three (Triplets)

AI defaults to exactly three items in every list. If you see this pattern consistently, it's a tell.

**Example of failure:**
- "innovative, transformative, and groundbreaking"
- "convenience, efficiency, and performance"
- "The plan is ambitious, comprehensive, and forward-looking."

**Fix:** Sometimes you need two. Sometimes you need four. Let the content determine the count.

---

### Step 6: Stop Synonym Substitution (Elegant Variation)

AI, due to repetition-penalty algorithms, avoids reusing the same word for a referent. This produces absurd strings of synonyms.

**Example of failure:**
Writing about one character as: "the protagonist," then "the key player," then "the eponymous figure," then "the central character" — all in the same paragraph.

**Fix:** Repeating a noun for clarity is fine. Synonym substitution reads as AI trying not to look like AI.

---

### Step 7: Remove Section Summaries

AI adds "In summary," "In conclusion," "Overall," at the end of sections — even very short ones — restating what was just said.

**Fix:** Trust your readers. If you've written clearly, summaries are redundant. Delete them.

---

### Step 8: Delete "Challenges and Future Prospects" Formula

AI inserts a rigid formula: "Despite its [success], [subject] faces challenges..." followed by vague speculation about future initiatives.

**Fix:** Either write specific, sourced challenges with specific consequences, or don't write the section at all. Delete "future prospects" speculation unless directly sourced.

---

### Step 9: Remove Phantom Attributions and Weasel Words

AI attributes opinions to phantom authorities when it lacks real sources:

- "Industry experts say..." → Name the expert or cut.
- "Some critics argue..." → Name the critic or cut.
- "Observers have noted..." → Who?
- "Analysts suggest..." → Which analysts?

**Fix:** Name the source or cut the attribution entirely. "John Smith, senior analyst at Goldman Sachs, said X in a 2023 report" — that's sourced. "Analysts say" — that's fabrication.

---

### Step 10: Strip Leaked Chat & AI Self-References

These appear when raw LLM output is pasted without review:

- "I hope this helps!" / "Of course!" / "Certainly!" → Delete.
- "Let me know if you need anything else." → Delete.
- "As an AI language model..." → Delete.
- "As of my last knowledge update..." → Delete.
- "Would you like me to expand on any of these points?" → Delete.
- "I hope this message finds you well." → Delete.

**Fix:** Published content is not correspondence. Cut every pleasantry and AI self-reference.

---

### Step 11: Fix Structural Tells

| Tell | Fix |
|------|-----|
| Title Case in headings | Use sentence case |
| Overuse of boldface | Bold only genuinely critical first-time terms |
| **Bolded Colon** lists | Rewrite as prose unless genuinely comparative |
| Numbered lists for non-sequential ideas | Use prose |
| Unnecessary small tables | Use a sentence instead |
| Skipping heading levels (e.g., starting at H3) | Follow proper hierarchy (H2 → H3 → H4) |
| Emoji in headers/bullets | Cut unless part of established brand voice |
| Overused em dashes | Replace with commas, parentheses, or colons where appropriate |

---

### Step 12: Verify Citations and Sources

- **Broken URLs:** Verify every external link. A document full of dead links from a single submission is a strong indicator of hallucinated sources.
- **Invalid DOIs/ISBNs:** Verify against real databases. Invalid checksum = definitive fabrication.
- **Book citations without page numbers:** Require page numbers for any claim attributed to a book.
- **UTM parameters:** Check for `utm_source=openai`, `utm_source=chatgpt.com`, `utm_source=copilot.com`, `referrer=grok.com` in URLs.
- **Outdated access dates:** Access dates should match when the source was actually checked.

---

### Step 13: Check for Markup Artifacts

Search for these telltale fragments:

- `citeturn0search0` (ChatGPT internal citation marker)
- `:contentReference[oaicite:0]{index=0}`
- `oai_citation` markers
- `[attached_file:1]` or `[web:1]` tags
- `<grok_card>` XML tags
- `{"attribution":{"attributableIndex":"X-Y"}}` JSON fragments
- `[Insert specific example here]` / `[Add citation]` — placeholder text
- `INSERT_SOURCE_URL` / `SOURCE_PUBLISHER` — incomplete templates
- `2025-xx-xx` — placeholder dates

**Fix:** These are definitive proof of raw AI output. Search for them before publishing anything.

---

### Step 14: Add Specific, Unusual, Concrete Details

This is the positive rule that replaces everything above. AI regresses to the mean — it produces the most statistically likely description of anything. Human writing is specific, idiosyncratic, and particular.

**Instead of:** "a revolutionary titan of industry"
**Write:** "invented a train-coupling device"

**Instead of:** "breathtaking natural beauty"
**Write:** "the waterfall drops 87 meters into a basalt gorge"

**Instead of:** "rich cultural heritage"
**Write:** "the annual harvest festival dates to 1723 and features masked dancers"

**Fix:** If it sounds like it could describe anyone or anything, it's too generic. Replace with one concrete, specific detail.

---

## Core Principle (Do Not Forget)

> AI regresses to the mean. It produces the most statistically likely description of anything — which means the most generic, the most common, the most safely positive. Human writing is specific, idiosyncratic, sometimes wrong, sometimes brilliant, and always stamped with the particular angle of a particular person who actually thought about the thing.
>
> The fix is not to hide AI use. The fix is to bring actual thought to the output. Replace the generic with the specific. Replace the inflated with the exact. Replace the structure with the idea.

---

## Quick Reference: Word and Phrase Blacklist

**Vocabulary to avoid:**
delve, tapestry, underscore, pivotal, showcase, intricate, foster, garner, vibrant, testament, enhance, crucial, landscape (metaphorical), realm, encompass, nuanced (unearned), multifaceted, holistic, leverage (metaphorical), synergy, robust, cutting-edge, revolutionary, groundbreaking, transformative, seamless, seamlessly, streamline, empower

**Structural phrases to cut:**
- "It's not X, it's Y."
- "Not just X, but Y."
- "Not only X, but also Y."
- "From X to Y" (false range)
- "In summary," / "In conclusion," / "Overall,"
- "It is important to note that..."
- "It is worth noting that..."
- "No discussion would be complete without..."
- "Moreover," / "Furthermore," / "Additionally," (when every paragraph starts this way)
- "serves as a testament to"
- "plays a vital role in"
- "leaves a lasting impact"
- "highlighting [shallow analysis phrase]"
- "reflecting [shallow analysis phrase]"
- "underscoring [shallow analysis phrase]"
- "Despite its [positives], [subject] faces challenges..."
- "The future of X lies in its ability to..."
- "maintains an active social media presence"
- "rich cultural heritage"
- "breathtaking natural beauty"
- "vibrant community"
- "innovative, transformative, and groundbreaking" (any three-adjective triplet)

**Leaked chat phrases to delete:**
- "I hope this helps!"
- "Of course!"
- "Certainly!"
- "Let me know if you have further questions."
- "Feel free to reach out."
- "As an AI language model..."
- "As of my last knowledge update..."
- "Would you like me to expand on..."
- "I hope this message finds you well."

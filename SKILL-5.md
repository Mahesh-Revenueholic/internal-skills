---
name: fuck-slop
description: >
  De-slop pass for any text: detects and erases the statistical fingerprints of
  AI writing (negative parallelism / "not X but Y", em-dash abuse, rule-of-three,
  false ranges, puffery vocabulary, uniform cadence, hedged both-sidesing) and
  rewrites the text into its target register — academic article, tweet, reddit
  post, email, blog, anything between. Use when the user says "fuck slop",
  "f*ck slop", "deslop", "de-slop this", "remove the AI tells", "humanize this",
  "make this not sound like AI", or invokes /fuck-slop. Also use before
  publishing any agent-drafted prose.
---

# F*ck Slop

Strip every mark of AI writing from a text and make it good in its genre. Not "make it pass a detector" — make it read like a specific person with a specific point wrote it for a specific audience.


## Mandatory Execution Rule (READ BEFORE EVERY EXECUTION)

This skill must be executed by running actual grep/search patterns against the full text of the draft. Not a mental checklist. Not a "I wrote it with awareness so it's probably clean" assumption. Run every pattern from the tells.md reference file against every line of the draft.

The most common failure mode is doing a mental scan instead of a mechanical scan. The same priors that produce slop make it invisible on re-read. You cannot reliably see your own slop. Detection must be mechanical.

If the text is in a file, run the grep commands literally. If the text is in conversation, apply each pattern by hand, line by line, and document what you found.

Do not skip this. Do not shortcut this. A draft that has not been mechanically scanned is not reviewed. It is assumed clean, and assumption is the enemy of quality.

---

## Common Pitfalls and Risks

These are the specific failure modes observed when running fuck-slop. Read before every execution.

### Pitfall 1: Mental Checklist Instead of Mechanical Scan
**What goes wrong:** You read through the draft, think "looks good," and tick boxes mentally. You miss patterns because the same priors that produce slop make it invisible on re-read.
**How to prevent it:** Run the actual grep patterns from tells.md against the full text. Every pattern. Every line. Document findings before rewriting.
**Red flag:** You are about to say "the draft looks clean" and you have not run a single grep pattern.

### Pitfall 2: Rewriting Patterns Instead of Rewriting Meaning
**What goes wrong:** You find a "not X but Y" pattern and rewrite it as "less about X than Y." Same move, different wig. The slop survives the rewrite.
**How to prevent it:** When you find a pattern, ask: "What is this sentence actually asserting?" Then assert that directly. Never fix a pattern by paraphrasing the pattern.
**Red flag:** Your rewrite contains "less about," "more than just," or any variant of the original pattern.

### Pitfall 3: Not Re-Scanning After Rewrite
**What goes wrong:** You rewrite the findings, deliver the result, and do not re-scan. The rewrite introduced new tells because the model writing it has the same priors.
**How to prevent it:** Re-run the full Phase 1 scan on your rewritten text. Fix and re-scan until a pass produces zero pattern hits. Cap at 4 passes.
**Red flag:** You are about to deliver a rewritten draft and you have not re-scanned it.

### Pitfall 4: Only Scanning a Sample
**What goes wrong:** You scan the first few paragraphs, find them clean, and assume the rest is clean too. Slop clusters in later sections where attention drops.
**How to prevent it:** Always run the scan against the ENTIRE draft. Not a sample. Not the first 500 words. The entire text.
**Red flag:** You are about to review a draft and you are only looking at part of it.

### Pitfall 5: Missing Repetitive Structural Patterns
**What goes wrong:** You scan for word-level tells (puffery, negation patterns) but miss structural repetition. Every tool section ends with "Where it fits:". Every function section ends with "The Tradeoff in [X]." The reader notices by section 3.
**How to prevent it:** After scanning for word-level tells, do a separate pass for structural repetition. Search for repeated closing phrases, repeated section openers, and templated section structures. If a phrase appears as a section closer more than twice, flag it.
**Red flag:** You can predict the structure of section 4 by looking at section 2.

### Pitfall 6: Missing Generic Assessments
**What goes wrong:** You scan for banned vocabulary but miss vague qualitative judgments like "The platform's strength is breadth" or "Its analytics depth is moderate rather than deep." These are slop because they could apply to any tool.
**How to prevent it:** Search for assessment patterns: "strength is" + abstract noun, "depth is" + adjective, "analytics are" + adjective. Replace with specific observations about what the tool can and cannot do.
**Red flag:** Your assessment of a tool could be copy-pasted onto a different tool and still make sense.

### Pitfall 7: Not Running the Cadence Check
**What goes wrong:** You scan for vocabulary and patterns but do not check sentence length variation. The draft has uniform 18-24 word sentences throughout, which is the strongest current AI tell.
**How to prevent it:** Run the cadence check. Flag any run of 3+ consecutive sentences within 4 words of the same length. Vary deliberately: follow a long sentence with a short one. Fragments are legal.
**Red flag:** Every sentence in a paragraph is roughly the same length.


### Pitfall 8: Compliant But Flat (Missing Engagement)
**What goes wrong:** The draft passes every slop pattern check. No banned phrases. No negation patterns. No puffery. Correct structure. Verified claims. But it is boring. It reads like a compliant template with no human voice. No named frameworks. No specific thresholds. No blunt opinions. No surprising observations.
**Why it happens:** The model focuses so hard on avoiding banned patterns that it produces safe, flat, lifeless prose. Compliance without engagement is its own form of slop.
**How to prevent it:** After running the mechanical slop scan, run a separate engagement check. Ask: Does the draft use named frameworks? Does it use specific numbers and thresholds? Are skip recommendations blunt? Does the opening say something surprising? Is one narrative threaded through the whole piece? Does the closing line stick? Are tradeoffs stated as practical implications? Do tool sections use varied structure? If the answer to most of these is no, flag as "compliant but flat" and recommend engagement rewrites.
**Red flag:** The draft passes all slop checks but you would not actually want to read it.

### Pitfall 9: Subjective Assessment Instead of Literal Pattern Matching
**What goes wrong:** You assess whether the opening "feels" confrontational instead of searching for literal banned phrases. You say "this doesn't seem confrontational" when the text literally contains "Most guides to..." This is a reasoning failure, not a detection failure.
**Why it happens:** Subjective assessment is faster than mechanical scanning. But it is unreliable. The same priors that produce slop make it invisible to subjective review.
**How to prevent it:** For banned opening patterns, search for literal phrases: "Most guides", "Every listicle", "If you search for", "Most resources on", "Most articles", "If you look at". If any appear, flag as Critical. This is a pattern match, not a judgment call. Do not assess whether it "feels" confrontational. Search for the literal strings.
**Red flag:** You are about to say "this opening is fine" and you have not searched for the literal banned phrases.

## Why this is a loop, not a style guide

The worst tells — above all the **"not X but Y"** family — are not vocabulary mistakes. They are emergent properties of how LLMs generate text: preference tuning rewards balanced, contrastive, comprehensive-sounding framing, so the contrast move is baked into the model's priors. Two consequences drive this skill's architecture:

1. **You cannot reliably see your own slop.** The same priors that produce the pattern make it invisible on re-read. Detection must be mechanical — regex against a fixed catalog — never "does this look AI to me?"
2. **Rewriting reintroduces slop.** Ask a model to remove "it's not just X, it's Y" and it produces "this is less about X than Y" — the same move in a wig. So every rewrite gets re-scanned, and the loop runs until the scan is clean.

Workflow: **Scan → Diagnose → Rewrite by meaning → Re-scan → (repeat) → Register check.**

## Phase 0: Fix the target

Before touching the text, establish:

- **Genre and venue** — academic article, tweet, reddit post, LinkedIn, email, blog, docs, marketing. If not stated and not obvious from the text, ask. Genre decides which tells are fatal and what "good" means; see [references/voices.md](references/voices.md).
- **Audience and stance** — who reads it, and what the author actually claims. Slop is what fills the space where a claim should be; you cannot remove it without knowing the claim.
- **Constraints** — length limits, required citations, house style.

## Phase 1: Mechanical scan

Run the detection patterns from [references/tells.md](references/tells.md) against the text. If the text is in a file (or you can write it to a temp file), run the grep commands in that reference literally — the catalog is written as runnable `grep -Ein` patterns. Otherwise apply each pattern by hand, line by line.

Produce a finding list: line/sentence, matched pattern, tell category. Also run the two structural checks that regex can't fully catch:

- **Cadence**: flag any run of 3+ consecutive sentences within ±4 words of the same length, and any paragraph where every sentence has the same shape (subject–verb–elaboration).
- **Formatting**: bold scattered through prose, emoji-decorated headers or bullets, "**Term:** definition" bullet lists, headers on a text too short to need them, a tidy intro–three-points–conclusion skeleton.

Report the findings to the user as a short table before rewriting (category, count, worst example). This is the diagnosis; the user should see what was wrong.


## Phase 1.5: Engagement Quality Check

After the mechanical slop scan (Phase 1) and before rewriting (Phase 2), run a separate engagement check. A draft that passes all slop checks but is boring is still a failed draft.

Check for the following engagement techniques. At least 3 should be present across the draft:

1. **Named frameworks:** Does the draft name its patterns? (e.g., "Death by launch-and-leave" not "Common failure pattern #1")
2. **Specific numbers and thresholds:** Does it use actionable thresholds? (e.g., "adoption drops when it takes more than 15 seconds" not "ease of use matters")
3. **Blunt skip recommendations:** Are skip recommendations direct? (e.g., "Everyone else should skip it" not "this tool may not be suitable for smaller teams")
4. **Surprising opening:** Does the opening say something unexpected? (Not "there are many platforms on the market")
5. **Narrative threading:** Is one thread connected through the whole piece? (Not disconnected sections)
6. **Sticky closing:** Does the closing line stick? (Not "Choose the right platform for your needs")
7. **Tradeoffs as implications:** Are features translated into buyer implications? (e.g., "The $3,000 minimum means this is for companies with 60+ users" not "has a $3,000 minimum")
8. **Varied tool structure:** Do tool sections use different structures? (Not identical subsection headers for every tool)

If the draft passes all slop checks but has fewer than 3 engagement techniques, flag as Critical: "Draft is compliant but fails engagement. Rewrite flat sections using engagement techniques. A boring draft that passes all checks is still a failed draft."

Add engagement findings to the finding list from Phase 1. These get addressed in Phase 2 (rewrite by meaning).

## Phase 2: Rewrite by meaning, not by frame

Go finding by finding. The cardinal rule: **never fix a pattern by paraphrasing the pattern.** Fix it by deciding what the sentence actually asserts, then asserting that.

### The "not X but Y" family — three-way triage

Every negative parallelism gets exactly one of these treatments:

1. **The negation is a strawman** (nobody believes X). Delete the X half entirely and assert Y directly, with whatever evidence the text has.
 - *"It's not just a tool, it's a fundamental shift in how teams work"* → *"Teams that adopted it stopped holding standups within a month."*
2. **The contrast is real** (people genuinely hold X). Then earn it: name who holds X, say concretely why Y beats it. A real contrast survives being made specific; slop doesn't.
3. **The sentence asserts nothing** (the contrast is decoration on an empty claim). Delete the whole sentence. Most cases are this one.

Banned escape hatches — these are the same move and count as new findings: "less about X than Y", "X matters, but Y matters more", "the real X is Y", "the question isn't X, it's Y", "X? Y." (rhetorical-question variant), and the em-dash variant "— not X, but Y".

### Everything else

- **Puffery and inflated vocabulary** (pivotal, seismic, testament, tapestry, landscape, delve…): replace with the plain word, or with the concrete fact the puffery was hiding. "Plays a vital role in" → "does".
- **Rule-of-three lists**: keep the strongest item, cut the rest — unless all three carry distinct information, in which case keep them and break the rhythm (different lengths, different syntax).
- **False ranges** ("from X to Y"): if you can't name a meaningful midpoint between X and Y, it's not a range — name the two things or cut one.
- **Hedged both-sidesing** ("it's worth noting", auto-counterpoints, "while X, it's also true that Y"): commit. One opinion, stated, owned. A counterpoint stays only if the author genuinely concedes it.
- **Uniform cadence**: vary deliberately. Follow a long sentence with a short one. Fragments are legal. Don't apply a formula (alternating long/short is its own tell) — read the paragraph aloud and break wherever the rhythm is metronomic.
- **Low specificity**: replace "many companies" / "studies show" / "recent research" with the actual names, numbers, and dates — **only from the source text, the conversation, or verifiable research you actually do**. Never invent specifics. If the author needs to supply one, leave a marked placeholder: `[ADD: which study?]`.
- **Stock skeleton**: kill throat-clearing openers ("In today's fast-paced world…"), summary conclusions ("In conclusion… Ultimately…"), and engagement-bait endings ("What do you think?"). Start where the point starts; stop when it's made.

### What not to do — overcorrection is also slop

- No fake typos, forced slang, or manufactured "voice". Humanizer-tool output is its own genre of slop.
- Em dashes are not banned. Humans use them. The tell is density and the double-dash "— not X, but —" move. Budget: at most one em dash per ~150 words, never two in a sentence.
- Don't trade precision for personality in academic or technical text. There, de-slopping means cutting puffery and committing to claims — not adding attitude.
- Preserve the author's meaning, claims, and facts exactly. This is a style pass, not a content edit. Flag, don't silently fix, anything that looks factually wrong.

## Phase 3: Verify loop

Re-run the full Phase 1 scan **on your rewritten text**. This step is not optional and not a formality — expect your own rewrite to contain new tells, because the model writing it has the same priors that created them. Fix and re-scan until a pass produces zero pattern hits and the cadence check passes. Cap at 4 passes; if a pattern survives 4 passes, rewrite that sentence from scratch starting from its bare claim ("what fact or opinion is this sentence for?").

## Phase 4: Register check

Check the clean text against its genre profile in [references/voices.md](references/voices.md): right length, right formality, right person, genre-specific tells gone (e.g. on reddit: no bold, no bullet essay; in academic prose: no first-person hot takes added). Then the final test — read it aloud. Anywhere you wouldn't say it to the actual audience, rewrite that sentence.

Deliver: the rewritten text, plus a brief change log (categories fixed, counts, and number of verify passes it took).

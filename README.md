Documentation maintained alongside skill versions. Update this file whenever SKILL.md is changed.
seo-blog-writer — Technical Documentation
Skill ID: seo-blog-writer 
Current Version: 2.0.0 
Status: Stable 
Maintained by: Mahesh / Claude skill-creator session 
Compatible with: Claude skill framework v1.x ; Opencraft AI Response Styles
Skill 

Table of Contents
Overview
Architecture
Input Specification
Output Specification
Pipeline Integration
Processing Steps
Constraint Subsystems
Known Limitations
Changelog
Skill.md 

Overview
seo-blog-writer is a prompt skill that generates complete, SEO-optimised B2B SaaS blog posts alongside their meta assets (title tag, meta description, slug). It is designed for content that ranks in search and reads like it was written by a practitioner — not assembled by an AI.
The skill operates on a 5-step pipeline: input classification, awareness stage detection, structure planning, content generation with inline constraint enforcement, and a pre-delivery self-audit.
It integrates natively with competitor-page-assessor as an optional upstream input.

Architecture
INPUT
  └─ Step 0: Input Classifier
        └─ Step 1: Awareness Stage Detector (Schwartz 1-5)
              └─ Step 2: Structure Planner
                    └─ Step 3: Content Generator
                          ├─ Voice & Tone Module
                          ├─ Claim Integrity Rules (v2.0 addition)
                          └─ Blacklist Enforcer
                    └─ Step 3.5: Self-Audit Gate (v2.0 addition)
                          ├─ Claim Audit
                          ├─ Specificity Audit
                          └─ Voice Audit
OUTPUT
  └─ Step 4: Output Formatter
        ├─ SEO Meta Block (title tag, meta description, slug)
        └─ Blog Post (Markdown, H2/H3)

Input Specification
The skill accepts four input modes. These are not mutually exclusive — a full brief that also includes competitor-page-assessor output is valid.
Mode
Required fields
Optional fields
keyword-only
target keyword
none
topic+audience
topic, audience description
tone hints, geography
full-brief
topic, audience, awareness stage, CTA, product/company context
competitor data
pipeline
competitor-page-assessor output
full brief fields

Keyword-only behaviour: When only a keyword is provided, the skill surfaces its assumptions before writing. Format:
Assuming audience is [X], awareness stage is [Y], and intent is [Z].
Let me know if I should adjust any of these before I proceed.
The user can correct assumptions and the skill restarts from Step 1 with the corrected context.

Output Specification
All output is delivered in a fixed order:
SEO Meta Block
Field
Format
Constraints
Title tag
Plain string
60–65 characters. Includes primary keyword. Written for clicks, not just ranking.
Meta description
Plain string
150–160 characters. Summarises value. Includes keyword naturally. Gives a reason to click.
Slug
kebab-case string
Keyword-first. No filler words (no the, a, how-to-use-a).

Blog Post
Property
Value
Format
Markdown
Heading levels used
H2, H3 only. No H1 (title tag handles that).
Target length
1,500–2,500 words. Can exceed if topic demands it. Should not fall below without explicit justification.
CTA placement
End of post, as a natural continuation of the argument — not a bolted-on section.


Pipeline Integration
Upstream: competitor-page-assessor
When competitor-page-assessor output is passed as input, the blog writer treats the gap analysis and "How to Beat This Page" section as content strategy directives.
Specifically:
Identified content gaps become required coverage areas in the post structure
Competitor weaknesses (Clarity/Depth/Usefulness/Presentation) inform where to go deeper
Questions competitors failed to answer are answered fully, not touched on
The post is considered complete only when every flagged gap is closed — not mentioned, closed
What "closed" means: A gap is closed when the post answers the underlying question fully enough that a reader would not need to visit the competitor page. Nodding at a gap does not close it.
Future upstream candidates
The skill is designed to accept output from any structured content brief tool. As long as the upstream output includes a target query, audience description, and content gaps or recommendations, it can be passed in under the pipeline input mode.

Processing Steps
Step 0 — Input Classifier
Reads the input and categorises it into one of the four input modes. If the input is ambiguous (e.g. a topic with some but not all brief fields), the skill defaults to the richest mode the data supports and states its assumptions.
Step 1 — Awareness Stage Detector
Maps the reader onto Schwartz's five-stage awareness ladder using signals from the keyword, topic framing, and any audience context provided.
Stage
Signal patterns
Unaware
No category awareness in keyword. Broad lifestyle or outcome-focused query.
Problem-aware
Keywords name the pain, not the solution. "Why is X slow", "X keeps failing".
Solution-aware
Keywords reference solution types. "Best X tool", "X software comparison".
Product-aware
Brand or product name in keyword or brief. Objection-framed questions.
Most aware
Pricing, trial, sign-up intent signals.

Default: Problem-aware, if no strong signal exists.
The awareness stage governs: headline framing, intro hook style, problem section depth, solution introduction timing, how much product specificity is appropriate, and CTA directness.
Step 2 — Structure Planner
Maps the post structure before writing prose. Does not default to a listicle skeleton. Structure reflects:
Awareness stage
Search intent (informational / commercial / transactional / navigational)
The logical flow of information that serves this specific reader
Structural requirements:
Intro must name the reader's tension within the first 2–3 sentences. No warmup.
Subheads must form a coherent logical sequence when read in isolation (the "subhead scan test").
Each section covers one idea thoroughly rather than three ideas shallowly.
CTA follows from the post's argument as a next step, not a separate conversion event.
Step 3 — Content Generator
Writes the post with three active subsystems running in parallel. See Constraint Subsystems below.
Step 3.5 — Self-Audit Gate
A mandatory internal checklist run before producing the final output. Not skippable. Three audit passes:
Claim Audit
Every stat is sourced or replaced with a qualitative pattern description
Every strong performance claim is followed by its mechanism
No unverified stat has been compounded into a calculation
Specificity Audit
Every problem statement passes the competitor test (see Constraint Subsystems)
Every product-specific term is defined on first use
Integration claims name specific platforms
No audience-excluding conditional framing
Voice Audit
No sentence reads like it could have been written by a category
FAQ answers are one clear answer per question, not a paragraph per sentence
Subheads form a logical sequence top to bottom
Step 4 — Output Formatter
Assembles the final output in the fixed format: SEO meta block followed by the blog post. No additional commentary, caveats, or preamble unless the user asked for keyword-only mode, in which case the assumption statement precedes the output.

Constraint Subsystems
1. Claim Integrity Rules
Added in v2.0. The most significant change from v1.0.
On statistics:
No stat may be used without a traceable, named source
When a source is unavailable, the observable pattern is described qualitatively instead
Unverified stats may not be compounded into calculations
Stats that vary by industry, role level, or company size must acknowledge that variance
On strong performance claims:
Any claim of faster/better/cheaper than the alternative must be immediately followed by the mechanism that produces it
"Cut screening time by 80%" is not a valid sentence without the next sentence explaining what the product does that creates that reduction
If the mechanism cannot be explained, the claim is softened or removed
On product-specific terminology:
Every technical product term is defined plainly on its first use
Undefined jargon used as a selling point erodes trust faster than no claim at all
Integration claims name specific platforms — "your existing workflow" is not a valid integration claim
On problem framing:
The Competitor Test: every problem statement must be rewritten if it could appear on a rival's page without changing a word
Category-level truisms ("quality drops as volume increases") are not insights and are replaced with specific mechanisms or consequences
Audience-excluding conditionals ("if you're hiring for 500 roles") are reframed in terms of the underlying experience
2. Blacklist Enforcer
A list of phrase categories that are prohibited in all output. Covers:
Category
Examples
"It's not X, it's Y" clichés
"It's not just about...", "The real reason isn't X..."
False pattern interrupts
"Here's the kicker", "Here's the thing"
Artificial urgency
"In today's world", "Now more than ever"
Credibility theater
"Let's be honest", "Full transparency"
Engagement bait
"Think about it", "Picture this"
Faux authority
"Studies show", "Experts agree"
Transition stuffing
"That said", "With that in mind"
False intimacy
"Sound familiar?", "We've all been there"
Manufactured insight
"What most people don't realize"
Weak intensifiers
"Really", "Very", "Basically"
Empty conjunctions
"Moreover", "Furthermore"
Vague gesturing
"And so much more", "The list goes on"
Pain-point theater
"Struggling with", "Frustrated by"
False simplicity
"Simply put", "Put simply"
Journey clichés
"Transform your", "Game-changer", "Dive deep into"
Formatting
Em dashes, invented figures, unattributed stats

3. Voice and Tone Module
Persona: experienced direct response B2B SaaS copywriter. Expert, approachable, warm, conversational. Not jargon-heavy. Not attacking.
Positioning: Socratic. The skill sits on the same side of the table as the reader and looks at the problem together. Never adversarial. Never frames the reader's current process as stupid.
Sentence rhythm: mix of short punchy sentences and longer ones that carry weight. No paragraph walls. Metaphors and analogies grounded in the reader's industry, workflow, and geography when known.

Known Limitations
No real-time data access. The skill cannot source statistics at write time. When operating without a full brief that includes verified figures, it will describe patterns qualitatively. If the user provides a sourced stat, the skill will use it. If they provide an unsourced one, it will flag this and suggest a qualitative reframe.
Product-specific terms require user input. The skill will define technical terms on first use, but it can only define what it knows. If the product has proprietary terminology that is not in the brief, the definitions will be generic. The more specific the brief, the more accurate the definitions.
Awareness stage detection is inferential. With only a keyword and no brief, stage detection relies on keyword pattern matching. This is usually accurate for common B2B SaaS keyword types but can misfire on ambiguous or broad topics. The assumption declaration at Step 0 is the safety mechanism for this.
Word count is a target, not a guarantee. The 1,500–2,500 word target is an instruction, not a hard constraint. Very narrow topics may produce shorter output. Very complex topics may run longer. The guiding principle is reader satisfaction, not word count.

Changelog

v2.0.0 — Claim Integrity and Specificity Update
Type: Breaking improvement (output quality) Trigger: Post-audit review of a use-case page draft that surfaced three systematic failure modes
What changed
Added: Claim Integrity Rules subsystem (Step 3)
A dedicated rules block covering four claim types: statistics, strong performance claims, product-specific terminology, and problem framing. This subsystem replaces the single-line "no invented numbers" instruction that existed in v1.0's Blacklist section.
The v1.0 instruction was a prohibition without a replacement behaviour. The model had no guidance on what to do when it wanted to use a figure but could not source it, resulting in unattributed floating statistics. The v2.0 subsystem provides explicit fallback behaviour: describe the observable pattern qualitatively.
Key rules introduced:
No stat without a named, traceable source
Every strong performance claim must be followed by its mechanism
Every product-specific term defined on first use
Specific integration platforms named, not "your existing workflow"
The Competitor Test for problem framing (can this sentence appear on a rival's page unchanged? if yes, rewrite)
No audience-excluding conditional framing in headlines or subheads
Added: Step 3.5 — Self-Audit Gate
A mandatory pre-delivery checklist with three passes: Claim Audit, Specificity Audit, Voice Audit. Catches issues that the inline rules miss at the sentence level, particularly FAQ length (answered at the structural level), subhead coherence (caught at the sequence level), and audience-excluding framing (caught at the document level).
Modified: Blacklist — Formatting section
The "no invented numbers or fake case study figures" line was deprecated and replaced with a pointer to the Claim Integrity Rules. The intent is the same; the behaviour is now governed by a richer subsystem rather than a single prohibition.
Modified: Step 3 — What to Do
Minor wording tightened. "What the actual friction feels like" now reads "what the actual friction feels like in their day." No functional change.
What did not change
Input specification (all four modes preserved)
Awareness stage table
Output format specification
The Blacklist (all categories preserved, no additions)
Principles section
Pipeline integration with competitor-page-assessor
Root cause analysis
Three failure modes were identified from the audit:
Unanchored statistics. The model used plausible-sounding industry figures without sources because the skill permitted them as long as they were "real." Without a source requirement, "real" was unenforced. The model also compounded unverified stats into calculations, which multiplied the credibility problem.


Claims without mechanisms. Strong performance claims were asserted but never explained. The model had no instruction to follow a claim with its mechanism. A skeptical reader's first question after "cut screening time by 80%" is "how?" — the skill gave no guidance that this question must be answered in the same breath.


Category-level copy. Problem headlines described truisms shared across every competitor in the category. The skill's "specificity" guidance was too abstract — it said to be specific but did not define what fails the specificity test. The Competitor Test operationalises this: if the sentence could appear on a rival's page unchanged, it is not specific enough.



v1.0.0 — Initial Release
Type: New skill
What was built
Full B2B SaaS blog writing skill built around a direct response copywriting persona. Features:
Four input modes (keyword-only, topic+audience, full brief, pipeline)
Schwartz awareness stage detection and calibration
Structure planning step (non-listicle by default)
Voice and tone module with Socratic positioning
Full blacklist covering 16 phrase categories
Fixed output format: SEO meta block + Markdown blog post
Native pipeline integration with competitor-page-assessor
Word count target: 1,500–2,500 words
Design decisions:
Awareness stage defaults to Problem-aware, the most common stage for B2B SaaS SEO content
Keyword-only mode surfaces assumptions before writing rather than guessing silently
The CTA is treated as part of the content, not a separate conversion event bolted on at the end
The Blacklist was populated from an existing master phrase blacklist maintained separately




#!/usr/bin/env python3
"""
human-write-review.py — AI tell detector
Scans text for ~14 categories of AI writing patterns.
Usage: python3 human-write-review.py [file] | pbpaste | python3 human-write-review.py
Options: --json, --severity N
"""

import re
import sys
from collections import defaultdict

# ── 1. VOCABULARY BLACKLIST ──
blacklist = {
    "delve": ("delve / delves into", 1, "Replace with 'examine', 'explore', or 'covers'"),
    "delve into": ("delve / delves into", 1, "Replace with 'examine', 'explore', or 'covers'"),
    "delves into": ("delve / delves into", 1, "Replace with 'examine', 'explore', or 'covers'"),
    "tapestry": ("tapestry", 1, "Concrete description instead"),
    "underscore": ("underscore / underscores", 2, "Replace with 'shows' or 'highlights'"),
    "underscores": ("underscore / underscores", 2, "Replace with 'shows' or 'highlights'"),
    "pivotal": ("pivotal", 1, "Replace with 'key' or 'important' or specific fact"),
    "showcase": ("showcase / showcases", 2, "Replace with 'shows' or 'demonstrates'"),
    "showcases": ("showcase / showcases", 2, "Replace with 'shows' or 'demonstrates'"),
    "intricate": ("intricate / intricacies", 2, "Use specific description instead"),
    "intricacies": ("intricate / intricacies", 2, "Use specific description instead"),
    "foster": ("foster / fosters", 2, "Replace with 'encourage' or 'build'"),
    "fosters": ("foster / fosters", 2, "Replace with 'encourage' or 'build'"),
    "garner": ("garner / garners", 1, "Replace with 'get', 'receive', or 'attract'"),
    "garners": ("garner / garners", 1, "Replace with 'get', 'receive', or 'attract'"),
    "testament": ("testament", 2, "Replace with 'shows' or 'reflects'"),
    "stands as a testament": ("testament", 3, "Remove entirely. 'Is' works. Specific fact works better."),
    "enhance": ("enhance / enhances", 2, "Replace with 'improve' or specific action"),
    "enhances": ("enhance / enhances", 2, "Replace with 'improve' or specific action"),
    "crucial": ("crucial", 2, "Replace with specific importance or remove"),
    "landscape": ("landscape (metaphorical)", 2, "If metaphorical (e.g., 'tech landscape'), replace with 'field' or 'industry'"),
    "realm": ("realm", 2, "Replace with 'field' or 'area'"),
    "encompass": ("encompass / encompasses", 2, "Replace with 'include' or 'cover'"),
    "encompasses": ("encompass / encompasses", 2, "Replace with 'include' or 'cover'"),
    "multifaceted": ("multifaceted", 1, "Use specific aspects instead"),
    "holistic": ("holistic", 2, "Unless medicine/wellness context, replace with 'complete' or 'comprehensive'"),
    "leverage": ("leverage (metaphorical)", 2, "If not about actual levers, replace with 'use'"),
    "synergy": ("synergy / synergies", 1, "Replace with specific joint effect"),
    "synergies": ("synergy / synergies", 1, "Replace with specific joint effect"),
    "robust": ("robust", 2, "Replace with specific quality (stable, reliable, tested)"),
    "cutting-edge": ("cutting-edge", 1, "Replace with specific technology or feature"),
    "revolutionary": ("revolutionary", 1, "Remove or replace with specific change"),
    "groundbreaking": ("groundbreaking", 1, "Remove or replace with specific innovation"),
    "transformative": ("transformative", 1, "Remove or replace with specific effect"),
    "seamless": ("seamless / seamlessly", 2, "Replace with 'smooth' or specific description"),
    "seamlessly": ("seamless / seamlessly", 2, "Replace with 'smoothly' or remove"),
    "streamline": ("streamline / streamlines", 2, "Replace with 'simplify' or specific action"),
    "streamlines": ("streamline / streamlines", 2, "Replace with 'simplify' or specific action"),
    "empower": ("empower / empowers", 2, "Replace with 'enable' or 'help'"),
    "empowers": ("empower / empowers", 2, "Replace with 'enable' or 'help'"),
}

# ── 2. PUFFERY ──
puffery_phrases = [
    (r"plays\s+a\s+vital\s+role", "plays a vital role", 2, "Remove. State what it actually does."),
    (r"serves\s+as\s+a\s+testament", "serves as a testament", 3, "Remove. 'Is' or specific fact."),
    (r"leaves?\s+a\s+lasting\s+impact", "leaves a lasting impact", 2, "Remove. State the actual effect."),
    (r"watershed\s+moment", "watershed moment", 2, "Remove. Describe what happened."),
    (r"lasting\s+legacy", "lasting legacy", 2, "Remove or replace with specific legacy."),
    (r"rich\s+cultural\s+heritage", "rich cultural heritage", 2, "Replace with specific cultural elements."),
    (r"breathtaking\s+(natural\s+)?beauty", "breathtaking beauty", 2, "Replace with specific geographic description."),
    (r"vibrant\s+(community|traditions?|culture)", "vibrant community/traditions/culture", 2, "Replace with specific details."),
    (r"a\s+mosaic\s+of\s+diverse", "a mosaic of diverse", 2, "Remove. Use concrete description."),
    (r"a\s+melting\s+pot\s+of", "a melting pot of", 2, "Remove. Use concrete description."),
    (r"stunning\s+vistas?", "stunning vista", 2, "Replace with actual geographic terms."),
    (r"a\s+jewel\s+of\s+(the\s+)?", "a jewel of the...", 2, "Remove."),
    (r"cutting-edge\s+solutions?", "cutting-edge solutions", 1, "Replace with specific capability."),
    (r"industry-leading", "industry-leading", 1, "Remove or replace with specific metric."),
    (r"commitment\s+to\s+excellence", "commitment to excellence", 1, "Remove."),
    (r"passion\s+for\s+(innovation|excellence|quality)", "passion for innovation/excellence", 1, "Remove."),
]

# ── 3. NEGATIVE PARALLELISMS ──
neg_parallel = [
    (r"[Ii]t'?s?\s+not\s+(?:just\s+)?(?:about\s+)?(\w[^.,;!?]+)[,;]?\s*(?:it'?s?|but)\s+", "It's not X, it's Y / but", 3, "Remove or rewrite as direct statement."),
    (r"[Nn]ot\s+just\s+a\w*\s+(\w+),?\s+but\s+(?:a\w*\s+)?", "Not just X, but Y", 3, "Remove or rewrite as direct statement."),
    (r"[Nn]ot\s+only\s+(\w[^,]+),\s+but\s+also", "Not only X, but also Y", 2, "Use unless the contrast is genuinely surprising."),
]

# ── 4. COPULATIVES ──
copulatives = [
    (r"serves?\s+as\s+(?:a\s+)?", "serves as", 2, "Replace with 'is'"),
    (r"stands?\s+as\s+(?:a\s+)?", "stands as", 2, "Replace with 'is'"),
    (r"features?\s+a\s+wide\s+range\s+of", "features a wide range of", 2, "Replace with 'has'"),
    (r"offers?\s+(?:a\s+)?unique\s+blend\s+of", "offers a unique blend of", 2, "Replace with 'combines'"),
    (r"represents?\s+a\s+significant\s+milestone", "represents a significant milestone", 2, "Replace with 'is a milestone'"),
    (r"serves?\s+as\s+a\s+powerful\s+reminder", "serves as a powerful reminder", 2, "Replace with 'is a reminder'"),
]

# ── 5. WEASEL WORDS ──
weasel = [
    (r"(?:[Ii]ndustry\s+)?[Ee]xperts?\s+sa(?:y|id)", "Experts say", 3, "Name the expert or remove."),
    (r"[Ss]ome\s+critics?\s+argue", "Some critics argue", 3, "Name the critic or remove."),
    (r"[Oo]bservers?\s+have\s+noted", "Observers have noted", 3, "Name the observer or remove."),
    (r"[Aa]nalysts?\s+suggest", "Analysts suggest", 3, "Name the analyst or remove."),
    (r"[Mm]any\s+believe\s+that", "Many believe that", 3, "Source it or remove."),
    (r"[Ii]t\s+is\s+widely\s+accepted\s+that", "It is widely accepted that", 3, "Source it or remove."),
    (r"[Ii]t\s+is\s+generally\s+believed", "It is generally believed", 3, "Source it or remove."),
]

# ── 6. TRANSITIONS ──
transitions = [
    (r"^[Mm]oreover,?", "Moreover", 1, ""),
    (r"^[Ff]urthermore,?", "Furthermore", 1, ""),
    (r"^[Aa]dditionally,?", "Additionally", 1, ""),
    (r"^[Ii]n\s+addition,?", "In addition", 1, ""),
    (r"^[Oo]n\s+the\s+other\s+hand,?", "On the other hand", 1, ""),
    (r"^[Nn]evertheless,?", "Nevertheless", 1, ""),
]

# ── 7. SECTION SUMMARIES ──
section_summaries = [
    (r"^[Ii]n\s+summary,?", "In summary", 2, "Remove. Trust the reader."),
    (r"^[Ii]n\s+conclusion,?", "In conclusion", 2, "Remove. Trust the reader."),
    (r"^[Oo]verall,?", "Overall", 2, "Remove. Trust the reader."),
    (r"^[Tt]o\s+conclude", "To conclude", 2, "Remove. Trust the reader."),
]

# ── 8. EDITORIALIZING ──
editorial = [
    (r"[Ii]t'?s?\s+(?:important|worth|crucial|essential|critical)\s+to\s+note", "It's important/worth to note", 2, "Remove. State the fact."),
    (r"[Ii]t\s+(?:is\s+)?(?:important|worth|crucial|essential|critical)\s+to\s+note", "It is important/worth to note", 2, "Remove. State the fact."),
    (r"[Ii]t\s+(?:is\s+)?worth\s+remembering", "It is worth remembering", 2, "Remove. State the fact."),
    (r"[Nn]o\s+discussion\s+of\s+\w+\s+would\s+be\s+complete\s+without", "No discussion of X would be complete without", 2, "Remove."),
    (r"[Cc]rucially,?", "Crucially", 2, "Remove unless genuinely critical."),
    (r"[Ss]ignificantly,?", "Significantly", 2, "Remove unless genuinely significant."),
]

# ── 9. CHALLENGES & FUTURE FORMULA ──
challenges_future = [
    (r"[Dd]espite\s+(?:its|their)\s+\w+,\s*\w+\s+faces?\s+challenges?", "Despite its [positives], [subject] faces challenges", 3, "Rewrite. If challenges exist, state them specifically."),
    (r"[Cc]hallenges?\s+and\s+[Ff]uture\s+[Dd]irections?", "Challenges and Future Directions", 2, "Avoid this formulaic heading."),
    (r"[Tt]he\s+future\s+of\s+\w+\s+lies?\s+in\s+its?\s+ability\s+to", "The future of X lies in its ability to", 3, "Remove. Speculation without source."),
]

# ── 10. LEAKED CHAT PHRASES ──
leaked_chat = [
    (r"I\s+hope\s+this\s+(?:helps?|finds?\s+you\s+well)", "I hope this helps/finds you well", 2, "Remove. Published content is not correspondence."),
    (r"[Oo]f\s+course!?", "Of course!", 2, "Remove."),
    (r"[Cc]ertainly!?", "Certainly!", 2, "Remove."),
    (r"[Ll]et\s+me\s+know\s+if\s+(?:you\s+have|there'?s?)", "Let me know if you have...", 2, "Remove."),
    (r"[Ff]eel\s+free\s+to\s+(?:reach\s+out|ask)", "Feel free to reach out/ask", 2, "Remove."),
    (r"[Pp]lease?\s+do\s+not\s+hesitate\s+to", "Please do not hesitate to", 2, "Remove."),
    (r"[Ww]ould\s+you\s+like\s+me\s+to\s+expand", "Would you like me to expand", 2, "Remove."),
]

# ── 11. AI SELF-REFERENCES ──
ai_refs = [
    (r"As\s+(?:an\s+)?AI\s+(?:language\s+)?model", "As an AI language model", 3, "Never belongs in published content."),
    (r"As\s+of\s+my\s+last\s+(?:knowledge\s+)?update", "As of my last knowledge update", 3, "Never belongs in published content."),
    (r"I\s+(?:don'?t|do\s+not)\s+have\s+(?:access\s+to\s+)?real-?time\s+information", "I don't have access to real-time information", 3, "Never belongs in published content."),
    (r"I\s+(?:am\s+)?unable\s+to\s+(?:provide|access)", "I am unable to provide/access", 3, "Never belongs in published content."),
    (r"Please?\s+note\s+that\s+(?:I\s+do\s+not|this\s+information)", "Please note that I do not / this information", 2, "Remove."),
]

# ── 12. SOCIAL MEDIA PRESENCE ──
social_media = [
    (r"maintains?\s+(?:an\s+)?active\s+(?:social\s+media\s+)?presence", "maintains an active social media presence", 2, "Remove or cite specific social media activity."),
]

# ── 13. FALSE RANGES ──
false_ranges = [
    (r"[Ff]rom\s+\w[^,]+to\s+\w[^,.]+\b", "From X to Y (potential false range)", 1, "Check if there's a real continuum between X and Y."),
]

# ── 14. MARKUP ARTIFACTS ──
markup_artifacts = [
    (r"citeturn0\w+", "citeturn0... artifact", 3, "Definitive raw AI output artifact. Remove."),
    (r"oai_citation", "oai_citation artifact", 3, "Definitive raw AI output artifact. Remove."),
    (r":contentReference\[oaicite:", ":contentReference[oaicite:...", 3, "Definitive raw AI output artifact. Remove."),
    (r"\[(?:attached_file|web):\d+\]", "[attached_file:N] or [web:N] artifact", 3, "Raw AI output artifact. Remove."),
    (r"<grok_card>", "<grok_card> artifact", 3, "Grok raw output. Remove."),
    (r'{"attribution":', 'JSON attribution artifact', 3, "Raw AI output artifact. Remove."),
    (r"INSERT_SOURCE_URL|SOURCE_PUBLISHER", "Placeholder text", 3, "Unedited template. Fill or remove."),
    (r"\[Insert\s+\w+\s+example", "[Insert example here]", 3, "Unedited template. Fill or remove."),
    (r"\[Add\s+citation", "[Add citation]", 3, "Unedited template. Fill or remove."),
    (r"\d{4}-\w{2,3}-\d{2,4}\s*\(placeholder\)", "Placeholder date", 3, "Unedited template. Fill or remove."),
    (r"[Uu]tm_source=(?:openai|chatgpt|copilot)", "UTM parameter (AI fingerprint)", 3, "Remove tracking parameters."),
]


# ── HELPER: Em dash density ──
def check_em_dash_density(lines):
    results = []
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        dashes = len(re.findall(r"\u2014|--", line))
        if dashes >= 3:
            results.append({
                "category": "EM_DASH",
                "pattern": f"{dashes} em dashes in one line",
                "severity": 2,
                "line": i,
                "text": line.strip()[:120],
                "fix": "Replace some with commas, colons, or parentheses."
            })
    return results


# ── HELPER: Rule of Three ──
def check_rule_of_three(lines):
    results = []
    triplet = re.compile(r"(\w+),?\s+(\w+),?\s+(?:and\s+)?(\w+)\s+(?:and|or|\w)", re.I)
    ai_candidates = {"innovative","transformative","groundbreaking","revolutionary","seamless","robust",
                     "dynamic","strategic","scalable","comprehensive","efficient","effective",
                     "powerful","unique","holistic","integrated","optimized","flexible","agile"}
    for i, line in enumerate(lines, 1):
        for m in triplet.finditer(line):
            words = {m.group(1).lower().strip(","), m.group(2).lower().strip(","), m.group(3).lower().strip(",")}
            if words & ai_candidates:
                results.append({
                    "category": "RULE_OF_THREE",
                    "pattern": f"'{m.group(1)}, {m.group(2)}, and {m.group(3)}'",
                    "severity": 2,
                    "line": i,
                    "text": line.strip()[:120],
                    "fix": "Let content determine count, not a consistent triplet pattern."
                })
    return results


# ── HELPER: Inline-Header Vertical Lists ──
def check_inline_header_lists(text, lines):
    results = []
    if "*" not in text and "\u2022" not in text:
        return results
    inline_header = re.compile(r"^[\s*\u2022\-]*\*?([A-Z]\w+(?:\s+\w+){0,4})\*?:", re.M)
    for m in inline_header.finditer(text):
        pos = m.start()
        line_no = text[:pos].count("\n") + 1
        results.append({
            "category": "INLINE_HEADER_LIST",
            "pattern": f"Bolded-colon list: '{m.group(1)}:'",
            "severity": 1,
            "line": line_no,
            "text": lines[line_no-1].strip()[:120] if line_no-1 < len(lines) else "",
            "fix": "Consider prose instead of list format."
        })
    return results


# ── MAIN SCAN ──
def scan_text(text):
    lines = text.split("\n")
    findings = []

    # Word-level blacklist (with word boundaries)
    for i, line in enumerate(lines, 1):
        lower = line.lower()
        for word, (group, sev, fix) in blacklist.items():
            pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.I)
            if pattern.search(line):
                findings.append({
                    "category": "AI_VOCAB",
                    "pattern": group,
                    "severity": sev,
                    "line": i,
                    "text": line.strip()[:120],
                    "fix": fix
                })

    # Pattern-based checks
    checks = [
        (puffery_phrases, "PUFFERY"),
        (neg_parallel, "NEG_PARALLEL"),
        (copulatives, "COPULATIVE"),
        (weasel, "WEASEL"),
        (section_summaries, "SECTION_SUMMARY"),
        (editorial, "EDITORIAL"),
        (challenges_future, "CHALLENGES_FUTURE"),
        (leaked_chat, "LEAKED_CHAT"),
        (ai_refs, "AI_SELF_REF"),
        (social_media, "SOCIAL_MEDIA"),
        (false_ranges, "FALSE_RANGE"),
        (markup_artifacts, "MARKUP_ARTIFACT"),
    ]

    for patterns, cat in checks:
        for pattern, label, sev, fix in patterns:
            for m in pattern.finditer(text):
                pos = m.start()
                line_no = text[:pos].count("\n") + 1
                findings.append({
                    "category": cat,
                    "pattern": label,
                    "severity": sev,
                    "line": line_no,
                    "text": lines[line_no-1].strip()[:120] if line_no-1 < len(lines) else "",
                    "fix": fix
                })

    # Transition overuse (3+ in whole text is suspicious)
    current_transitions = []
    for i, line in enumerate(lines, 1):
        for pattern, label, sev, _ in transitions:
            if pattern.search(line):
                current_transitions.append((label, i, line.strip()[:80]))
    if len(current_transitions) >= 3:
        for label, line_no, snippet in current_transitions:
            findings.append({
                "category": "TRANSITION_OVERUSE",
                "pattern": f"Transition: {label}",
                "severity": 1,
                "line": line_no,
                "text": snippet,
                "fix": "Vary transitions or cut. Multiple in same document is a tell."
            })

    # Em dashes
    findings.extend(check_em_dash_density(lines))

    # Rule of three
    findings.extend(check_rule_of_three(lines))

    # Inline-header lists
    findings.extend(check_inline_header_lists(text, lines))

    # Deduplicate
    seen = set()
    unique = []
    for f in findings:
        key = (f["line"], f["category"], f["pattern"])
        if key not in seen:
            seen.add(key)
            unique.append(f)

    return unique


# ── REPORT FORMATTING ──
def format_report(findings):
    if not findings:
        return "✅ No AI tells detected. Text looks human-written."

    sev_counts = defaultdict(int)
    cat_counts = defaultdict(int)

    for f in findings:
        sev_counts[f["severity"]] += 1
        cat_counts[f["category"]] += 1

    severity_label = {1: "low", 2: "medium", 3: "high"}

    lines = []
    total = len(findings)
    high = sev_counts[3]
    med = sev_counts[2]
    low = sev_counts[1]

    lines.append(f"📊 SUMMARY: {total} violations ({high} high, {med} medium, {low} low)")
    lines.append("")

    for sev_level in [3, 2, 1]:
        subset = [f for f in findings if f["severity"] == sev_level]
        if not subset:
            continue
        lines.append(f"{'━' * 3} {severity_label[sev_level].upper()} {'━' * 30}")
        for f in subset:
            fix_text = f"  → Fix: {f['fix']}" if f['fix'] else ""
            lines.append(f"{f['line']}. [{f['category']}] Line {f['line']},  \"{f['pattern']}\" ({severity_label[sev_level]})")
            if f['text']:
                lines.append(f"   \"{f['text']}\"")
            lines.append(f"   {fix_text}")
            lines.append("")

    lines.append(f"{'━' * 3} BY CATEGORY {'━' * 30}")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        lines.append(f"  {cat}: {count}")

    return "\n".join(lines)


# ── CLI ──
def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 human-write-review.py [options] [file]")
        print("  Reads from file, or stdin if no file given.")
        print("  Options:")
        print("    --help      Show this help")
        print("    --json      Output JSON")
        print("    --severity N  Only show >= severity N (1-3)")
        return

    output_json = "--json" in sys.argv
    severity_filter = None
    if "--severity" in sys.argv:
        idx = sys.argv.index("--severity")
        if idx + 1 < len(sys.argv):
            try:
                severity_filter = int(sys.argv[idx + 1])
            except ValueError:
                pass

    text = None
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        try:
            with open(args[0], "r") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args[0]}' not found.")
            sys.exit(1)
    else:
        text = sys.stdin.read()

    if not text or not text.strip():
        print("No text provided.")
        return

    findings = scan_text(text)

    if severity_filter:
        findings = [f for f in findings if f["severity"] >= severity_filter]

    if output_json:
        import json
        print(json.dumps(findings, indent=2))
    else:
        print(format_report(findings))


if __name__ == "__main__":
    main()

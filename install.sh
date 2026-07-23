#!/usr/bin/env bash
set -euo pipefail

REPO="https://github.com/Mahesh-Revenueholic/internal-skills.git"
TARGET="${1:-$HOME/.ai-skills}"
TEMP=$(mktemp -d)

echo "→ Cloning internal-skills..."
git clone --depth 1 "$REPO" "$TEMP" 2>/dev/null

echo "→ Installing skills to $TARGET..."
mkdir -p "$TARGET"

installed=0
for f in "$TEMP"/*.md "$TEMP"/*.py; do
  [ -f "$f" ] || continue
  cp "$f" "$TARGET/"
  echo "  ✓ $(basename "$f")"
  installed=$((installed + 1))
done

rm -rf "$TEMP"

echo ""
echo "✓ Installed $installed files to $TARGET"
echo ""
echo "Next: paste this in your AI tool:"
echo "  Load skills from $TARGET and run the SEO blog pipeline."

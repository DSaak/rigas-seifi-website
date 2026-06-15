#!/bin/zsh
# Double-click this file to publish the website:
#   rebuild -> save a version snapshot -> commit -> push to GitHub.
# GitHub Pages then updates the live site in about a minute.
#
# (Double-clicking opens Terminal in your home folder, so we cd to the
#  project by absolute path first. set -e aborts before pushing if the
#  build fails, so a broken site never goes live.)
set -e
cd "/Users/ds/Claude/Rigas Seifi Website"

echo "==> Building site..."
/usr/bin/python3 build.py

echo "==> Saving version snapshot..."
sh snapshot.sh "publish" >/dev/null

echo "==> Committing & pushing..."
git add -A
if git diff --cached --quiet; then
  echo "    No changes to publish."
else
  git commit -m "Publish $(date '+%Y-%m-%d %H:%M')"
  git push
  echo ""
  echo "Done. Live in ~1 min:  https://dsaak.github.io/rigas-seifi-website/"
fi

echo ""
echo "You can close this window."

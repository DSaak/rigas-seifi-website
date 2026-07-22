#!/bin/sh
# Snapshot the current website source into the versions folder and keep
# only the 15 most recent versions.
#   Usage: sh snapshot.sh "short_label"
set -e
SRC="/Users/ds/Claude/Rigas Seifi Website"
VROOT="/Users/ds/Claude/Rigas Seifi Website/versions"
LABEL="${1:-update}"
mkdir -p "$VROOT"

# next version number (highest existing vNN + 1)
LAST=$(ls -1 "$VROOT" 2>/dev/null | sed -n 's/^v\([0-9]\{1,\}\).*/\1/p' | sort -n | tail -1)
NEXT=$(printf "%02d" $(( ${LAST:-0} + 1 )))
STAMP=$(date +%Y%m%d-%H%M)
DEST="$VROOT/v${NEXT}_${LABEL}_${STAMP}"

mkdir -p "$DEST"
( cd "$SRC" && rsync -a --exclude docs --exclude versions --exclude __pycache__ --exclude '.DS_Store' ./ "$DEST/" )

# keep only the 15 newest snapshots
( cd "$VROOT" && ls -1dt */ 2>/dev/null | tail -n +16 | while read d; do rm -rf "$d"; done )

echo "Saved $DEST"
echo "Current versions:"
ls -1 "$VROOT"

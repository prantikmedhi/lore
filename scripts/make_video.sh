#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: scripts/make_video.sh slides.pdf audio.m4a output.mp4" >&2
  exit 1
fi

SLIDES_PDF="$1"
AUDIO="$2"
OUTPUT="$3"
WORKDIR="$(mktemp -d)"

pdftoppm -png -r 180 "$SLIDES_PDF" "$WORKDIR/slide"
ffmpeg -y -framerate 1/8 -pattern_type glob -i "$WORKDIR/*.png" -i "$AUDIO" -c:v libx264 -c:a aac -pix_fmt yuv420p -shortest "$OUTPUT"

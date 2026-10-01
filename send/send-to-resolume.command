#!/bin/bash
# Code Painter by JAS.BLACK — sender (macOS): offers the painting to Resolume (or any VJ app) as a Syphon source called
# "Code Painter". Double-click it, then switch on "send" in the studio's out panel. Close this window to stop.
# The first time it sets itself up (a minute): it needs Python 3.9–3.12 (the one macOS offers to install is fine).
cd "$(dirname "$0")" || exit 1

pick() {
  for c in python3.12 python3.11 python3.10 python3.9 \
           /opt/homebrew/bin/python3.12 /opt/homebrew/bin/python3.11 /usr/local/bin/python3.12 /usr/local/bin/python3.11 \
           /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 \
           /usr/bin/python3 python3; do
    if command -v "$c" >/dev/null 2>&1; then
      v=$("$c" -c 'import sys; print(sys.version_info[0] * 100 + sys.version_info[1])' 2>/dev/null)
      if [ -n "$v" ] && [ "$v" -ge 309 ] && [ "$v" -le 312 ]; then echo "$c"; return; fi
    fi
  done
}

VENV="${CP_SEND_VENV:-$HOME/.code-painter-send}"
if [ ! -x "$VENV/bin/python" ] || ! "$VENV/bin/python" -c 'import syphon, websockets, PIL' >/dev/null 2>&1; then
  PY=$(pick)
  if [ -z "$PY" ]; then
    echo "The sender needs Python 3.9 – 3.12."
    echo "Install it from https://www.python.org/downloads/ (3.12), or run:  xcode-select --install"
    echo "then double-click send-to-resolume.command again."
    read -r -p "Press Return to close."; exit 1
  fi
  echo "First run: setting up the sender with $("$PY" --version 2>&1) (about a minute)…"
  rm -rf "$VENV"
  "$PY" -m venv "$VENV" && "$VENV/bin/python" -m pip install --upgrade --quiet pip \
    && "$VENV/bin/python" -m pip install --quiet syphon-python websockets Pillow \
    || { echo "Setting up failed (see above). Check the internet connection and try again."; read -r -p "Press Return to close."; exit 1; }
fi
"$VENV/bin/python" send-to-resolume.py "$@"
read -r -p "The sender stopped. Press Return to close."

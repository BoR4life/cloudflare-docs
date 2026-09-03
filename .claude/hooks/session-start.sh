#!/bin/bash
# SessionStart hook: prepare the cloudflare-docs workspace for Claude Code on the web.
set -euo pipefail

# Only run in remote (Claude Code on the web) sessions.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

# The Astro build and `astro check` need more heap than the Node default.
export NODE_OPTIONS="--max-old-space-size=4192"

# Installs dependencies and runs postinstall (patch-package + `astro sync`),
# which generates the .astro types that `astro check` and the editor rely on.
# `npm install` (not `npm ci`) so repeat runs reuse the cached node_modules.
# `--no-save` keeps package-lock.json untouched: npm otherwise rewrites key order on
# every run, leaving a dirty working tree at the start of each session.
npm install --no-save --no-fund --no-audit

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  {
    echo 'export NODE_OPTIONS="--max-old-space-size=4192"'
  } >> "$CLAUDE_ENV_FILE"
fi

#!/usr/bin/env bash
# soulscript: pkws helper
# Usage:
#   ./soulscripts/ss_git.sh                -> git status (default)
#   ./soulscripts/ss_git.sh status         -> git status
#   ./soulscripts/ss_git.sh pull           -> git pull origin master
#   ./soulscripts/ss_git.sh git pull       -> same as above
#   (future) ./soulscripts/ss_git.sh ssh shrine  -> other domain

# Detect repo root if possible
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

if [ -z "$REPO_ROOT" ]; then
  REPO_ROOT="."
fi

cd "$REPO_ROOT" || {
  echo "[ss] Error: could not cd into repo root: $REPO_ROOT"
  exit 1
}

# --- Domain + command parsing ---

first="$1"
shift || true   # safe even if no args

domain=""
cmd=""

if [ -z "$first" ]; then
  # No args: default to git status
  domain="git"
  cmd="status"
elif [ "$first" = "git" ]; then
  # Explicit domain: git
  domain="git"
  cmd="${1:-status}"
else
  # For now, treat anything else as a git subcommand
  # (later we can branch here: if [ "$first" = "ssh" ]; then ... )
  domain="git"
  cmd="$first"
fi

case "$domain" in
  git)
    case "$cmd" in
      pull)
        echo "[ss][git] git pull origin master"
        git pull origin master
        ;;
      push)
        echo "[ss][git] git push origin master"
        git push origin master
        ;;
      pushall)
        echo "[ss][git] git push origin master"
        git push origin master && \
        echo "[ss][git] git push github master" && \
        git push github master
        ;;
      pullall)
        echo "[ss][git] git pull origin master"
        git pull origin master && \
        echo "[ss][git] git pull github master"
        git pull github master
        ;;
      status|"")
        echo "[ss][git] git status -sb"
        git status -sb
        ;;
      *)
        echo "[ss][git] Unknown git command: $cmd"
        echo "Usage: $0 [git] {pull|push|pushall|pullall|status}"
        exit 1
        ;;
    esac
    ;;

  *)
    echo "[ss] Unknown domain: $domain"
    echo "Current domains: git"
    exit 1
    ;;
esac


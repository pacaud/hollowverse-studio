#!/usr/bin/env bash
# soulscript: pkws git helper
# Usage:
#   ss git status
#   ss git pull
#   ss git push
#   ss git pushall
#   ss git pullall
#   ss git add .
#   ss git add <file> [...]
#   ss git commit "message"

# Detect repo root
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
  REPO_ROOT="."
fi

cd "$REPO_ROOT" || {
  echo "[ss] Error: could not cd into repo root: $REPO_ROOT"
  exit 1
}

# If first arg is 'git', drop it: ss git <cmd> ...
if [ "$1" = "git" ]; then
  shift
fi

cmd="$1"
shift || true   # now $@ = rest of args (if any)

# Default command: status
if [ -z "$cmd" ]; then
  cmd="status"
fi

case "$cmd" in
  status)
    echo "[ss][git] git status -sb"
    git status -sb
    ;;

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

  add)
    if [ "$#" -eq 0 ]; then
      echo "[ss][git] git add ."
      git add .
    else
      echo "[ss][git] git add $*"
      git add "$@"
    fi
    ;;

  commit)
    msg="$*"
    if [ -z "$msg" ]; then
      echo "[ss][git] git commit"
      git commit
    else
      echo "[ss][git] git commit -m \"$msg\""
      git commit -m "$msg"
    fi
    ;;

  *)
    echo "[ss][git] Unknown git command: $cmd"
    echo "Usage: ss git {status|pull|push|pushall|pullall|add|commit}"
    exit 1
    ;;
esac

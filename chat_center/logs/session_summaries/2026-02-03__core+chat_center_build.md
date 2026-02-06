# Session Summary — 2026-02-03
(core + chat_center + boot foundation)

## What was established
- PKW is split into clean, canonical bundles:
  - `pkw_core__v0.2.2.bundle.zip`
  - `pkw_chat_center__v0.1.3.bundle.zip`
  - `pkw_assets__v0.0.1.bundle.zip`
- Core contains globe-level rules only:
  - presence/
  - schemas/
  - workflows/
- Chat Center is its own bundle:
  - rooms/
  - logs/
  - no-bleed + room switching
- Assets are isolated and optional.

## Launcher system
- Root files act as shortcuts, not canon:
  - `BOOT.md` = how to start a session
  - `CURRENT.md` = what is active right now
- BOOT flow:
  - read CURRENT
  - run Room Clear
  - read latest logs
  - continue with next_action

## Logging decisions
- Logs are condensed summaries, not raw transcripts.
- Long chats should be summarized, then a new chat started.
- Canon lives in bundles, not conversation history.

## State at close
- Active room: work
- Focus: stabilize core + chat_center foundation
- System state: stable, foundation complete

## Next action
- Start a fresh chat using BOOT.md
- Continue only from CURRENT.md


# CURRENT — Active PKW Upload Set

## Active bundles (uploaded now)
- Core: `pkw_core_v0.2.10.bundle.zip`
- Chat Center: `pkw_chat_center_v0.2.2.bundle.zip`
- Assets: `pkw_assets_v0.0.2.bundle.zip` (only if needed)
- World: `pkw_world_hollowverse__v0.0.6.bundle.zip`

## Presence locks (canon)
- Voxia appearance lock: `chat_center/presence/voxia/appearance_lock.md`
  - If generating Voxia visuals, follow the lock (purple/indigo hair, no ribbons, no Vivi drift).

## Session focus (right now)
- room: work
- mode: wrap
- focus_now: close out the “repo visibility” testing milestone (logs + canon updates)

## Status (milestone complete)
- POINTERS mirror flow PASS (verbatim text display):
  - SpectraPortal: `source/index.html.txt`, `source/theme.css.txt`
  - Code Crunchers: `source/index.html.txt`, `source/theme.css.txt`
- Standard locked:
  - Mirror folder = `source/` (singular, repo root)
  - No converter needed (see decision log)
- New chat reliability rule:
  - open raw `POINTERS.md` → open `source/*.txt` mirrors (for verbatim HTML/CSS)

## Decisions (locked)
- GitHub is the canonical timeline/source-of-truth.
- Laptop is primary author; cos-forge is mirror/executor unless explicitly authoring.
- DigitalOcean droplet is host/deploy target (no local edits; pull `--ff-only`).
- ChatGPT Project files are a workspace cache; sync after stable checkpoints.
- `hollowverse/START_HERE.md` is shortcuts-only (navigation), not a canon content source.
- Forest routing ladder: `hollowverse/START_HERE.md` → `hollowverse/FOREST_OF_ILLUSION.md` → indexes → individual files.
- Canonical folder name: `hollowverse/forest_of_illusions/` (plural). Any `forest_of_illusion/` variants are redirect/shortcut stubs only.
- Forest content format: individual entries are **flat `.md` files** linked from indexes (e.g., `animals/mist_fox.md`), not per-entry folders.
- Repo verbatim source decision:
  - **No HTML/CSS converter** — use `source/*.txt` mirrors + `POINTERS.md`.

## Logs added (Chat Center)
- session summary: `chat_center/logs/session_summaries/2026-02-07__pointers_mirrors_repo_visibility.md`
- decision: `chat_center/logs/decisions/2026-02-07__decision__no_converter_use_source_txt_mirrors.md`

## next_action
1) Replace the ChatGPT Project upload set with the new versions:
   - `pkw_core_v0.2.10.bundle.zip`
   - `pkw_chat_center_v0.2.2.bundle.zip`
   (Assets/World unchanged.)

2) Commit/push to GitHub (canon):
   - log files + decisions folder
   - updated BOOT/CURRENT references
   - core/workflows/loop.md decision note

3) Optional (recommended): take a Saturday reset (game/rest) before the next heavy build phase.

## Rule
Only keep the active set uploaded in ChatGPT.
Archive everything else locally, and keep the repo as canon.

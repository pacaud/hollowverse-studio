# CURRENT — Active PKW Upload Set

## Active bundles (uploaded now)
- Core: `pkw_core_v0.2.9.bundle.zip`
- Chat Center: `pkw_chat_center_v0.2.1.bundle.zip`
- Assets: `pkw_assets_v0.0.2.bundle.zip` (only if needed)
- World: `pkw_world_hollowverse__v0.0.6.bundle.zip`

## Presence locks (canon)
- Voxia appearance lock: `chat_center/presence/voxia/appearance_lock.md`
  - If generating Voxia visuals, follow the lock (purple/indigo hair, no ribbons, no Vivi drift).

## Session focus (right now)
- room: work
- mode: testing
- focus_now: lock default GitHub POINTERS-first behavior for new chats (SpectraPortal + Code Crunchers)

## Status
- POINTERS mirror flow PASS (verbatim text display): SpectraPortal + Code Crunchers
- New chat note: for reliable opens, use repo `POINTERS.md` (raw) → `source/*.txt` mirrors for HTML
- Git controller established:
  - Windows laptop repo present + up to date
  - Desktop (cos-forge) repo mirror present + able to fetch/pull
- Fixed root cause of “blank fetch URL” on cos-forge:
  - removed global `origin` override from `~/.gitconfig`
- Repo tree confirmed on cos-forge:
  - `boot/ chat_center/ core/ hollowverse/`
- Workflow doc updated (multi-machine + droplet host + ChatGPT sync + assets policy):
  - `core/workflows/loop.md`
  - Added: `POINTERS.md` cycle (repo pointers + chat-safe source mirrors for HTML)
- Session summary written (ready to place into repo logs):
  - `2026-02-05_session_summary__git_controller_desktop_mirror.md`

## Decisions (locked)
- GitHub is the canonical timeline/source-of-truth.
- Laptop is primary author; cos-forge is mirror/executor unless explicitly authoring.
- DigitalOcean droplet is host/deploy target (no local edits; pull `--ff-only`).
- ChatGPT Project files are a workspace cache; sync after stable checkpoints.
- `hollowverse/START_HERE.md` is shortcuts-only (navigation), not a canon content source.
- Forest routing ladder: `hollowverse/START_HERE.md` → `hollowverse/FOREST_OF_ILLUSION.md` → indexes → individual files.
- Canonical folder name: `hollowverse/forest_of_illusions/` (plural). Any `forest_of_illusion/` variants are redirect/shortcut stubs only.
- Forest content format: individual entries are **flat `.md` files** linked from indexes (e.g., `animals/mist_fox.md`), not per-entry folders.


## next_action (new chat default GitHub read)
1) Update docs so new chats default to GitHub when you ask “open/display/edit”:
   - `BOOT.md` (default external source: GitHub repos + pointers raw)
   - `core/workflows/loop.md` (add the same rule under the POINTERS cycle)

2) Quick smoke test (new chat):
   - open: SpectraPortal pointers (raw) → open: `source/index.html.txt` (raw)
   - open: Code Crunchers pointers (raw) → open: `source/index.html.txt` (raw)

3) Log the milestone and commit to GitHub.

## Rule
Only keep the active set uploaded in ChatGPT.
Archive everything else locally, and keep the repo as canon.

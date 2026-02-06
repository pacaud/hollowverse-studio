# CURRENT — Active PKW Upload Set

## Active bundles (uploaded now)
- Core: `pkw_core_v0.2.6.bundle.zip`
- Chat Center: `pkw_chat_center_v0.2.1.bundle.zip`
- Assets: `pkw_assets_v0.0.2.bundle.zip` (only if needed)
- World: `pkw_world_hollowverse__v0.0.6.bundle.zip`

## Presence locks (canon)
- Voxia appearance lock: `chat_center/presence/voxia/appearance_lock.md`
  - If generating Voxia visuals, follow the lock (purple/indigo hair, no ribbons, no Vivi drift).

## Session focus (right now)
- room: work
- mode: work
- focus_now: close out Git workflow + sync BOOT/CURRENT + log the milestone

## Status
- Git controller established:
  - Windows laptop repo present + up to date
  - Desktop (cos-forge) repo mirror present + able to fetch/pull
- Fixed root cause of “blank fetch URL” on cos-forge:
  - removed global `origin` override from `~/.gitconfig`
- Repo tree confirmed on cos-forge:
  - `boot/ chat_center/ core/ hollowverse/`
- Workflow doc updated (multi-machine + droplet host + ChatGPT sync + assets policy):
  - `core/workflows/loop.md`
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

## next_action (close-out checkpoint)
1) Update workflow loop (repo canon on Laptop):
   - replace: `core/workflows/loop.md` (now includes Voxia edit cycle + `main` branch)
   - `git add core/workflows/loop.md`
   - `git commit -m "Workflow: update loop (Voxia edit cycle + main branch)"`
   - `git push origin main`

2) Bump Core bundle version (workspace + exports):
   - export: `pkw_core_v0.2.6.bundle.zip`
   - update references in `BOOT.md` + `CURRENT.md`
   - commit + push those doc updates

3) Sync cos-forge mirror:
   - `git pull --ff-only`

4) Sync ChatGPT Project files (workspace cache):
   - upload/replace: `pkw_core_v0.2.6.bundle.zip`
   - upload/replace: `BOOT.md`, `CURRENT.md`
   - keep only the active bundles listed above

5) Optional: stop or switch to light tasks (recommended after a checkpoint)

## Rule
Only keep the active set uploaded in ChatGPT.
Archive everything else locally, and keep the repo as canon.

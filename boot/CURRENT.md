# CURRENT — Active PKW Upload Set

## Active bundles (uploaded now)
- Core: `pkw_core_v0.2.5.bundle.zip`
- Chat Center: `pkw_chat_center_v0.2.0.bundle.zip`
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
1) Update workflow doc in repo (Windows laptop):
   - replace: `core/workflows/loop.md`
   - `git add core/workflows/loop.md`
   - `git commit -m "Update workflow loop: multi-machine + droplet + ChatGPT sync"`
   - `git push origin master`

2) Place the session summary into repo logs:
   - path: `chat_center/logs/session_summaries/2026-02-05_session_summary__git_controller_desktop_mirror.md`
   - update `chat_center/logs/_index.md` with a link/entry
   - commit + push

3) Sync cos-forge mirror:
   - `git branch --set-upstream-to=origin/master master` (only if pull complains)
   - `git pull`

4) Sync ChatGPT Project files (this workspace cache):
   - upload/replace: `BOOT.md`, `CURRENT.md`
   - upload/replace: `chat_center/presence/voxia/appearance_lock.md`
   - upload the updated `loop.md` (optional but recommended)
   - keep only the active bundles listed above

5) Stop for the night (recommended):
   - no new repo setup tonight (SpectraPortal/CodeCrunchers tomorrow)

## Rule
Only keep the active set uploaded in ChatGPT.
Archive everything else locally, and keep the repo as canon.

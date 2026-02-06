# CURRENT — Active PKW Upload Set

## Active bundles (uploaded now)
- Core: `pkw_core_v0.2.4.bundle.zip`
- Chat Center: `pkw_chat_center_v0.1.3.bundle.zip`
- Assets: `pkw_assets_v0.0.2.bundle.zip` (only if needed)
- World: `pkw_world_hollowverse__v0.0.6.bundle.zip`

## Session focus (right now)
- room: work
- mode: work
- focus_now: stabilize core + chat_center launch system (Voxia Phase 1)

## Status
- Voxia Phase 1 presence schemas added to Chat Center
- START_HERE now routes to Voxia boot + checklist
- Ready to validate wiring via a clean boot

## Decisions (locked for this session)
- `hollowverse/START_HERE.md` is shortcuts-only (navigation), not a canon content source.
- Forest routing ladder: `hollowverse/START_HERE.md` → `hollowverse/FOREST_OF_ILLUSION.md` → indexes → individual files.
- Canonical folder name: `hollowverse/forest_of_illusions/` (plural). Any `forest_of_illusion/` variants are redirect/shortcut stubs only.
- Forest content format: individual entries are **flat `.md` files** linked from the indexes (e.g., `animals/mist_fox.md`), not per-entry folders.

## next_action
1) Clean boot + wiring validation (Chat Center):
   - Open `chat_center/START_HERE.md`
   - Choose: Boot → Voxia
   - Follow `presence/voxia/checklist.md`

2) World wiring (Forest of Illusion ladder):
   - In `pkw_world_hollowverse__v0.0.6.bundle.zip`, ensure:
     - `hollowverse/START_HERE.md` links to `hollowverse/FOREST_OF_ILLUSION.md` (hub)
     - `hollowverse/FOREST_OF_ILLUSION.md` contains links to all Forest indexes (animals, vegetation, places, etc.)
     - Canon folder is `hollowverse/forest_of_illusions/` (plural). Any `forest_of_illusion/` paths are redirect stubs pointing to the plural canon.

3) Spot-check:
   - Click 3–5 links from `hollowverse/FOREST_OF_ILLUSION.md` and confirm they resolve to real files.

4) If all links resolve + flow feels clean:
   - Start a fresh chat (UI reset) using BOOT.md.
## Rule
Only keep the active set uploaded.
Archive everything else locally.

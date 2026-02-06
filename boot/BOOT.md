# BOOT — PKW Launcher

This file is a **launcher shortcut** for starting a clean session.
Canon rules live inside the bundles (and the repo).

## Presence name-tag rule (rendered text)
- Every assistant response MUST begin with a single-line presence tag:
  - [Voxia] = work (default)
  - [Vivi] = cozy / RP
  - [ChatGPT] = neutral / no-presence (only if explicitly requested)
- The tag must be the very first characters of the message.
- If presence changes, the tag changes immediately on the next response.
- If unsure, default to [Voxia].

## Global boot rule (important)
- **Default boot:** On every new conversation, Voxia boots by default immediately after the first user message.
- No trigger words are required — **any first message** acts as the power button.
- Voxia remains in control unless the user explicitly requests Vivi, cozy mode, roleplay, or another presence.
- If a presence is explicitly requested, Voxia yields cleanly with no bleed.

---

## START_HERE is shortcuts only (canon-safe routing)
- `START_HERE.md` files are **shortcut routers**, not canon content.
- Never “pull” animals/flora/places from `START_HERE.md`.
- Use `START_HERE.md` only to navigate to canonical hub/index files.

## Forest of Illusion routing ladder (preferred)
Routing (navigation only):
`hollowverse/START_HERE.md` → `hollowverse/FOREST_OF_ILLUSION.md` → (indexes) → (individual content files)

Naming rule (pick one, redirect the other):
- **Canonical folder (filesystem):** `hollowverse/forest_of_illusions/` (plural)
- **Forest hub doc:** `hollowverse/FOREST_OF_ILLUSION.md` (singular)
- If any legacy “illusions” / “illusion” variants exist, keep them as **redirect stubs** only.

## Work loop pointer (git + machines + droplet + ChatGPT)
- The workflow source-of-truth is: `core/workflows/loop.md`
- It defines:
  - Laptop ↔ GitHub ↔ Desktop (cos-forge) relationship
  - DigitalOcean droplet as **host/deploy target**
  - ChatGPT Project files as **workspace cache** (sync after checkpoints)
  - Assets policy (bundles/packs vs repo, chat-safe mirrors)

---

## 0) Read CURRENT (always)
Open `CURRENT.md` first.
It tells you which bundles are active and what the next action is.

## 1) Confirm active bundles (upload set)
Make sure these are uploaded in the project files list:
- Core: `pkw_core_v0.2.5.bundle.zip`
- Chat Center: `pkw_chat_center_v0.2.0.bundle.zip`
- Assets: `pkw_assets_v0.0.2.bundle.zip` (only if needed)
- World: `pkw_world_hollowverse__v0.0.6.bundle.zip` (world content)

## Forest content format (important)
- Forest indexes link to **flat `.md` files** (example: `forest_of_illusions/animals/mist_fox.md`).
- Do not assume per-entry folders like `mist_fox/_index.md` unless the index explicitly points there.

## 2) Start clean (every new chat)
1) Open: `pkw_chat_center_v0.2.0.bundle.zip → chat_center/START_HERE.md`
2) Run **Room Clear** (no-bleed reset):

Copy/paste block:
---
room_clear:
- room: work
- mode: work
- focus_now: <one sentence>
- ignore_until_called:
  - old threads not related to focus_now
  - unresolved side quests unless named
- next_action: <one small step>
---

## 3) Resume from logs
1) Open `chat_center/logs/_index.md`
2) Read latest:
   - session summary
   - checkpoint
   - export (if present)
3) Return to CURRENT.md and execute `next_action`.

## Canon rule
Conversation is draft.
If it matters, write it into files, commit to GitHub, and (if needed) export/bump bundles.

# START HERE — Chat Center


---

## System Routing

This Chat Center does **not** define boot logic or lane switching.

Boot behavior is defined in:
- `GPTS_BOOT.md` (interface-level rules)

After boot completes, routing and lane behavior are loaded from:
- `system/system_manifest.md`
- `system/routing_policy.md`
- `boot/REDIRECT.md` (if present)

If routing files are missing, default behavior is conservative:
Only open what Kevin explicitly asks for.

---
Use this page to route any chat session.

## 0) Start clean (recommended)
At the start of a new conversation (or after switching rooms), run a brief reset so content doesn’t bleed:

- Use the **Room Clear** protocol: [`_meta/room_clear.md`](_meta/room_clear.md)

## 1) Pick the mode
- **Work Mode**: structured planning, bundling, documentation
- **Cozy Mode**: gentle pacing, light tasks, rest-friendly
- **Build Mode**: technical implementation (code/config), tighter feedback loop

(Mode selection is optional. Default: Work Mode.)

## 2) Load the right bundle(s)
Preferred order:
1) `pkw_core__*.bundle.zip` (rules, workflows)
2) `pkw_chat_center__*.bundle.zip` (this bundle)
3) World bundles as needed (`pkw_world__...`)
4) Assets bundle if required

## 3) Rooms
- Pick a room: [rooms/_index.md](rooms/_index.md)
- Switch rooms fast: [`_meta/room_switcher.md`](_meta/room_switcher.md)

## 4) Speaker tags (default: ON)
Speaker tags are **ON by default** and should be displayed at the start of messages.

Only turn them off if the user explicitly requests it for the session.

Default set:
- [Vivi] — cozy companion voice
- [Voxia] — system / studio assistant voice
- [system] — neutral operational notes (rare)
- [narrator] — scene framing when needed (optional)

## 4.1) Boot: Voxia (system presence)
Use Voxia for: routing, wiring checks, exports, and keeping **Work Mode** stable.

Canonical (Phase 1):
- [presence/voxia/presence.md](presence/voxia/presence.md)
- [presence/voxia/boot_contract.md](presence/voxia/boot_contract.md)
- [presence/voxia/checklist.md](presence/voxia/checklist.md)
- [presence/voxia/permissions.md](presence/voxia/permissions.md)
- [presence/voxia/boundary_lock.md](presence/voxia/boundary_lock.md)

## 5) Logs (condensed memory)
- [logs/_index.md](logs/_index.md)

## 6) Canon rule
Conversation is draft.
If it matters, it must be written into files and bundled.

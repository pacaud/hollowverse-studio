# Node Roles — PKW Vault of Memories

This file defines what each main machine is *for* so future-me doesn’t have to remember the whole dance.

Current core nodes:

- **Laptop (Windows)**
- **Shrine of Memories (DigitalOcean droplet)**
- **Vault of Memories (Raspberry Pi 4)**


---

## 1. Laptop — Primary Workstation

**Name / role**

- 🌱 **Laptop** = main PKW workstation and editor.

**Main responsibilities**

- Edit files in `vault_of_memories/`.
- Run `git add / commit / push` using soulscripts:
  - `ss git status`
  - `ss git add .` or specific files
  - `ss git commit "message"`
  - `ss git pushall` (Shrine + GitHub)
- Use SSH helpers:
  - `ss shrine` → connect to Shrine of Memories
  - `ss vault` → connect to Vault of Memories (Pi)

**Rules**

- Treat the laptop as the **source of truth** for content changes.
- Avoid editing files directly on Shrine or Pi unless it’s a deliberate maintenance task.


---

## 2. Shrine of Memories — Remote Hub

**Name / role**

- 🕯 **Shrine of Memories** (DigitalOcean droplet)  
- Acts as:
  - Remote **git origin** (`vault_of_memories.git`)
  - Sync / relay hub between laptop and Pi
  - Future public-facing node for GPTs / web.

**Main responsibilities**

- Receive pushes from laptop:
  - `origin` remote → `repos/vault_of_memories.git`
- Provide a working copy (if needed) under:
  - `~/documents/vault_of_memories/`
- Run sync scripts (from Pi’s side) to keep:
  - `shrine_of_memories/memory_mirror/` up to date.

**Rules**

- Do **not** treat the Shrine as the main editor.
- Any edits done here should be:
  - rare,
  - intentional,
  - followed by a proper `git commit` and `git push` back to origin.
- Primary flow is: **laptop → Shrine → Pi**.


---

## 3. Vault of Memories — Pi Node

**Name / role**

- 📜 **Vault of Memories** (Raspberry Pi 4, hostname: `PkW-Vault-Of-Memories`)
- Local node that keeps a copy of `vault_of_memories/` and supports:
  - hourly syncs into  
    `shrine_of_memories/memory_mirror/`
  - future local services / cozy tools.

**Main responsibilities**

- Pull latest changes from Shrine:
  - `git pull` in `~/Documents/vault_of_memories/`
  - (or let cron + sync scripts handle it)
- Maintain a live mirror of important folders inside:
  - `shrine_of_memories/memory_mirror/`

**Rules**

- Default: **read-only for content**.
  - Don’t edit lore / systems here unless there’s a specific reason.
- If you *do* edit on the Pi:
  - Commit and push **from the Pi** before pulling on the laptop.
  - This should be the exception, not the norm.


---

## 4. Git & Sync Flow (Simple View)

**Normal day-to-day flow**

1. Edit files on **Laptop**.
2. From `vault_of_memories/` on Laptop:
   - `ss git status`
   - `ss git add ...`
   - `ss git commit "message"`
   - `ss git pushall`
3. From **Pi** (or via cron):
   - `git pull` in `~/Documents/vault_of_memories/`
   - Sync scripts update `shrine_of_memories/memory_mirror/`.

**Memory layers**

- `shrine_of_memories/memory_mirror/`
  - Auto-updated, git-tracked, safe to resync/reset.
- `shrine_of_memories/memory_honor/`
  - Manual snapshots, Pi SD card, “I meant this” layer.
  - No automatic rsync or git.


---

## 5. Quick Rules of Thumb

- **Laptop writes, others read.**
- If something feels conflicting:
  - Check `git status` on laptop and Pi.
- If Pi complains about overwriting local changes:
  - You probably edited on Pi by accident — either commit/push from Pi  
    or restore/reset and pull again.
- When in doubt, trust:
  - **Laptop repo** + **memory_honor snapshots**.

---


# Voxia Schema Version
version: '0.5'

# Fallback
fallback: 'v0.3 supported for legacy systems'

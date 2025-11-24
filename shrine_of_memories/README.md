# Shrine of Memories

The **Shrine of Memories** is the storage heart of the Vault of Memories.

It links three layers:
- the **Shrine** in the cloud (droplet),
- the **Vault** at home (Pi),
- the **Keeper’s choice** layer (SD card / manual archive).

This folder does **not** store all data by itself —  
it describes *how* memory is mirrored and honored.

---

## Structure

- `memory_mirror/`  
  Live, Git-based mirror of the Shrine repo on the Pi.

  - Updated automatically on the Pi via:
    - `/home/kevin/pkw_node/shrine_sync.sh`
    - cron jobs:
      - `@reboot /home/kevin/pkw_node/shrine_connect_on_boot.sh`
      - `0 * * * * /home/kevin/pkw_node/shrine_sync.sh`
  - Represents: **“What the Shrine currently knows.”**

- `memory_honor/`  
  Manual, sacred snapshots.

  - Updated **only on purpose** by the Keeper.
  - Used for tar/zip archives or hand-picked copies.
  - Represents: **“This moment mattered. Keep this, even if everything else breaks.”**

---

## Mental Model

- Laptop → Shrine (push with `git`)  
- Shrine → Pi (pull with `git` via sync scripts)  
- Pi → SD card (manual snapshots into Memory Honor when it *feels right*)

- `memory_mirror/` = live reflection  
- `memory_honor/` = chosen, deliberate archive

If you’re reading this because you feel lost:
- Trust `memory_honor/` for what was sacred.
- Trust `memory_mirror/` for what is current.
- Rebuild from whichever one your heart says is right.


# Voxia Schema Version
version: '0.3'

# memory_mirror/ — Pi Mirror (Git-Synced)

This folder is part of the **Vault of Memories** repo and lives on every node
(laptop, Shrine droplet, Pi). It represents the *live mirror* of the Shrine.

## Role

- This folder is **Git-tracked**.
- It lives inside the main repo at:

  `vault_of_memories/shrine_of_memories/memory_mirror/`

- On the **Pi**, the whole repo is cloned to:

  `/home/kevin/Documents/vault_of_memories`

  and kept in sync from the Shrine using `git pull`.

## Sync Flow

- **Laptop**  
  - You edit files in `vault_of_memories/` (including this folder).  
  - Run: `git add`, `git commit`, `git push origin master`.

- **Shrine (droplet)**  
  - Holds the remote bare repo: `repos/vault_of_memories.git`.  
  - Stores the official history.

- **Pi (Vault mirror)**  
  - Has a working copy at: `/home/kevin/Documents/vault_of_memories`.
  - Syncs from Shrine using:

    - `/home/kevin/pkw_node/shrine_sync.sh`
    - Cron:
      - `@reboot /home/kevin/pkw_node/shrine_connect_on_boot.sh`
      - `0 * * * * /home/kevin/pkw_node/shrine_sync.sh`

  - These scripts run `git pull origin master` and log to:
    - `/home/kevin/shrine_sync.log`

## Edit Rules

- **Normal edits** should happen on the **laptop**, then be pushed to Shrine.
- The **Pi** is mostly **read-only mirror**:
  - You can read from here.
  - You *can* edit + `git commit` + `git push` from the Pi when needed,
    but treat that as a deliberate choice, not a habit.

## Future Notes

This folder can hold:

- status notes about sync
- extra metadata about mirrors
- any configs related specifically to “how the mirror behaves”

If you ever forget how the mirror works, remember:

> Laptop → Shrine (push)  
> Shrine → Pi (pull via scripts)  
> `memory_mirror/` = live, Git-based reflection of the repo.


# Voxia Schema Version
version: '0.3'

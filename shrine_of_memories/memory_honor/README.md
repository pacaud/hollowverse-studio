# memory_honor/ — Manual, Sacred Snapshots

This folder represents the **“I meant this”** layer of backup.

It is **not** for automatic sync.  
It exists to hold **deliberate, manual snapshots** of important states.

## Role

- Symbolically linked to the **Pi SD card**.
- Used for **long-term, intentional backups**, not constant mirroring.
- Protected from:
  - automatic `git pull` / `git push`
  - automatic rsync jobs

Memory Honor is where you put things when you want to say:

> “This moment mattered. Keep this, even if everything else breaks.”

## Recommended Use

When something important happens (big structural change, emotional milestone, etc.):

1. From the Pi (or droplet), create a snapshot of the repo or key paths:
   - Example (adjust paths as needed):

   ```bash
   # Example: archive the whole repo
   tar czf /media/kevin/MEMORY_HONOR/vault_$(date +%Y-%m-%d).tar.gz -C /home/kevin/Documents vault_of_memories


# Voxia Schema Version
version: '0.3'

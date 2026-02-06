# Workflow Loop (Git-backed + Multi-machine)

This loop is the default working rhythm for PKW: Universe.
Goal: build → verify → log → commit stable checkpoints → keep ChatGPT Project files in sync.

This document also defines how **Laptop**, **Desktop (cos-forge)**, **GitHub**, **ChatGPT Project files**, and the **DigitalOcean Droplet (host)** work together.

---

## 0) Roles (who does what)

### GitHub (remote)
- The **canonical timeline** and shared source-of-truth.
- Stores the repo history and stable checkpoints.

### Laptop (primary author)
- Default **editing machine**.
- Where you usually: edit → bundle → verify → commit → push.
- Keeps the work loop simple and avoids conflicts.

### Desktop / cos-forge (mirror + executor)
- Default **mirror** of GitHub + optional build/test box.
- Normally: `git pull` and run heavier tests/build steps.
- Only commits if you explicitly decide: “desktop is author for this change.”

### DigitalOcean Droplet (host / publish)
- The **runtime host** for public-facing things (website, demos, services).
- Pulls from GitHub (or receives deploy artifacts) and serves them via Nginx/systemd/etc.
- Should generally **not** be the main editing machine.
- Treat it as: **deploy target**, not authoring workstation.

### ChatGPT Project files (workspace cache)
- A **working snapshot** so ChatGPT can read BOOT/CURRENT/bundles without you re-uploading every time.
- Not canonical by itself. Canon is repo + bundles.
- Keep it synced after stable checkpoints (see Section 10).

---

## 1) Core rules
- **Canon lives in files + bundles**, not in chat messages.
- Chat is a **workbench**; GitHub is the **timeline + source-of-truth**.
- Commit only when you can say: **“this state is safe to return to.”**
- Prefer **canonical paths**; shortcuts are routing aids only.

---

## 2) Start of cycle (sync + room)

### On the machine you are working on (usually Laptop)
1) Sync from GitHub:
   - `git pull`
2) room_clear (work)
3) open `CURRENT.md` and follow `next_action`

### On cos-forge (when you switch or before running tests)
1) Sync from GitHub:
   - `git pull`

---

## 3) Work phase (make changes)
During the cycle you may:
- create/edit `.md` files
- update indexes/manifests
- bump bundle versions when needed
- update `BOOT.md` / `CURRENT.md` when wiring changes
- add/adjust shortcuts (only if canon paths remain correct)

Notes:
- Keep changes small and reversible.
- Treat bundles as “release artifacts” that reflect canon state.

---

## 4) Verify phase (before logging/committing)
Run a fast verification pass:

### A) Wiring checks
- `START_HERE.md` → hub → indexes
- 3–5 link spot-checks across categories (animals / vegetation / terrain or places / weather)

### B) Content pulls (confidence stamp)
- Pull at least 1–3 canon items:
  - random plant
  - animal (and legendary if available)
  - weather

### C) Assets sanity
- Confirm referenced asset paths exist in the assets bundle.
- If Chat UI fails to render PNG:
  - keep PNG as canon
  - create a **chat-safe JPG mirror** later (do not block progress)

---

## 5) Log phase (always)
Write a short log entry under:
- `chat_center/logs/session_summaries/`

Include:
- what changed (files/bundles)
- what passed/failed (wiring, pulls, assets)
- next action

### Log cap rule
- If a log file hits ~**250 lines**, roll to a new part:
  - `YYYY-MM-DD_session_summary__p01.md`
  - `YYYY-MM-DD_session_summary__p02.md`
- Add a rollover marker at the end of the old file.

---

## 6) Commit triggers (when to commit)
Commit when **any** of these are true:
- A wiring step **PASS**
- A bundle version **bump**
- Presence wiring/boot contracts updated
- A session ended and the state is “known good”

Avoid committing when:
- you’re mid-experiment and unsure
- verification failed and you haven’t logged + fixed

---

## 7) Commit + push (stable checkpoint)
Typical flow (usually on Laptop):

- `git status`
- `git add <paths>`
- `git commit -m "<checkpoint message>"`
- `git push origin master`

Commit message style (examples):
- `Wiring PASS: Step 2 forest ladder + logs (2026-02-05)`
- `Bump: pkw_world_hollowverse v0.0.6 + route fixes`
- `Presence: Voxia Phase 1 contracts + boot wiring`

---

## 8) Multi-machine safety rules (Laptop + Desktop)
To avoid conflicts:

1) **Pull before edits**
- On whichever machine you will edit on: `git pull` first.

2) **One author at a time (recommended)**
- Default: Laptop authors, cos-forge mirrors/tests.
- If you author on cos-forge, do it intentionally and push promptly.

3) **Switching machines**
- After you push on one machine, always `git pull` on the other before doing anything.

---

## 9) Deploy cycle (Droplet publish)
After a stable checkpoint is pushed to GitHub:

1) On the droplet, update to the latest code:
- `git pull` (or pull a specific branch/tag)

2) Build/restart as needed:
- build steps (if any)
- reload services (Nginx/systemd/pm2/etc.)

3) Confirm the site/service is live:
- quick smoke test (homepage loads, key routes work)

Notes:
- Prefer **fast-forward-only** pulls on droplet.
- Avoid local edits on droplet. If an emergency hotfix happens, immediately push it back to GitHub and pull on author machine.

---

## 10) Sync ChatGPT Project files (after a stable checkpoint)
After meaningful edits (especially to `BOOT.md`, `CURRENT.md`, bundles, workflow docs), update the ChatGPT **Project Files** so ChatGPT is working from the latest canon snapshot.

Upload/replace in the ChatGPT Project:
- `BOOT.md` (latest)
- `CURRENT.md` (latest)
- any updated `.bundle.zip` files referenced by CURRENT
- any standalone workflow/docs you want available without opening bundles (like this file)

Rule of thumb:
- If you **bumped a bundle** or changed **routing**, do the Project upload in the same session.
- Keep only the latest versions visible in the Project file list to prevent drift.

---

## 11) Repeat
After pushing + deploying + syncing Project files:
- update `CURRENT.md` if next steps changed
- start the next cycle

---

## Principle
**Build small. Verify fast. Log always. Commit only safe states. Deploy from GitHub. Sync Project files after checkpoints.**

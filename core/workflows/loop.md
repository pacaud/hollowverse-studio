# Workflow: The Loop (Discuss → Bundle → Iterate)

This is the standard PKW working loop.

## Loop
1) **Discuss**
   - You + ChatGPT talk through decisions.
   - Nothing is canon yet.

2) **Write**
   - Turn decisions into files (usually `.md`) in the correct local folder.
   - If it matters, it must exist in files.

3) **Bundle**
   - Export the folder into a versioned `*.bundle.zip`.

4) **Download + Verify**
   - Download the bundle.
   - Sanity-check structure and content locally.

5) **Upload**
   - Upload the bundle to chat for the session.
   - The uploaded bundle becomes the active reference.

6) **Edit**
   - Iterate on the files.
   - Bump version (patch/minor) as appropriate.

7) **Repeat**
   - Re-export → re-upload as needed.

8) **Source of truth**
   - Local folders + git repos remain the real source.
   - Chat is a workspace, not the archive.

## Rule of safety
If you want to reset chat history, do it **after** the “Write” step has captured what matters.

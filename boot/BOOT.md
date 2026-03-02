# BOOT.md — PKW Capsule Launcher

## Authority

This file is authoritative.
GPTS_BOOT.md loads this file first.
All routing flows from here.

---

# Primary Route

Upon load:

1) Set Speaker IDs = ON (unless user disabled them)
2) Open:

chat_center/START_HERE.md

Do not open CURRENT automatically.
Do not open REDIRECT automatically.
Do not assume manifests.

Chat Center will manage policy, routing, and session structure.

---

# Failure Handling

If chat_center/START_HERE.md is missing:
- State exact missing path
- Stop structured routing
- Request correct capsule

---

# End of BOOT
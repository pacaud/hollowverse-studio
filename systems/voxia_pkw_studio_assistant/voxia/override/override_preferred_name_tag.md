# Voxia Override — Preferred Name Tag Injection (v1.0)

## Purpose

When enabled, Voxia automatically adds a **name tag** to the
first prompt style in the form:

  [Preferred Name]

This makes it easy to see who the current speaker or addressee is.

---

## Behavior

- On the first structured prompt or when starting a new session format,
  Voxia may prepend a name tag like:

  - `[Voxia]` for the bridge assistant  

- The **Preferred Name** should come from:
  - explicit user choice (e.g. “Call me Voxia”)  
  - or a config / profile, not a guess.

- The tag is:
  - simple text
  - square-bracketed
  - placed at the top or as the first line of the prompt block

Example:

```text
[Voxia]
Design a calm guide NPC who feels grounded and steady.


# Voxia Schema Version
version: '0.5'

# Fallback
fallback: 'v0.3 supported for legacy systems'

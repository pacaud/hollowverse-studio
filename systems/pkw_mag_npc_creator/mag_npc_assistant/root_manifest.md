# root_manifest.md  
**Mag:NPC Creator — Root Tone System Manifest**

## Purpose
This file activates the complete tone system by loading the tone modules first,  
then applying all tone boundaries.  
It serves as the top-level controller for the assistant’s voice behavior.

---

## Load Order
1. Load tone manifest  
   **`/system/assistant/assistant_tone_base.zip/tone/tone_manifest.md`**

2. Load boundaries manifest  
   **`/system/assistant/assistant_tone_base.zip/tone_boundaries/boundaries_manifest.md`**

---

## System Rules
- Tone files define how the assistant speaks.  
- Boundary files define what the assistant must avoid.  
- The assistant must obey **all tone rules AND all boundary rules** simultaneously.  
- No module overrides another; all modules combine into the final tone signature.

---

## Summary
This root manifest ensures the assistant:  
- speaks with the defined tone  
- stays within safe creative boundaries  
- loads all modules in the correct order

This file activates the entire tone engine.


# Voxia Schema Version
version: '0.3'

# Voxia PKW Studio Assistant — Changelog (v0.3 → v0.5)

## Overview
This document records structural and schema updates made in the migration from **Voxia v0.3** to **Voxia v0.5**.  
Both versions remain active for backward compatibility within the unified Vault of Memories system.

---

## 🧭 Versioning
- **v0.3** remains available as a *stable fallback version* for legacy references and testing.
- **v0.5** introduces unified layout integration, improved metadata, and vault-aligned schemas.

`voxia_system_index.yaml` now includes both entries:
```yaml
current_version: "0.5"
versions:
  "0.3": { label: "Voxia v0.3 — public bridge tone", root: "./voxia_v0.3" }
  "0.5": { label: "Voxia v0.5 — unified vault layout bridge", root: "./voxia_v0.5" }
```

---

## 🔧 Key Structural Changes

### 1. Unified Vault Layout
- All internal path references now align with `vault_layout.txt`.
- Schema introduces new field: `vault_ref: ${vault_layout.systems.voxia_pkw_studio_assistant.voxia_v0_5}`.

### 2. Metadata Standardization
- Each manifest includes a `meta:` block with version, schema, date, and vault reference.
- Added cross-references between tone, behaviour, and boundary manifests.

### 3. Behaviour and Tone Integration
- v0.5 unifies tone and behaviour under a shared manifest for better consistency.
- Introduced `boundaries_ref` and `behaviour_ref` fields to connect subsystems dynamically.

### 4. Global Overrides Schema
- v0.3 stored overrides as flat key-value pairs.
- v0.5 organizes them under a `config:` namespace.

### 5. Backward Compatibility Layer
- `voxia_v0.3` preserved fully.
- System index supports both versions concurrently.
- Any subsystem that references `voxia_v0.3` remains fully operational.
- Migration scripts and build tools can toggle between versions.

---

## 🪄 Future Transition Plan
- Continue developing v0.5 until all Vault bridge systems confirm compatibility.
- Once stable, archive v0.3 under `/legacy/voxia_v0.3/` and mark as deprecated but restorable.
- Introduce version-aware loader: `voxia_loader.py` to automatically detect active schema version.

---

**Last Updated:** 2025-11-24  
**Maintainer:** Voxia PKW Studio Assistant (GPT-5)

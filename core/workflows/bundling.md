# Workflow: Bundling

Goal: produce a clean `*.bundle.zip` snapshot that is safe to upload.

## Steps
1) Run the preflight checklist: [`../RESTRAINTS.md`](../RESTRAINTS.md)
2) Confirm you are exporting **one bundle**
3) Ensure the bundle has a top-level `_index.md`
4) Check size targets:
   - aim < ~400MB (active)
   - never exceed 512MB (hard)
5) Avoid nested zips (max 1 legacy sub-zip)
6) Export with a versioned name:
   - `pkw_<scope>__v<semver>.bundle.zip`
7) Update `core/BUNDLE_REGISTRY.md` if this is a new bundle
8) Upload and work from the exported zip for that session

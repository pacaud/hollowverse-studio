# Workflow: Bundling

Goal: produce a clean `*.bundle.zip` snapshot that is safe to upload.

## Steps
1) Confirm you are exporting **one bundle**
2) Ensure the bundle has a top-level `_index.md`
3) Check size targets:
   - aim < ~400MB (active)
   - never exceed 512MB (hard)
4) Avoid nested zips (max 1 legacy sub-zip)
5) Export with a versioned name:
   - `pkw_<scope>__v<semver>.bundle.zip`
6) Update `core/BUNDLE_REGISTRY.md` if this is a new bundle
7) Upload and work from the exported zip for that session

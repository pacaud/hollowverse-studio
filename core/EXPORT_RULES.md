# Export Rules — PKW Core

Local folders are the source of truth.
Bundle zips are export snapshots designed for upload and portability.

## What to export
Export one bundle at a time:
- Core bundle
- World bundles
- Assets bundle
- Chat Center bundle (if separated later)

Avoid exporting a "mega-zip" containing everything unless strictly needed.

## Export checklist
0) Run the preflight checklist: [`RESTRAINTS.md`](RESTRAINTS.md)
1) Ensure the bundle has a top-level `_index.md`
2) Keep bundle size under the design target:
   - ~400MB active budget
   - ~100MB overflow buffer
3) Avoid nested zips:
   - Allow at most one legacy sub-zip (rare)
4) Name the bundle using the naming rules:
   - `pkw_<scope>__v<semver>.bundle.zip`
5) Update `BUNDLE_REGISTRY.md` if a new bundle is created.

## Recommended tooling
- Use a consistent bundler script (e.g., Python) to avoid manual mistakes.
- Include a build hash or timestamp in an optional metadata file:
  - `_bundle.meta.json` (optional, but recommended later)

## Path discipline (ChatGPT sandbox vs user machines)
- In ChatGPT's workspace, uploaded files appear under: `/mnt/data/`.
- Treat `/mnt/data/` as a temporary sandbox workspace. Do not imply these paths exist on the user's machines.
- When giving commands for the user's machines:
  - Prefer *relative* instructions ("run from repo root") over absolute paths.
  - If an absolute path is required, ask the user for it or read the project's docs (e.g., `POINTERS.md`).

See also:
- [`workflows/importing.md`](workflows/importing.md)

## Operational rule
If you need to actively work inside a bundle, export that bundle as a top-level zip
rather than nesting additional archives.

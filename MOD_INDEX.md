# Personal Mod Index

This repository publishes an automatic mod index for all installable `.zip` files stored in the repository root.

The output follows the `schema_version: 1` feed shape used by `gen1recomp-mod-index`, while supporting this repository's monorepo layout: every ZIP is inspected directly and its internal `manifest.json` becomes one index entry.

## Published files

After GitHub Pages is enabled with **Source: GitHub Actions**, the workflow publishes:

- a searchable web page at `https://faff0x.github.io/gen1recomp/`;
- the machine-readable feed at `https://faff0x.github.io/gen1recomp/data/index.json`;
- one generated Markdown description per mod under `data/mods/<author>@<id>/description.md`.

## How it works

`python scripts/build_mod_index.py`:

1. finds every `.zip` in the repository root;
2. requires exactly one `manifest.json` inside each archive;
3. reads the mod ID, title, author, version, category, API, game version, permissions, dependencies and conflicts;
4. creates a direct download URL for that exact ZIP;
5. writes `site/data/index.json` and generated descriptions;
6. fails the build when an archive is invalid, has no manifest, has a non-semver version, or duplicates another mod ID.

The workflow runs after changes to ZIP files, the generator, the site, or the workflow itself.

## Local validation

From the repository root:

```bash
python scripts/build_mod_index.py
python -m http.server -d site 8080
```

Then open `http://localhost:8080`.

## Adding or updating a mod

Upload the new ZIP to the repository root. Keep these requirements:

- the archive contains exactly one `manifest.json`;
- `manifest.json.id` uses only letters, numbers, `_` or `-`;
- `manifest.json.version` is semantic versioning such as `1.2.0`;
- IDs are unique across all ZIP files;
- the ZIP remains directly installable by Gen 1 Recomp.

No hand-written index entry is necessary. The next successful deployment rebuilds the complete feed.

## Difference from the community index

The community project normally keeps one metadata folder per mod and can track one GitHub Releases repository per entry. This repository stores many mod ZIPs together, so automatic release tracking is disabled per entry and each generated `downloadURL` points directly to the corresponding file on the `main` branch.

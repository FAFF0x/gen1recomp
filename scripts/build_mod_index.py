#!/usr/bin/env python3
"""Build a Gen 1 Recomp-compatible index from mod ZIP files in the repo root."""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
DATA_DIR = SITE_DIR / "data"
MODS_DIR = DATA_DIR / "mods"

REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "FAFF0x/gen1recomp")
DOWNLOAD_REF = os.environ.get("INDEX_DOWNLOAD_REF", "main")
DEFAULT_AUTHOR = REPOSITORY.split("/", 1)[0]
REPO_URL = f"https://github.com/{REPOSITORY}"

ALLOWED_CATEGORIES = [
    "GAMEPLAY", "CONTENT", "BALANCE", "ART", "AUDIO", "UI", "QOL",
    "TRANSLATION", "TOTAL_CONVERSION", "LIBRARY", "TOOL", "OTHER",
]
ALLOWED_PROFILES = {"content", "overhaul", "total_conversion"}
ALLOWED_PERMISSIONS = {"network", "filesystem", "engine_internals"}
ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+].*)?$")

CATEGORY_MAP = {
    "QUEST": "CONTENT",
    "STORY": "CONTENT",
    "QUALITY_OF_LIFE": "QOL",
    "QUALITY OF LIFE": "QOL",
    "TOTAL CONVERSION": "TOTAL_CONVERSION",
}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text_from_zip(archive: zipfile.ZipFile, path: str) -> str | None:
    try:
        return archive.read(path).decode("utf-8-sig").strip()
    except (KeyError, UnicodeDecodeError):
        return None


def find_manifest(archive: zipfile.ZipFile) -> tuple[str, dict[str, Any]]:
    candidates = [
        name for name in archive.namelist()
        if not name.endswith("/") and PurePosixPath(name).name.lower() == "manifest.json"
    ]
    if len(candidates) != 1:
        raise ValueError(f"expected exactly one manifest.json, found {len(candidates)}")

    manifest_path = candidates[0]
    raw = read_text_from_zip(archive, manifest_path)
    if raw is None:
        raise ValueError("manifest.json is not valid UTF-8")
    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid manifest.json: {exc}") from exc
    if not isinstance(manifest, dict):
        raise ValueError("manifest.json must contain a JSON object")
    return manifest_path, manifest


def normalize_categories(value: Any) -> list[str]:
    values = value if isinstance(value, list) else [value]
    result: list[str] = []
    for item in values:
        if not isinstance(item, str):
            continue
        category = CATEGORY_MAP.get(item.strip().upper(), item.strip().upper())
        if category in ALLOWED_CATEGORIES and category not in result:
            result.append(category)
    return result[:4] or ["OTHER"]


def normalize_requirements(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    result: list[str] = []
    for item in value:
        requirement: str | None = None
        if isinstance(item, str):
            requirement = item.strip()
        elif isinstance(item, dict):
            mod_id = item.get("id")
            version = item.get("version") or item.get("constraint")
            if isinstance(mod_id, str) and mod_id:
                requirement = mod_id if not version else f"{mod_id}@{version}"
        if requirement and requirement not in result:
            result.append(requirement)
    return result


def one_line(value: Any, fallback: str) -> str:
    if not isinstance(value, str):
        return fallback
    compact = " ".join(value.split())
    return compact[:200] or fallback


def optional_manifest_fields(manifest: dict[str, Any]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    api = manifest.get("api")
    if isinstance(api, int) and 1 <= api <= 2:
        output["api"] = api
    game_version = manifest.get("game_version")
    if isinstance(game_version, str) and game_version:
        output["game_version"] = game_version[:64]
    profile = manifest.get("profile")
    if profile in ALLOWED_PROFILES:
        output["profile"] = profile
    if isinstance(manifest.get("affects_link"), bool):
        output["affects_link"] = manifest["affects_link"]
    if isinstance(manifest.get("experimental"), bool):
        output["experimental"] = manifest["experimental"]
    permissions = manifest.get("permissions")
    if isinstance(permissions, list):
        clean = [p for p in permissions if p in ALLOWED_PERMISSIONS]
        if clean:
            output["permissions"] = list(dict.fromkeys(clean))
    dependencies = normalize_requirements(manifest.get("dependencies"))
    conflicts = normalize_requirements(manifest.get("conflicts"))
    if dependencies:
        output["dependencies"] = dependencies
    if conflicts:
        output["conflicts"] = conflicts
    license_name = manifest.get("license")
    if isinstance(license_name, str) and license_name:
        output["license"] = license_name[:64]
    return output


def build_description(
    archive: zipfile.ZipFile,
    manifest_path: str,
    title: str,
    summary: str,
    download_url: str,
) -> str:
    parent = PurePosixPath(manifest_path).parent
    for name in ("description.md", "README.md", "readme.md"):
        text = read_text_from_zip(archive, str(parent / name))
        if text:
            return f"{text}\n\n---\n\n[Source repository]({REPO_URL}) · [Download ZIP]({download_url})\n"
    return f"# {title}\n\n{summary}\n\n[Source repository]({REPO_URL}) · [Download ZIP]({download_url})\n"


def build_entry(zip_path: Path) -> dict[str, Any]:
    download_url = (
        f"https://raw.githubusercontent.com/{REPOSITORY}/"
        f"{quote(DOWNLOAD_REF, safe='')}/{quote(zip_path.name, safe='')}"
    )
    with zipfile.ZipFile(zip_path) as archive:
        manifest_path, manifest = find_manifest(archive)
        mod_id = manifest.get("id")
        if not isinstance(mod_id, str) or not ID_RE.fullmatch(mod_id):
            raise ValueError("manifest id is missing or invalid")
        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
            raise ValueError("manifest version is missing or is not semver")
        title_value = manifest.get("name") or manifest.get("title") or mod_id.replace("_", " ").title()
        title = one_line(title_value, mod_id)[:80]
        author = one_line(manifest.get("author"), DEFAULT_AUTHOR)[:64]
        summary = one_line(manifest.get("description"), f"{title} mod for Pokémon Gen 1 Recomp.")
        folder = f"{DEFAULT_AUTHOR}@{mod_id}"
        entry: dict[str, Any] = {
            "folder": folder,
            "id": mod_id,
            "title": title,
            "author": author,
            "summary": summary,
            "version": version,
            "categories": normalize_categories(manifest.get("categories", manifest.get("category"))),
            "repo": REPO_URL,
            "downloadURL": download_url,
            "automatic_version_check": False,
            **optional_manifest_fields(manifest),
            "thumbnail": None,
            "description_url": f"data/mods/{folder}/description.md",
            "latest": None,
            "update_check": "off",
        }
        root_parts = PurePosixPath(manifest_path).parts
        if len(root_parts) > 1:
            install_folder = root_parts[0]
            if install_folder != mod_id and ID_RE.fullmatch(install_folder):
                entry["folderName"] = install_folder
        description = build_description(archive, manifest_path, title, summary, download_url)

    output_dir = MODS_DIR / folder
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "description.md").write_text(description, encoding="utf-8")
    return entry


def main() -> None:
    zip_paths = sorted(ROOT.glob("*.zip"), key=lambda path: path.name.lower())
    if not zip_paths:
        fail(f"no mod ZIP files found in {ROOT}")
    if MODS_DIR.exists():
        shutil.rmtree(MODS_DIR)
    MODS_DIR.mkdir(parents=True, exist_ok=True)

    mods: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_ids: set[str] = set()
    for zip_path in zip_paths:
        try:
            entry = build_entry(zip_path)
            if entry["id"] in seen_ids:
                raise ValueError(f"duplicate mod id {entry['id']!r}")
            seen_ids.add(entry["id"])
            mods.append(entry)
            print(f"indexed {zip_path.name}: {entry['id']} {entry['version']}")
        except (OSError, zipfile.BadZipFile, ValueError) as exc:
            errors.append(f"{zip_path.name}: {exc}")
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        fail(f"index build failed for {len(errors)} archive(s)")

    mods.sort(key=lambda mod: str(mod["title"]).casefold())
    index = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(mods),
        "categories": ALLOWED_CATEGORIES,
        "mods": mods,
    }
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {DATA_DIR / 'index.json'} with {len(mods)} mods")


if __name__ == "__main__":
    main()

"""Generate a changeset file from staged git changes.

Usage: python scripts/gen_changeset.py [--bump minor|patch|major|none] [--summary TEXT]
"""

import argparse
import json
import subprocess
import uuid
from pathlib import Path
from typing import Iterable, Set

from changeset_paths import (
    REPO_ROOT,
    SERVICES_DIR,
    path_bumps_service,
    path_to_service,
    pkg_name,
    read_pyproject_version,
)
from seed_package_json import build_package_json

CHANGESET_DIR = REPO_ROOT / ".changeset"


def staged_paths() -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--staged", "--name-only"],
        capture_output=True, text=True, check=True, cwd=REPO_ROOT,
    ).stdout
    return [line for line in out.splitlines() if line.strip()]


def affected_services(paths: Iterable[str]) -> Set[str]:
    services = set()
    for p in paths:
        if path_bumps_service(p):
            svc = path_to_service(p)
            if svc is not None:
                services.add(svc)
    return services


def seed_missing_package_json(services: Iterable[str], services_dir: Path = SERVICES_DIR) -> list[Path]:
    """Create package.json for services that lack one; existing files are left alone.

    Changesets only knows a service through its package.json, so a new service
    named in a changeset without one breaks `changeset version`.
    """
    created = []
    for svc in sorted(services):
        pkg = services_dir / svc / "package.json"
        pyproject = services_dir / svc / "pyproject.toml"
        if pkg.exists() or not pyproject.exists():
            continue
        data = build_package_json(svc, read_pyproject_version(pyproject))
        pkg.write_text(json.dumps(data, indent=2) + "\n")
        created.append(pkg)
    return created


def render_changeset(services: Set[str], bump: str, summary: str) -> str:
    lines = ["---"]
    if services and bump != "none":
        for svc in sorted(services):
            lines.append(f'"{pkg_name(svc)}": {bump}')
    lines.append("---")
    lines.append("")
    lines.append(summary)
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bump", choices=["minor", "patch", "major", "none"], default="minor")
    parser.add_argument("--summary", default="Update service")
    args = parser.parse_args()

    services = affected_services(staged_paths())
    if args.bump != "none" and not services:
        print("No releasable service changes staged; emitting empty changeset")

    created = seed_missing_package_json(services)
    if created:
        # `npm ci` in the release workflow rejects workspaces missing from the lock file.
        subprocess.run(
            ["npm", "install", "--package-lock-only", "--ignore-scripts", "--no-audit", "--no-fund"],
            check=True, cwd=REPO_ROOT,
        )
        subprocess.run(["git", "add", "--", "package-lock.json", *map(str, created)], check=True, cwd=REPO_ROOT)
        print(f"Seeded {len(created)} package.json files")

    # render_changeset emits empty frontmatter when bump == "none" or no services.
    emitted = services if args.bump != "none" else set()
    content = render_changeset(services, args.bump, args.summary)
    CHANGESET_DIR.mkdir(exist_ok=True)
    out = CHANGESET_DIR / f"{uuid.uuid4().hex[:8]}.md"
    out.write_text(content)
    print(f"Wrote {out} ({len(emitted)} services, bump={args.bump})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Aggregate service changelogs into root CHANGELOG.md index.

Derives changed services from the pyproject.toml version diff between the working
tree and HEAD (post `changeset version` + sync_pyproject, before the changesets
action commits), and the release highlights from the changesets that
`changeset version` consumed.
"""

import re
import subprocess
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from changeset_paths import REPO_ROOT, _VERSION_RE, pkg_name

_CHANGESET_RE = re.compile(r"\A\s*---\n(.*?)\n---\n(.*)\Z", re.DOTALL)
_RELEASE_RE = re.compile(r"^[ \t]*\S+[ \t]*:[ \t]*(?:major|minor|patch)[ \t]*$", re.MULTILINE)


def _extract(text: str) -> Optional[str]:
    m = _VERSION_RE.search(text)
    return m.group(1) if m else None


def changed_services(repo_root: Path) -> Dict[str, str]:
    """Return {service: new_version} for services whose pyproject version changed
    in the working tree relative to HEAD.

    Run inside the changesets `version` step, where `changeset version` and
    sync_pyproject have edited pyproject.toml in the working tree but not yet
    committed. The new version is read from the working-tree file; the old
    version from HEAD.
    """
    changed_paths = subprocess.run(
        ["git", "diff", "HEAD", "--name-only", "--", "services/*/pyproject.toml"],
        capture_output=True, text=True, cwd=repo_root,
    ).stdout.splitlines()

    result: Dict[str, str] = {}
    for path in changed_paths:
        parts = Path(path).parts
        if len(parts) < 2:
            continue
        service = parts[1]
        new_ver = _extract((repo_root / path).read_text())
        old = subprocess.run(
            ["git", "show", f"HEAD:{path}"],
            capture_output=True, text=True, cwd=repo_root,
        )
        old_ver = _extract(old.stdout) if old.returncode == 0 else None
        if new_ver and new_ver != old_ver:
            result[service] = new_ver
    return result


def consumed_changesets(repo_root: Path) -> List[Tuple[str, int]]:
    """Return (summary, package_count) for each changeset `changeset version`
    consumed, oldest first.

    `changeset version` deletes the changeset files from the working tree, but
    HEAD still has them. Changesets that release no package are skipped.
    """
    def git(*args: str) -> str:
        return subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True, cwd=repo_root,
        ).stdout

    deleted = set(git("diff", "HEAD", "--name-only", "--diff-filter=D", "--", ".changeset/*.md").splitlines())
    added = git("log", "--reverse", "--diff-filter=A", "--name-only", "--format=", "HEAD", "--", ".changeset")

    result = []
    for path in dict.fromkeys(added.splitlines()):
        if path not in deleted:
            continue
        m = _CHANGESET_RE.match(git("show", f"HEAD:{path}"))
        if not m:
            continue
        packages = len(_RELEASE_RE.findall(m.group(1)))
        summary = m.group(2).strip()
        if packages and summary:
            result.append((summary, packages))
    return result


def render_highlight(summary: str, packages: int) -> str:
    """Render a changeset as a list item with its body indented under the first
    line, as @changesets/changelog-git does in the service changelogs.

    The indent also stops a body line from starting a `## ` section, which the
    release tooling splits the root changelog on.
    """
    first, *rest = summary.splitlines()
    noun = "package" if packages == 1 else "packages"
    return "\n".join([f"- {first} ({packages} {noun})"] + [f"  {line}".rstrip() for line in rest])


def generate_root_changelog(
    changed_packages: Dict[str, str],
    changelog_path: Path,
    release_date: str,
    highlights: Sequence[Tuple[str, int]] = (),
) -> None:
    header = "# AWS SDK for Python - Releases\n\n"
    existing = ""
    if changelog_path.exists():
        existing = changelog_path.read_text()
        if existing.startswith(header):
            existing = existing[len(header):]

    section = f"## {release_date}\n\n"
    if highlights:
        section += "### Highlights\n\n"
        section += "\n".join(render_highlight(s, n) for s, n in highlights)
        section += "\n\n### Packages\n\n"
    for service in sorted(changed_packages):
        version = changed_packages[service]
        section += f"- [{pkg_name(service)} v{version}](services/{service}/CHANGELOG.md)\n"
    section += "\n"

    changelog_path.write_text(header + section + existing)


def main() -> None:
    changed = changed_services(REPO_ROOT)
    if not changed:
        print("No package version changes detected")
        return
    print(f"Aggregating changelog for {len(changed)} changed packages...")
    generate_root_changelog(
        changed, REPO_ROOT / "CHANGELOG.md", date.today().isoformat(), consumed_changesets(REPO_ROOT),
    )
    print("✓ Root changelog updated")


if __name__ == "__main__":
    main()

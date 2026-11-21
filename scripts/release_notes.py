#!/usr/bin/env python3
"""Build GitHub release notes for the latest root CHANGELOG.md section.

Reads the top (most recent) section of the root changelog, leads with its
highlights, expands each released package's entry with that version's section
from the service changelog, writes the notes body to the given path, and prints
the release date (the section heading) to stdout.

Usage: release_notes.py <output-file>
"""

import os
import re
import sys
from pathlib import Path

from changeset_paths import REPO_ROOT

_ENTRY_RE = re.compile(
    r"\[(?P<pkg>\S+) v(?P<version>\S+)\]\(services/(?P<service>[^/]+)/CHANGELOG\.md\)"
)
# Written by aggregate_changelog.py; highlight bodies are indented, so neither
# heading can occur inside one.
_HIGHLIGHTS_RE = re.compile(r"^### Highlights\n(.*?)^### Packages$", re.MULTILINE | re.DOTALL)

# GitHub caps release bodies at 125k characters; fall back to links past this.
_MAX_BODY = 120_000


def version_section(changelog: Path, version: str) -> str:
    """Return the body of the `## <version>` section, or "" if not found."""
    if not changelog.exists():
        return ""
    for section in changelog.read_text().split("\n## ")[1:]:
        head, _, body = section.partition("\n")
        if head.strip() == version:
            return body.strip()
    return ""


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1])

    sections = (REPO_ROOT / "CHANGELOG.md").read_text().split("\n## ")
    if len(sections) < 2:
        sys.exit("root CHANGELOG.md has no release sections")
    date, _, index = sections[1].partition("\n")
    entries = [m.groupdict() for m in _ENTRY_RE.finditer(index)]
    if not entries:
        sys.exit("no package entries in the latest changelog section")

    repo = os.environ.get("GITHUB_REPOSITORY", "")
    links = "\n".join(
        f"- [{e['pkg']} v{e['version']}]"
        f"(https://github.com/{repo}/blob/main/services/{e['service']}/CHANGELOG.md)"
        for e in entries
    )

    parts = []
    for e in entries:
        changelog = REPO_ROOT / "services" / e["service"] / "CHANGELOG.md"
        body = version_section(changelog, e["version"])
        parts.append(f"## {e['pkg']} v{e['version']}\n\n{body}".strip())
    m = _HIGHLIGHTS_RE.search(index)
    highlights = f"## Highlights\n\n{m.group(1).strip()}\n\n" if m else ""
    notes = highlights + "\n\n".join(parts)

    if len(notes) > _MAX_BODY:
        notes = f"{highlights}Released {len(entries)} packages:\n\n{links}"

    out.write_text(notes + "\n")
    print(date.strip())


if __name__ == "__main__":
    main()

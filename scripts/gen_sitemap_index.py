#!/usr/bin/env python3
"""Generate the sitemap index of capo-sdk.dev, which robots.txt points to.

The main site and every service site are built separately, each with its own
`sitemap.xml`; the index lists them all. Services without a `zensical.toml`
have no site and are left out, as in docs/services.md.

Usage: gen_sitemap_index.py <output path>
"""

import sys
from pathlib import Path

from changeset_paths import SERVICES_DIR

SITE = "https://capo-sdk.dev"


def sitemap_index(services: list[str]) -> str:
    urls = [f"{SITE}/sitemap.xml", *(f"{SITE}/services/{s}/sitemap.xml" for s in services)]
    entries = "".join(f"  <sitemap>\n    <loc>{url}</loc>\n  </sitemap>\n" for url in urls)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}"
        "</sitemapindex>\n"
    )


def main() -> None:
    services = sorted(p.parent.name for p in SERVICES_DIR.glob("*/zensical.toml"))
    Path(sys.argv[1]).write_text(sitemap_index(services))
    print(f"Wrote a sitemap index of {len(services)} services to {sys.argv[1]}")


if __name__ == "__main__":
    main()

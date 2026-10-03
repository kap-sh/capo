#!/usr/bin/env python3
"""Generate docs/services.md, the index of per-service documentation sites.

Every service with a `zensical.toml` has its own site at
`https://<service>.capo-sdk.dev`. Services without one are left out, so the
index never links to a site that does not exist.
"""

import re
from typing import List

from changeset_paths import REPO_ROOT, SERVICES_DIR

_DESCRIPTION_RE = re.compile(r'^description\s*=\s*"Python SDK for (.+)\."', re.MULTILINE)

# The services most commonly accessed through an SDK, listed first and in this
# order so they are not buried in the alphabetical list of every service.
POPULAR = [
    "s3",
    "ec2",
    "lambda",
    "dynamodb",
    "iam",
    "sts",
    "sqs",
    "sns",
    "rds",
    "secrets-manager",
    "ssm",
    "kms",
    "cloudwatch",
    "cloudwatch-logs",
    "ecs",
    "eks",
    "ecr",
    "cloudformation",
    "bedrock-runtime",
    "sesv2",
    "eventbridge",
    "sfn",
    "kinesis",
    "athena",
    "glue",
    "cognito-identity-provider",
    "api-gateway",
    "elastic-load-balancing-v2",
    "route-53",
    "cloudfront",
]

HEADER = """\
# Services

Every service is a standalone package with its own documentation site: the
API reference of its clients, operations, paginators, waiters, types and
errors.
"""

TABLE_HEADER = """\
| Service | Package | Documentation |
| --- | --- | --- |
"""


def table(services: List[str]) -> str:
    rows = []
    for service in services:
        pyproject = SERVICES_DIR / service / "pyproject.toml"
        m = _DESCRIPTION_RE.search(pyproject.read_text())
        if not m:
            raise ValueError(f"no description in {pyproject}")
        host = f"{service}.capo-sdk.dev"
        rows.append(f"| {m.group(1)} | `capo-{service}` | [{host}](https://{host}) |\n")
    return TABLE_HEADER + "".join(rows)


def main() -> None:
    documented = sorted(p.parent.name for p in SERVICES_DIR.glob("*/zensical.toml"))
    unknown = [s for s in POPULAR if not (SERVICES_DIR / s).is_dir()]
    if unknown:
        raise ValueError(f"no such services in POPULAR: {unknown}")
    popular = [s for s in POPULAR if s in documented]

    text = HEADER
    if popular:
        text += "\n## Popular services\n\n" + table(popular)
    text += "\n## All services\n\n" + table(documented)
    (REPO_ROOT / "docs" / "services.md").write_text(text)


if __name__ == "__main__":
    main()

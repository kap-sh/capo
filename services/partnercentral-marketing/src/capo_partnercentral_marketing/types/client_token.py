"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ClientToken``."""

from typing import TypeAlias

"""Idempotency token for mutating operations. <p>Printable ASCII 33-126 — no spaces, no control characters — per the AWS Idempotency Standard. Never `@required`: a caller that does not need replay protection omits it."""
ClientToken: TypeAlias = str

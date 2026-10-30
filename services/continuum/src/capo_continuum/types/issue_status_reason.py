"""Generated from Smithy shape ``com.amazonaws.continuum#IssueStatusReason``."""

from typing import Literal, TypeAlias, cast

"""Why an issue is FAILED. Present only when `status` is FAILED."""
IssueStatusReason: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "REMEDIATION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssueStatusReason) -> str:
    return value


def deserialize_json(data: str) -> IssueStatusReason:
    return cast(IssueStatusReason, data)

"""Generated from Smithy shape ``com.amazonaws.continuum#IssueStatus``."""

from typing import Literal, TypeAlias, cast

"""The customer-facing lifecycle status of an issue. Coarse by design: `phase` says which part of Continuum's workflow an IN_PROGRESS (or FAILED) issue is in, and `statusReason` says why a FAILED issue failed. Distinct from FindingStatus. Continuum sets this value; callers can't set it."""
IssueStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssueStatus) -> str:
    return value


def deserialize_json(data: str) -> IssueStatus:
    return cast(IssueStatus, data)

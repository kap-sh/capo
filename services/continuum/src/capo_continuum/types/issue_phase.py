"""Generated from Smithy shape ``com.amazonaws.continuum#IssuePhase``."""

from typing import Literal, TypeAlias, cast

"""The part of Continuum's workflow an issue is in (IN_PROGRESS) or failed in (FAILED, when known)."""
IssuePhase: TypeAlias = Literal[
    "VALIDATION",
    "PRIORITIZATION",
    "REMEDIATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssuePhase) -> str:
    return value


def deserialize_json(data: str) -> IssuePhase:
    return cast(IssuePhase, data)

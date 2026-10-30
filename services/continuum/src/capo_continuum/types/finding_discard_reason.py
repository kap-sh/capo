"""Generated from Smithy shape ``com.amazonaws.continuum#FindingDiscardReason``."""

from typing import Literal, TypeAlias, cast

"""Why a finding was not escalated into an issue. Present only when status is DISCARDED."""
FindingDiscardReason: TypeAlias = Literal[
    "SCANNER_VALIDATED_FALSE_POSITIVE",
    "SCANNER_NEEDS_REVIEW",
    "FALSE_POSITIVE_VALIDATED_AGAINST_CONTEXT",
    "DUPLICATE_OF_OPEN_ISSUE",
    "DUPLICATE_OF_CLOSED_ISSUE",
    "COMPENSATING_CONTROL_PRESENT",
    "OUT_OF_SCOPE",
    "INSUFFICIENT_EVIDENCE",
    "PROCESSING_FAILED",
    "SOURCE_REPO_NOT_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingDiscardReason) -> str:
    return value


def deserialize_json(data: str) -> FindingDiscardReason:
    return cast(FindingDiscardReason, data)

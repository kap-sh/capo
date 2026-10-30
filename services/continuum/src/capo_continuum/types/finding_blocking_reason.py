"""Generated from Smithy shape ``com.amazonaws.continuum#FindingBlockingReason``."""

from typing import Literal, TypeAlias, cast

"""Why a validator rejected a finding. NONE accompanies a true positive."""
FindingBlockingReason: TypeAlias = Literal[
    "UNREACHABLE",
    "PROTECTED",
    "MISCLASSIFIED",
    "EXCLUDED",
    "NOT_FEASIBLE",
    "RISK_MITIGATED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingBlockingReason) -> str:
    return value


def deserialize_json(data: str) -> FindingBlockingReason:
    return cast(FindingBlockingReason, data)

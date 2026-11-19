"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationType``."""

from typing import Literal, TypeAlias, cast

InvestigationType: TypeAlias = Literal[
    "FINDING",
    "ACCOUNT",
    "ORGANIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationType) -> str:
    return value


def deserialize_json(data: str) -> InvestigationType:
    return cast(InvestigationType, data)

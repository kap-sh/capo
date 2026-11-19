"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationIndicatorType``."""

from typing import Literal, TypeAlias, cast

InvestigationIndicatorType: TypeAlias = Literal[
    "IP",
    "DOMAIN",
    "FILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationIndicatorType) -> str:
    return value


def deserialize_json(data: str) -> InvestigationIndicatorType:
    return cast(InvestigationIndicatorType, data)

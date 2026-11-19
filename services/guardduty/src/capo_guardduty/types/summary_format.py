"""Generated from Smithy shape ``com.amazonaws.guardduty#SummaryFormat``."""

from typing import Literal, TypeAlias, cast

SummaryFormat: TypeAlias = Literal[
    "STRING",
    "STRUCTURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryFormat) -> str:
    return value


def deserialize_json(data: str) -> SummaryFormat:
    return cast(SummaryFormat, data)

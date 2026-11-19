"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchVerdict``."""

from typing import Literal, TypeAlias, cast

FetchVerdict: TypeAlias = Literal[
    "THREAT",
    "BENIGN",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FetchVerdict) -> str:
    return value


def deserialize_json(data: str) -> FetchVerdict:
    return cast(FetchVerdict, data)

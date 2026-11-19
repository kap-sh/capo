"""Generated from Smithy shape ``com.amazonaws.guardduty#DefenseTactic``."""

from typing import Literal, TypeAlias, cast

DefenseTactic: TypeAlias = Literal[
    "Isolate",
    "Evict",
    "Restore",
    "Harden",
    "Detect",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefenseTactic) -> str:
    return value


def deserialize_json(data: str) -> DefenseTactic:
    return cast(DefenseTactic, data)

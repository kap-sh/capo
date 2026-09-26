"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RuleType``."""

from typing import Literal, TypeAlias, cast

RuleType: TypeAlias = Literal[
    "CONFIGURATION",
    "INSPECTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    return cast(RuleType, data)

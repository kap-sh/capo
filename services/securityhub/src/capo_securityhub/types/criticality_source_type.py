"""Generated from Smithy shape ``com.amazonaws.securityhub#CriticalitySourceType``."""

from typing import Literal, TypeAlias, cast

CriticalitySourceType: TypeAlias = Literal[
    "AutomationRule",
    "ResourceName",
    "TagInference",
]


# --- restJson1 ser/de ---
def serialize_json(value: CriticalitySourceType) -> str:
    return value


def deserialize_json(data: str) -> CriticalitySourceType:
    return cast(CriticalitySourceType, data)

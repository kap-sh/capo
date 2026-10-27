"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatGatewaySupportValue``."""

from typing import Literal, TypeAlias, cast

NatGatewaySupportValue: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NatGatewaySupportValue) -> str:
    return value


def deserialize_json(data: str) -> NatGatewaySupportValue:
    return cast(NatGatewaySupportValue, data)

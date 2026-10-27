"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatGatewaySupportState``."""

from typing import Literal, TypeAlias, cast

NatGatewaySupportState: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DISABLED",
    "DISABLING",
    "PENDING_ATTACHMENT_ACCEPTANCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NatGatewaySupportState) -> str:
    return value


def deserialize_json(data: str) -> NatGatewaySupportState:
    return cast(NatGatewaySupportState, data)

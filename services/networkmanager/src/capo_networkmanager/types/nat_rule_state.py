"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatRuleState``."""

from typing import Literal, TypeAlias, cast

NatRuleState: TypeAlias = Literal[
    "CREATING",
    "MODIFYING",
    "DELETING",
    "ACTIVATED",
    "ACTIVATING",
    "DEACTIVATED",
    "DEACTIVATING",
    "FAILED",
    "PENDING_ATTACHMENT_ACCEPTANCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NatRuleState) -> str:
    return value


def deserialize_json(data: str) -> NatRuleState:
    return cast(NatRuleState, data)

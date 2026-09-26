"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AutoApprovalRule``."""

from typing import Literal, TypeAlias, cast

AutoApprovalRule: TypeAlias = Literal["APPROVE_ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: AutoApprovalRule) -> str:
    return value


def deserialize_json(data: str) -> AutoApprovalRule:
    return cast(AutoApprovalRule, data)

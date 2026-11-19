"""Generated from Smithy shape ``com.amazonaws.guardduty#ActionPriority``."""

from typing import Literal, TypeAlias, cast

ActionPriority: TypeAlias = Literal[
    "IMMEDIATE",
    "SHORT_TERM",
    "STRATEGIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionPriority) -> str:
    return value


def deserialize_json(data: str) -> ActionPriority:
    return cast(ActionPriority, data)

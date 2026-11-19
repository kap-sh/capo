"""Generated from Smithy shape ``com.amazonaws.connecthealth#ChecklistItemStatus``."""

from typing import Literal, TypeAlias, cast

ChecklistItemStatus: TypeAlias = Literal[
    "DISCUSSED",
    "PARTIALLY_DISCUSSED",
    "NOT_DISCUSSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChecklistItemStatus) -> str:
    return value


def deserialize_json(data: str) -> ChecklistItemStatus:
    return cast(ChecklistItemStatus, data)

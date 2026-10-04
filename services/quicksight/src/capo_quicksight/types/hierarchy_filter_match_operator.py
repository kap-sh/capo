"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterMatchOperator``."""

from typing import Literal, TypeAlias, cast

HierarchyFilterMatchOperator: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> HierarchyFilterMatchOperator:
    return cast(HierarchyFilterMatchOperator, data)

"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyValuesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.hierarchy_filter_value

HierarchyValuesList: TypeAlias = list[
    "capo_quicksight.types.hierarchy_filter_value.HierarchyFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> HierarchyValuesList:
    return [item for item in data if item is not None]


def redact_sensitive(value: HierarchyValuesList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

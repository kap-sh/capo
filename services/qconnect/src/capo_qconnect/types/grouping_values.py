"""Generated from Smithy shape ``com.amazonaws.qconnect#GroupingValues``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.grouping_value

GroupingValues: TypeAlias = list["capo_qconnect.types.grouping_value.GroupingValue"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingValues) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupingValues:
    return [item for item in data if item is not None]


def redact_sensitive(value: GroupingValues) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

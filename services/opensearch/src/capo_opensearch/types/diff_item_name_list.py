"""Generated from Smithy shape ``com.amazonaws.opensearch#DiffItemNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.diff_item_name

DiffItemNameList: TypeAlias = list["capo_opensearch.types.diff_item_name.DiffItemName"]


# --- restJson1 ser/de ---
def serialize_json(value: DiffItemNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> DiffItemNameList:
    return [item for item in data if item is not None]

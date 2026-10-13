"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInventoryResultItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.search_inventory_result_item

SearchInventoryResultItems: TypeAlias = list[
    "capo_datazone.types.search_inventory_result_item.SearchInventoryResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchInventoryResultItems) -> list:
    import capo_datazone.types.search_inventory_result_item

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.search_inventory_result_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchInventoryResultItems:
    import capo_datazone.types.search_inventory_result_item

    out: SearchInventoryResultItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_datazone.types.search_inventory_result_item.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SearchInventoryResultItems) -> list[Any]:
    import capo_datazone.types.search_inventory_result_item

    return [
        capo_datazone.types.search_inventory_result_item.redact_sensitive(item)
        for item in value
    ]

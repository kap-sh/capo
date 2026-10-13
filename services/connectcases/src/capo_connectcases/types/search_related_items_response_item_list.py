"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchRelatedItemsResponseItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.search_related_items_response_item

SearchRelatedItemsResponseItemList: TypeAlias = list[
    "capo_connectcases.types.search_related_items_response_item.SearchRelatedItemsResponseItem | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelatedItemsResponseItemList) -> list:
    import capo_connectcases.types.search_related_items_response_item

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(
            capo_connectcases.types.search_related_items_response_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchRelatedItemsResponseItemList:
    import capo_connectcases.types.search_related_items_response_item

    out: SearchRelatedItemsResponseItemList = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(
            capo_connectcases.types.search_related_items_response_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SearchRelatedItemsResponseItemList) -> list[Any]:
    import capo_connectcases.types.search_related_items_response_item

    return [
        None
        if item is None
        else capo_connectcases.types.search_related_items_response_item.redact_sensitive(
            item
        )
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsResponseItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.search_all_related_items_response_item

SearchAllRelatedItemsResponseItemList: TypeAlias = list[
    "capo_connectcases.types.search_all_related_items_response_item.SearchAllRelatedItemsResponseItem | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsResponseItemList) -> list:
    import capo_connectcases.types.search_all_related_items_response_item

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(
            capo_connectcases.types.search_all_related_items_response_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchAllRelatedItemsResponseItemList:
    import capo_connectcases.types.search_all_related_items_response_item

    out: SearchAllRelatedItemsResponseItemList = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(
            capo_connectcases.types.search_all_related_items_response_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SearchAllRelatedItemsResponseItemList) -> list[Any]:
    import capo_connectcases.types.search_all_related_items_response_item

    return [
        None
        if item is None
        else capo_connectcases.types.search_all_related_items_response_item.redact_sensitive(
            item
        )
        for item in value
    ]

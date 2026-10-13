"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextResultItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.search_text_result_item

SearchTextResultItemList: TypeAlias = list[
    "capo_geo_places.types.search_text_result_item.SearchTextResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextResultItemList) -> list:
    import capo_geo_places.types.search_text_result_item

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.search_text_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchTextResultItemList:
    import capo_geo_places.types.search_text_result_item

    out: SearchTextResultItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.search_text_result_item.deserialize_json(item))
    return out


def redact_sensitive(value: SearchTextResultItemList) -> list[Any]:
    import capo_geo_places.types.search_text_result_item

    return [
        capo_geo_places.types.search_text_result_item.redact_sensitive(item)
        for item in value
    ]

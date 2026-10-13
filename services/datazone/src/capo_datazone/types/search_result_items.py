"""Generated from Smithy shape ``com.amazonaws.datazone#SearchResultItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.search_result_item

SearchResultItems: TypeAlias = list[
    "capo_datazone.types.search_result_item.SearchResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultItems) -> list:
    import capo_datazone.types.search_result_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.search_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchResultItems:
    import capo_datazone.types.search_result_item

    out: SearchResultItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.search_result_item.deserialize_json(item))
    return out


def redact_sensitive(value: SearchResultItems) -> list[Any]:
    import capo_datazone.types.search_result_item

    return [
        capo_datazone.types.search_result_item.redact_sensitive(item) for item in value
    ]

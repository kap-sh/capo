"""Generated from Smithy shape ``com.amazonaws.datazone#SearchTypesResultItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.search_types_result_item

SearchTypesResultItems: TypeAlias = list[
    "capo_datazone.types.search_types_result_item.SearchTypesResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypesResultItems) -> list:
    import capo_datazone.types.search_types_result_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.search_types_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchTypesResultItems:
    import capo_datazone.types.search_types_result_item

    out: SearchTypesResultItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.search_types_result_item.deserialize_json(item))
    return out


def redact_sensitive(value: SearchTypesResultItems) -> list[Any]:
    import capo_datazone.types.search_types_result_item

    return [
        capo_datazone.types.search_types_result_item.redact_sensitive(item)
        for item in value
    ]

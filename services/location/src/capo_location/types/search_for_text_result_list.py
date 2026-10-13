"""Generated from Smithy shape ``com.amazonaws.location#SearchForTextResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.search_for_text_result

SearchForTextResultList: TypeAlias = list[
    "capo_location.types.search_for_text_result.SearchForTextResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchForTextResultList) -> list:
    import capo_location.types.search_for_text_result

    out: list = []
    for item in value:
        out.append(capo_location.types.search_for_text_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchForTextResultList:
    import capo_location.types.search_for_text_result

    out: SearchForTextResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.search_for_text_result.deserialize_json(item))
    return out


def redact_sensitive(value: SearchForTextResultList) -> list[Any]:
    import capo_location.types.search_for_text_result

    return [
        capo_location.types.search_for_text_result.redact_sensitive(item)
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.location#SearchForSuggestionsResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.search_for_suggestions_result

SearchForSuggestionsResultList: TypeAlias = list[
    "capo_location.types.search_for_suggestions_result.SearchForSuggestionsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchForSuggestionsResultList) -> list:
    import capo_location.types.search_for_suggestions_result

    out: list = []
    for item in value:
        out.append(
            capo_location.types.search_for_suggestions_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchForSuggestionsResultList:
    import capo_location.types.search_for_suggestions_result

    out: SearchForSuggestionsResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.search_for_suggestions_result.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SearchForSuggestionsResultList) -> list[Any]:
    import capo_location.types.search_for_suggestions_result

    return [
        capo_location.types.search_for_suggestions_result.redact_sensitive(item)
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForSuggestionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.search_for_suggestions_result_list
    import capo_location.types.search_place_index_for_suggestions_summary


class SearchPlaceIndexForSuggestionsResponse(TypedDict, closed=True):
    summary: "capo_location.types.search_place_index_for_suggestions_summary.SearchPlaceIndexForSuggestionsSummary"
    """<p>Contains a summary of the request. Echoes the input values for <code>BiasPosition</code>, <code>FilterBBox</code>, <code>FilterCountries</code>, <code>Language</code>, <code>MaxResults</code>, and <code>Text</code>. Also includes the <code>DataSource</code> of the place index. </p>"""
    results: "capo_location.types.search_for_suggestions_result_list.SearchForSuggestionsResultList"
    """<p>A list of place suggestions that best match the search text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForSuggestionsResponse) -> dict:
    out: dict = {}
    import capo_location.types.search_place_index_for_suggestions_summary

    out["Summary"] = (
        capo_location.types.search_place_index_for_suggestions_summary.serialize_json(
            value["summary"]
        )
    )
    import capo_location.types.search_for_suggestions_result_list

    out["Results"] = (
        capo_location.types.search_for_suggestions_result_list.serialize_json(
            value["results"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForSuggestionsResponse:
    out: SearchPlaceIndexForSuggestionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Summary") is not None:
        import capo_location.types.search_place_index_for_suggestions_summary

        out["summary"] = (
            capo_location.types.search_place_index_for_suggestions_summary.deserialize_json(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForSuggestionsResponse.summary required"
        )
    if data.get("Results") is not None:
        import capo_location.types.search_for_suggestions_result_list

        out["results"] = (
            capo_location.types.search_for_suggestions_result_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        out["results"] = []
    return out


def redact_sensitive(value: SearchPlaceIndexForSuggestionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "summary" in value:
        import capo_location.types.search_place_index_for_suggestions_summary

        out["summary"] = (
            capo_location.types.search_place_index_for_suggestions_summary.redact_sensitive(
                value["summary"]
            )
        )
    if "results" in value:
        import capo_location.types.search_for_suggestions_result_list

        out["results"] = (
            capo_location.types.search_for_suggestions_result_list.redact_sensitive(
                value["results"]
            )
        )
    return out

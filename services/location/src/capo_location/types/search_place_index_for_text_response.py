"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForTextResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.search_for_text_result_list
    import capo_location.types.search_place_index_for_text_summary


class SearchPlaceIndexForTextResponse(TypedDict, closed=True):
    summary: "capo_location.types.search_place_index_for_text_summary.SearchPlaceIndexForTextSummary"
    """<p>Contains a summary of the request. Echoes the input values for <code>BiasPosition</code>, <code>FilterBBox</code>, <code>FilterCountries</code>, <code>Language</code>, <code>MaxResults</code>, and <code>Text</code>. Also includes the <code>DataSource</code> of the place index and the bounding box, <code>ResultBBox</code>, which surrounds the search results. </p>"""
    results: "capo_location.types.search_for_text_result_list.SearchForTextResultList"
    """<p>A list of Places matching the input text. Each result contains additional information about the specific point of interest. </p> <p>Not all response properties are included with all responses. Some properties may only be returned by specific data partners.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForTextResponse) -> dict:
    out: dict = {}
    import capo_location.types.search_place_index_for_text_summary

    out["Summary"] = (
        capo_location.types.search_place_index_for_text_summary.serialize_json(
            value["summary"]
        )
    )
    import capo_location.types.search_for_text_result_list

    out["Results"] = capo_location.types.search_for_text_result_list.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForTextResponse:
    out: SearchPlaceIndexForTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("Summary") is not None:
        import capo_location.types.search_place_index_for_text_summary

        out["summary"] = (
            capo_location.types.search_place_index_for_text_summary.deserialize_json(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError("SearchPlaceIndexForTextResponse.summary required")
    if data.get("Results") is not None:
        import capo_location.types.search_for_text_result_list

        out["results"] = (
            capo_location.types.search_for_text_result_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        out["results"] = []
    return out


def redact_sensitive(value: SearchPlaceIndexForTextResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "summary" in value:
        import capo_location.types.search_place_index_for_text_summary

        out["summary"] = (
            capo_location.types.search_place_index_for_text_summary.redact_sensitive(
                value["summary"]
            )
        )
    if "results" in value:
        import capo_location.types.search_for_text_result_list

        out["results"] = (
            capo_location.types.search_for_text_result_list.redact_sensitive(
                value["results"]
            )
        )
    return out

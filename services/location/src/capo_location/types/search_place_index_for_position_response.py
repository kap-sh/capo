"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForPositionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.search_for_position_result_list
    import capo_location.types.search_place_index_for_position_summary


class SearchPlaceIndexForPositionResponse(TypedDict, closed=True):
    summary: "capo_location.types.search_place_index_for_position_summary.SearchPlaceIndexForPositionSummary"
    """<p>Contains a summary of the request. Echoes the input values for <code>Position</code>, <code>Language</code>, <code>MaxResults</code>, and the <code>DataSource</code> of the place index. </p>"""
    results: "capo_location.types.search_for_position_result_list.SearchForPositionResultList"
    """<p>Returns a list of Places closest to the specified position. Each result contains additional information about the Places returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForPositionResponse) -> dict:
    out: dict = {}
    import capo_location.types.search_place_index_for_position_summary

    out["Summary"] = (
        capo_location.types.search_place_index_for_position_summary.serialize_json(
            value["summary"]
        )
    )
    import capo_location.types.search_for_position_result_list

    out["Results"] = capo_location.types.search_for_position_result_list.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForPositionResponse:
    out: SearchPlaceIndexForPositionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Summary") is not None:
        import capo_location.types.search_place_index_for_position_summary

        out["summary"] = (
            capo_location.types.search_place_index_for_position_summary.deserialize_json(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionResponse.summary required"
        )
    if data.get("Results") is not None:
        import capo_location.types.search_for_position_result_list

        out["results"] = (
            capo_location.types.search_for_position_result_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionResponse.results required"
        )
    return out


def redact_sensitive(value: SearchPlaceIndexForPositionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "summary" in value:
        import capo_location.types.search_place_index_for_position_summary

        out["summary"] = (
            capo_location.types.search_place_index_for_position_summary.redact_sensitive(
                value["summary"]
            )
        )
    if "results" in value:
        import capo_location.types.search_for_position_result_list

        out["results"] = (
            capo_location.types.search_for_position_result_list.redact_sensitive(
                value["results"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchQuickResponsesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.quick_response_search_results_list


class SearchQuickResponsesResponse(TypedDict, closed=True):
    results: "capo_wisdom.types.quick_response_search_results_list.QuickResponseSearchResultsList"
    """<p>The results of the quick response search.</p>"""
    next_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuickResponsesResponse) -> dict:
    out: dict = {}
    import capo_wisdom.types.quick_response_search_results_list

    out["results"] = (
        capo_wisdom.types.quick_response_search_results_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchQuickResponsesResponse:
    out: SearchQuickResponsesResponse = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_wisdom.types.quick_response_search_results_list

        out["results"] = (
            capo_wisdom.types.quick_response_search_results_list.deserialize_json(
                data["results"]
            )
        )
    else:
        raise DeserializationError("SearchQuickResponsesResponse.results required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchQuickResponsesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_wisdom.types.quick_response_search_results_list

        out["results"] = (
            capo_wisdom.types.quick_response_search_results_list.redact_sensitive(
                value["results"]
            )
        )
    return out

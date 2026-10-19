"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchSpacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.next_token
    import capo_quicksight.types.space_quicksight_search_filters
    import capo_quicksight.types.spaces_max_results


class SearchSpacesRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the spaces.</p>"""
    next_token: NotRequired["capo_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired[
        "capo_quicksight.types.spaces_max_results.SpacesMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""
    filters: "capo_quicksight.types.space_quicksight_search_filters.SpaceQuicksightSearchFilters"
    """<p>The filters to apply to the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpacesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    import capo_quicksight.types.space_quicksight_search_filters

    out["Filters"] = (
        capo_quicksight.types.space_quicksight_search_filters.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchSpacesRequest:
    out: SearchSpacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_quicksight.types.space_quicksight_search_filters

        out["filters"] = (
            capo_quicksight.types.space_quicksight_search_filters.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchSpacesRequest.filters required")
    return out

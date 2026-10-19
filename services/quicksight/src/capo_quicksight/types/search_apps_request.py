"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAppsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.next_token
    import capo_quicksight.types.search_apps_filter_list


class SearchAppsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the apps to search.</p>"""
    filters: "capo_quicksight.types.search_apps_filter_list.SearchAppsFilterList"
    """<p>The filters to apply to the search.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single request. Valid range is 1 to 100. If you don't specify a value, the default is 20.</p>"""
    next_token: NotRequired["capo_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAppsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.search_apps_filter_list

    out["Filters"] = capo_quicksight.types.search_apps_filter_list.serialize_json(
        value["filters"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchAppsRequest:
    out: SearchAppsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_quicksight.types.search_apps_filter_list

        out["filters"] = capo_quicksight.types.search_apps_filter_list.deserialize_json(
            data["Filters"]
        )
    else:
        out["filters"] = []
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

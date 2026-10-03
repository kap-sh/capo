"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchDashboardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.dashboard_search_filter_list
    import capo_quicksight.types.max_results
    import capo_quicksight.types.string


class SearchDashboardsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the user whose dashboards you're searching for. </p>"""
    filters: (
        "capo_quicksight.types.dashboard_search_filter_list.DashboardSearchFilterList"
    )
    """<p>The filters to apply to the search. Currently, you can search only by user name, for example, <code>"Filters": [ { "Name": "QUICKSIGHT_USER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1" } ]</code> </p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDashboardsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.dashboard_search_filter_list

    out["Filters"] = capo_quicksight.types.dashboard_search_filter_list.serialize_json(
        value["filters"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchDashboardsRequest:
    out: SearchDashboardsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_quicksight.types.dashboard_search_filter_list

        out["filters"] = (
            capo_quicksight.types.dashboard_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchDashboardsRequest.filters required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out

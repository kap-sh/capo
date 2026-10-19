"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListAnomalousLogGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_id
    import capo_devops_guru.types.list_anomalous_log_groups_max_results
    import capo_devops_guru.types.uuid_next_token


class ListAnomalousLogGroupsRequest(TypedDict, closed=True):
    insight_id: "capo_devops_guru.types.insight_id.InsightId"
    """<p> The ID of the insight containing the log groups. </p>"""
    max_results: NotRequired[
        "capo_devops_guru.types.list_anomalous_log_groups_max_results.ListAnomalousLogGroupsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomalousLogGroupsRequest) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnomalousLogGroupsRequest:
    out: ListAnomalousLogGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

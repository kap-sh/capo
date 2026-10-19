"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeFlowExecutionRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.flow_name
    import capo_appflow.types.max_results
    import capo_appflow.types.next_token


class DescribeFlowExecutionRecordsRequest(TypedDict, closed=True):
    flow_name: "capo_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    max_results: NotRequired["capo_appflow.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations). </p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowExecutionRecordsRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeFlowExecutionRecordsRequest:
    out: DescribeFlowExecutionRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

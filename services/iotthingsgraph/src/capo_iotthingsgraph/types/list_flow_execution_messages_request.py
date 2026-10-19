"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#ListFlowExecutionMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_id
    import capo_iotthingsgraph.types.max_results
    import capo_iotthingsgraph.types.next_token


class ListFlowExecutionMessagesRequest(TypedDict, closed=True):
    flow_execution_id: "capo_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
    """<p>The ID of the flow execution.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["capo_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlowExecutionMessagesRequest) -> dict:
    out: dict = {}
    out["flowExecutionId"] = value["flow_execution_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlowExecutionMessagesRequest:
    out: ListFlowExecutionMessagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("flowExecutionId") is not None:
        out["flow_execution_id"] = data["flowExecutionId"]
    else:
        out["flow_execution_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

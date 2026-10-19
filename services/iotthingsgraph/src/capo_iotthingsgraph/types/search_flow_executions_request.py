"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchFlowExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_id
    import capo_iotthingsgraph.types.max_results
    import capo_iotthingsgraph.types.next_token
    import capo_iotthingsgraph.types.timestamp
    import capo_iotthingsgraph.types.urn


class SearchFlowExecutionsRequest(TypedDict, closed=True):
    system_instance_id: "capo_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the system instance that contains the flow.</p>"""
    flow_execution_id: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The ID of a flow execution.</p>"""
    start_time: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time of the earliest flow execution to return.</p>"""
    end_time: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time of the latest flow execution to return.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["capo_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFlowExecutionsRequest) -> dict:
    out: dict = {}
    out["systemInstanceId"] = value["system_instance_id"]
    if "flow_execution_id" in value:
        out["flowExecutionId"] = value["flow_execution_id"]
    if "start_time" in value:
        import capo_iotthingsgraph.types.timestamp

        out["startTime"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_iotthingsgraph.types.timestamp

        out["endTime"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFlowExecutionsRequest:
    out: SearchFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("systemInstanceId") is not None:
        out["system_instance_id"] = data["systemInstanceId"]
    else:
        out["system_instance_id"] = ""
    if data.get("flowExecutionId") is not None:
        out["flow_execution_id"] = data["flowExecutionId"]
    if data.get("startTime") is not None:
        import capo_iotthingsgraph.types.timestamp

        out["start_time"] = (
            capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_iotthingsgraph.types.timestamp

        out["end_time"] = capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListEdgeAgentConfigurationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.hub_device_arn
    import capo_kinesis_video.types.list_edge_agent_configurations_input_limit
    import capo_kinesis_video.types.next_token


class ListEdgeAgentConfigurationsInput(TypedDict, closed=True):
    hub_device_arn: "capo_kinesis_video.types.hub_device_arn.HubDeviceArn"
    """<p>The "Internet of Things (IoT) Thing" Arn of the edge agent.</p>"""
    max_results: NotRequired[
        "capo_kinesis_video.types.list_edge_agent_configurations_input_limit.ListEdgeAgentConfigurationsInputLimit"
    ]
    """<p>The maximum number of edge configurations to return in the response. The default is 5.</p>"""
    next_token: NotRequired["capo_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter, when the result of a <code>ListEdgeAgentConfigurations</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of edge configurations, provide this token in your next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEdgeAgentConfigurationsInput) -> dict:
    out: dict = {}
    out["HubDeviceArn"] = value["hub_device_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEdgeAgentConfigurationsInput:
    out: ListEdgeAgentConfigurationsInput = {}  # type: ignore[typeddict-item]
    if data.get("HubDeviceArn") is not None:
        out["hub_device_arn"] = data["HubDeviceArn"]
    else:
        raise DeserializationError(
            "ListEdgeAgentConfigurationsInput.hub_device_arn required"
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

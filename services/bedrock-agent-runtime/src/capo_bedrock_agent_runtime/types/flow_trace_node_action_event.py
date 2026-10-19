"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeActionEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.node_name


class FlowTraceNodeActionEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that called the operation.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the operation was called.</p>"""
    request_id: "str"
    """<p>The ID of the request that the node made to the operation.</p>"""
    service_name: "str"
    """<p>The name of the service that the node called.</p>"""
    operation_name: "str"
    """<p>The name of the operation that the node called.</p>"""
    operation_request: NotRequired["object"]
    """<p>The request payload sent to the downstream service.</p>"""
    operation_response: NotRequired["object"]
    """<p>The response payload received from the downstream service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeActionEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    out["requestId"] = value["request_id"]
    out["serviceName"] = value["service_name"]
    out["operationName"] = value["operation_name"]
    if "operation_request" in value:
        out["operationRequest"] = value["operation_request"]
    if "operation_response" in value:
        out["operationResponse"] = value["operation_response"]
    return out


def deserialize_json(data: dict) -> FlowTraceNodeActionEvent:
    out: FlowTraceNodeActionEvent = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        out["node_name"] = ""
    if data.get("timestamp") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        out["request_id"] = ""
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("operationName") is not None:
        out["operation_name"] = data["operationName"]
    else:
        out["operation_name"] = ""
    if data.get("operationRequest") is not None:
        out["operation_request"] = data["operationRequest"]
    if data.get("operationResponse") is not None:
        out["operation_response"] = data["operationResponse"]
    return out

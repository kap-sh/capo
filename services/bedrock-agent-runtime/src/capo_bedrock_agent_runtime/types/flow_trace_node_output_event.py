"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_fields
    import capo_bedrock_agent_runtime.types.node_name


class FlowTraceNodeOutputEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that yielded the output.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the trace was returned.</p>"""
    fields: "capo_bedrock_agent_runtime.types.flow_trace_node_output_fields.FlowTraceNodeOutputFields"
    """<p>An array of objects containing information about each field in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_fields

    out["fields"] = (
        capo_bedrock_agent_runtime.types.flow_trace_node_output_fields.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeOutputEvent:
    out: FlowTraceNodeOutputEvent = {}  # type: ignore[typeddict-item]
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
    if data.get("fields") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_output_fields

        out["fields"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_output_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = []
    return out

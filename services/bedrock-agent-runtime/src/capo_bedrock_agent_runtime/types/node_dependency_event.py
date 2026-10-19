"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeDependencyEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.node_name
    import capo_bedrock_agent_runtime.types.node_trace_elements


class NodeDependencyEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that generated the dependency trace.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the dependency trace was generated.</p>"""
    trace_elements: (
        "capo_bedrock_agent_runtime.types.node_trace_elements.NodeTraceElements"
    )
    """<p>The trace elements containing detailed information about the node execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeDependencyEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.node_trace_elements

    out["traceElements"] = (
        capo_bedrock_agent_runtime.types.node_trace_elements.serialize_json(
            value["trace_elements"]
        )
    )
    return out


def deserialize_json(data: dict) -> NodeDependencyEvent:
    out: NodeDependencyEvent = {}  # type: ignore[typeddict-item]
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
    if data.get("traceElements") is not None:
        import capo_bedrock_agent_runtime.types.node_trace_elements

        out["trace_elements"] = (
            capo_bedrock_agent_runtime.types.node_trace_elements.deserialize_json(
                data["traceElements"]
            )
        )
    else:
        import capo_bedrock_agent_runtime.types._unknown

        out["trace_elements"] = (
            capo_bedrock_agent_runtime.types._unknown.UnknownUnionMember("")
        )
    return out

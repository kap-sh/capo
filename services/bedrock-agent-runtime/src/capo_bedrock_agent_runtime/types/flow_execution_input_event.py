"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionInputEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.flow_input_fields
    import capo_bedrock_agent_runtime.types.node_name


class FlowExecutionInputEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that receives the inputs.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the inputs are provided.</p>"""
    fields: "capo_bedrock_agent_runtime.types.flow_input_fields.FlowInputFields"
    """<p>A list of input fields provided to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionInputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.flow_input_fields

    out["fields"] = capo_bedrock_agent_runtime.types.flow_input_fields.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> FlowExecutionInputEvent:
    out: FlowExecutionInputEvent = {}  # type: ignore[typeddict-item]
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
        import capo_bedrock_agent_runtime.types.flow_input_fields

        out["fields"] = (
            capo_bedrock_agent_runtime.types.flow_input_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = []
    return out

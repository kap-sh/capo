"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowOutputEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_output_content
    import capo_bedrock_agent_runtime.types.node_name
    import capo_bedrock_agent_runtime.types.node_type


class FlowOutputEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the flow output node that the output is from.</p>"""
    node_type: "capo_bedrock_agent_runtime.types.node_type.NodeType"
    """<p>The type of the node that the output is from.</p>"""
    content: "capo_bedrock_agent_runtime.types.flow_output_content.FlowOutputContent"
    """<p>The content in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowOutputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.node_type

    out["nodeType"] = capo_bedrock_agent_runtime.types.node_type.serialize_json(
        value["node_type"]
    )
    import capo_bedrock_agent_runtime.types.flow_output_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.flow_output_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowOutputEvent:
    out: FlowOutputEvent = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowOutputEvent.node_name required")
    if data.get("nodeType") is not None:
        import capo_bedrock_agent_runtime.types.node_type

        out["node_type"] = capo_bedrock_agent_runtime.types.node_type.deserialize_json(
            data["nodeType"]
        )
    else:
        raise DeserializationError("FlowOutputEvent.node_type required")
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.flow_output_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.flow_output_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowOutputEvent.content required")
    return out


def serialize_event_json(value: FlowOutputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "flowOutputEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> FlowOutputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: FlowOutputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

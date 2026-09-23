"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowMultiTurnInputRequestEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_multi_turn_input_content
    import capo_bedrock_agent_runtime.types.node_name
    import capo_bedrock_agent_runtime.types.node_type


class FlowMultiTurnInputRequestEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node in the flow that is requesting the input.</p>"""
    node_type: "capo_bedrock_agent_runtime.types.node_type.NodeType"
    """<p>The type of the node in the flow that is requesting the input.</p>"""
    content: "capo_bedrock_agent_runtime.types.flow_multi_turn_input_content.FlowMultiTurnInputContent"
    """<p>The content payload containing the input request details for the multi-turn interaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowMultiTurnInputRequestEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.node_type

    out["nodeType"] = capo_bedrock_agent_runtime.types.node_type.serialize_json(
        value["node_type"]
    )
    import capo_bedrock_agent_runtime.types.flow_multi_turn_input_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.flow_multi_turn_input_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowMultiTurnInputRequestEvent:
    out: FlowMultiTurnInputRequestEvent = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowMultiTurnInputRequestEvent.node_name required")
    if data.get("nodeType") is not None:
        import capo_bedrock_agent_runtime.types.node_type

        out["node_type"] = capo_bedrock_agent_runtime.types.node_type.deserialize_json(
            data["nodeType"]
        )
    else:
        raise DeserializationError("FlowMultiTurnInputRequestEvent.node_type required")
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.flow_multi_turn_input_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.flow_multi_turn_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowMultiTurnInputRequestEvent.content required")
    return out


def serialize_event_json(value: FlowMultiTurnInputRequestEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "flowMultiTurnInputRequestEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> FlowMultiTurnInputRequestEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: FlowMultiTurnInputRequestEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

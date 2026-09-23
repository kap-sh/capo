"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace


class FlowTraceEvent(TypedDict, closed=True):
    trace: "capo_bedrock_agent_runtime.types.flow_trace.FlowTrace"
    """<p>The trace object containing information about an input or output for a node in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceEvent) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.flow_trace

    out["trace"] = capo_bedrock_agent_runtime.types.flow_trace.serialize_json(
        value["trace"]
    )
    return out


def deserialize_json(data: dict) -> FlowTraceEvent:
    out: FlowTraceEvent = {}  # type: ignore[typeddict-item]
    if data.get("trace") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace

        out["trace"] = capo_bedrock_agent_runtime.types.flow_trace.deserialize_json(
            data["trace"]
        )
    else:
        raise DeserializationError("FlowTraceEvent.trace required")
    return out


def serialize_event_json(value: FlowTraceEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "flowTraceEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> FlowTraceEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: FlowTraceEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

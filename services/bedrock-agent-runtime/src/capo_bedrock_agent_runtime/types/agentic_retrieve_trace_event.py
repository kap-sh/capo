"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveTraceEvent``."""

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes


class AgenticRetrieveTraceEvent(TypedDict, closed=True):
    id: "str"
    """<p>The unique identifier of the trace event.</p>"""
    timestamp: "int"
    """<p>The timestamp when the trace event occurred.</p>"""
    attributes: "capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes.AgenticRetrieveTraceEventAttributes"
    """<p>The attributes describing the trace event details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveTraceEvent) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["timestamp"] = value["timestamp"]
    import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes

    out["attributes"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveTraceEvent:
    out: AgenticRetrieveTraceEvent = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AgenticRetrieveTraceEvent.id required")
    if data.get("timestamp") is not None:
        out["timestamp"] = data["timestamp"]
    else:
        raise DeserializationError("AgenticRetrieveTraceEvent.timestamp required")
    if data.get("attributes") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes

        out["attributes"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes.deserialize_json(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveTraceEvent.attributes required")
    return out


def serialize_event_json(value: AgenticRetrieveTraceEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "traceEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AgenticRetrieveTraceEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AgenticRetrieveTraceEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out


def redact_sensitive(value: AgenticRetrieveTraceEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attributes" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes

        out["attributes"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_trace_event_attributes.redact_sensitive(
                value["attributes"]
            )
        )
    return out

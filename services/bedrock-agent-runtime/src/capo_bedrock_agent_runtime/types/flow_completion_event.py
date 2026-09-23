"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowCompletionEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_completion_reason


class FlowCompletionEvent(TypedDict, closed=True):
    completion_reason: (
        "capo_bedrock_agent_runtime.types.flow_completion_reason.FlowCompletionReason"
    )
    """<p>The reason that the flow completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowCompletionEvent) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.flow_completion_reason

    out["completionReason"] = (
        capo_bedrock_agent_runtime.types.flow_completion_reason.serialize_json(
            value["completion_reason"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowCompletionEvent:
    out: FlowCompletionEvent = {}  # type: ignore[typeddict-item]
    if data.get("completionReason") is not None:
        import capo_bedrock_agent_runtime.types.flow_completion_reason

        out["completion_reason"] = (
            capo_bedrock_agent_runtime.types.flow_completion_reason.deserialize_json(
                data["completionReason"]
            )
        )
    else:
        raise DeserializationError("FlowCompletionEvent.completion_reason required")
    return out


def serialize_event_json(value: FlowCompletionEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "flowCompletionEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> FlowCompletionEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: FlowCompletionEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

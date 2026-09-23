"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#MessageStopEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.stop_reason


class MessageStopEvent(TypedDict, closed=True):
    stop_reason: "capo_bedrock_runtime.types.stop_reason.StopReason"
    """<p>The reason why the model stopped generating output.</p>"""
    additional_model_response_fields: NotRequired["object"]
    """<p>The additional model response fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageStopEvent) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.stop_reason

    out["stopReason"] = capo_bedrock_runtime.types.stop_reason.serialize_json(
        value["stop_reason"]
    )
    if "additional_model_response_fields" in value:
        out["additionalModelResponseFields"] = value["additional_model_response_fields"]
    return out


def deserialize_json(data: dict) -> MessageStopEvent:
    out: MessageStopEvent = {}  # type: ignore[typeddict-item]
    if data.get("stopReason") is not None:
        import capo_bedrock_runtime.types.stop_reason

        out["stop_reason"] = capo_bedrock_runtime.types.stop_reason.deserialize_json(
            data["stopReason"]
        )
    else:
        raise DeserializationError("MessageStopEvent.stop_reason required")
    if data.get("additionalModelResponseFields") is not None:
        out["additional_model_response_fields"] = data["additionalModelResponseFields"]
    return out


def serialize_event_json(value: MessageStopEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "messageStop",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MessageStopEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MessageStopEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

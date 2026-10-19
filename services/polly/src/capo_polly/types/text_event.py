"""Generated from Smithy shape ``com.amazonaws.polly#TextEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_polly._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_polly.types.flush_stream_configuration
    import capo_polly.types.text
    import capo_polly.types.text_type


class TextEvent(TypedDict, closed=True):
    text: "capo_polly.types.text.Text"
    """<p>The text content to synthesize. If you specify <code>ssml</code> as the <code>TextType</code>, follow the SSML format for the input text.</p>"""
    text_type: NotRequired["capo_polly.types.text_type.TextType"]
    """<p>Specifies whether the input text is plain text or SSML. Default: plain text.</p>"""
    flush_stream_configuration: NotRequired[
        "capo_polly.types.flush_stream_configuration.FlushStreamConfiguration"
    ]
    """<p>Configuration for controlling when synthesized audio flushes to the output stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextEvent) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "text_type" in value:
        import capo_polly.types.text_type

        out["TextType"] = capo_polly.types.text_type.serialize_json(value["text_type"])
    if "flush_stream_configuration" in value:
        import capo_polly.types.flush_stream_configuration

        out["FlushStreamConfiguration"] = (
            capo_polly.types.flush_stream_configuration.serialize_json(
                value["flush_stream_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextEvent:
    out: TextEvent = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("TextType") is not None:
        import capo_polly.types.text_type

        out["text_type"] = capo_polly.types.text_type.deserialize_json(data["TextType"])
    if data.get("FlushStreamConfiguration") is not None:
        import capo_polly.types.flush_stream_configuration

        out["flush_stream_configuration"] = (
            capo_polly.types.flush_stream_configuration.deserialize_json(
                data["FlushStreamConfiguration"]
            )
        )
    return out


def serialize_event_json(value: TextEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "TextEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TextEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TextEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out

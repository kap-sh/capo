"""Generated from Smithy shape ``com.amazonaws.connect#ChatEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.chat_content
    import capo_connect.types.chat_content_type
    import capo_connect.types.chat_event_type


class ChatEvent(TypedDict, closed=True):
    type: "capo_connect.types.chat_event_type.ChatEventType"
    """<p>Type of chat integration event. </p>"""
    content_type: NotRequired["capo_connect.types.chat_content_type.ChatContentType"]
    """<p>Type of content. This is required when <code>Type</code> is <code>MESSAGE</code> or <code>EVENT</code>. </p> <ul> <li> <p>For allowed message content types, see the <code>ContentType</code> parameter in the <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html">SendMessage</a> topic in the <i>Connect Customer Participant Service API Reference</i>.</p> </li> <li> <p>For allowed event content types, see the <code>ContentType</code> parameter in the <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html">SendEvent</a> topic in the <i>Connect Customer Participant Service API Reference</i>. </p> </li> </ul>"""
    content: NotRequired["capo_connect.types.chat_content.ChatContent"]
    """<p>Content of the message or event. This is required when <code>Type</code> is <code>MESSAGE</code> and for certain <code>ContentTypes</code> when <code>Type</code> is <code>EVENT</code>.</p> <ul> <li> <p>For allowed message content, see the <code>Content</code> parameter in the <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html">SendMessage</a> topic in the <i>Connect Customer Participant Service API Reference</i>.</p> </li> <li> <p>For allowed event content, see the <code>Content</code> parameter in the <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html">SendEvent</a> topic in the <i>Connect Customer Participant Service API Reference</i>. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatEvent) -> dict:
    out: dict = {}
    import capo_connect.types.chat_event_type

    out["Type"] = capo_connect.types.chat_event_type.serialize_json(value["type"])
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> ChatEvent:
    out: ChatEvent = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.chat_event_type

        out["type"] = capo_connect.types.chat_event_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("ChatEvent.type required")
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    return out

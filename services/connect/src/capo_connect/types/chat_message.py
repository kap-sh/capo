"""Generated from Smithy shape ``com.amazonaws.connect#ChatMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.chat_content
    import capo_connect.types.chat_content_type


class ChatMessage(TypedDict, closed=True):
    content_type: "capo_connect.types.chat_content_type.ChatContentType"
    """<p>The type of the content. Supported types are <code>text/plain</code>, <code>text/markdown</code>, <code>application/json</code>, and <code>application/vnd.amazonaws.connect.message.interactive.response</code>.</p>"""
    content: "capo_connect.types.chat_content.ChatContent"
    """<p>The content of the chat message. Maximum of 16,384 bytes for all content types (<code>text/plain</code>, <code>text/markdown</code>, <code>application/json</code>, and <code>application/vnd.amazonaws.connect.message.interactive.response</code>).</p> <p>Some messaging channels enforce lower limits. For channel-specific message size limits, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html#chat-message-size-limits">Chat message size limits by channel</a> in the <i>Amazon Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatMessage) -> dict:
    out: dict = {}
    out["ContentType"] = value["content_type"]
    out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> ChatMessage:
    out: ChatMessage = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("ChatMessage.content_type required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("ChatMessage.content required")
    return out

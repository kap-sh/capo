"""Generated from Smithy shape ``com.amazonaws.qbusiness#ConversationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_id
    import capo_qbusiness.types.conversation_id


class ConversationSource(TypedDict, closed=True):
    conversation_id: "capo_qbusiness.types.conversation_id.ConversationId"
    """<p>The unique identifier of the Amazon Q Business conversation.</p>"""
    attachment_id: "capo_qbusiness.types.attachment_id.AttachmentId"
    """<p>The unique identifier of the Amazon Q Business attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationSource) -> dict:
    out: dict = {}
    out["conversationId"] = value["conversation_id"]
    out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_json(data: dict) -> ConversationSource:
    out: ConversationSource = {}  # type: ignore[typeddict-item]
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    else:
        out["conversation_id"] = ""
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    else:
        out["attachment_id"] = ""
    return out

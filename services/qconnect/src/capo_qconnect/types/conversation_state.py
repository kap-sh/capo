"""Generated from Smithy shape ``com.amazonaws.qconnect#ConversationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.conversation_status
    import capo_qconnect.types.conversation_status_reason


class ConversationState(TypedDict, closed=True):
    status: "capo_qconnect.types.conversation_status.ConversationStatus"
    """<p>The status of the conversation state.</p>"""
    reason: NotRequired[
        "capo_qconnect.types.conversation_status_reason.ConversationStatusReason"
    ]
    """<p>The reason of the conversation state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationState) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ConversationState:
    out: ConversationState = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out

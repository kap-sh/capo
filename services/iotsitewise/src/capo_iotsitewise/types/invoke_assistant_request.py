"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvokeAssistantRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.conversation_id
    import capo_iotsitewise.types.message_input


class InvokeAssistantRequest(TypedDict, closed=True):
    conversation_id: NotRequired[
        "capo_iotsitewise.types.conversation_id.ConversationId"
    ]
    """<p>The ID assigned to a conversation. IoT SiteWise automatically generates a unique ID for you, and this parameter is never required. However, if you prefer to have your own ID, you must specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    message: "capo_iotsitewise.types.message_input.MessageInput"
    """<p>A text message sent to the SiteWise Assistant by the user.</p>"""
    enable_trace: "bool"
    """<p>Specifies if to turn trace on or not. It is used to track the SiteWise Assistant's reasoning, and data access process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAssistantRequest) -> dict:
    out: dict = {}
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    out["message"] = value["message"]
    out["enableTrace"] = value.get("enable_trace", False)
    return out


def deserialize_json(data: dict) -> InvokeAssistantRequest:
    out: InvokeAssistantRequest = {}  # type: ignore[typeddict-item]
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvokeAssistantRequest.message required")
    if data.get("enableTrace") is not None:
        out["enable_trace"] = data["enableTrace"]
    else:
        out["enable_trace"] = False
    return out


def redact_sensitive(value: InvokeAssistantRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out

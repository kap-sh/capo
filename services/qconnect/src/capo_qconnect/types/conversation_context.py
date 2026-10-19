"""Generated from Smithy shape ``com.amazonaws.qconnect#ConversationContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.self_service_conversation_history_list


class ConversationContext(TypedDict, closed=True):
    self_service_conversation_history: "capo_qconnect.types.self_service_conversation_history_list.SelfServiceConversationHistoryList"
    """<p>The self service conversation history before the Amazon Q in Connect session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationContext) -> dict:
    out: dict = {}
    import capo_qconnect.types.self_service_conversation_history_list

    out["selfServiceConversationHistory"] = (
        capo_qconnect.types.self_service_conversation_history_list.serialize_json(
            value["self_service_conversation_history"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationContext:
    out: ConversationContext = {}  # type: ignore[typeddict-item]
    if data.get("selfServiceConversationHistory") is not None:
        import capo_qconnect.types.self_service_conversation_history_list

        out["self_service_conversation_history"] = (
            capo_qconnect.types.self_service_conversation_history_list.deserialize_json(
                data["selfServiceConversationHistory"]
            )
        )
    else:
        out["self_service_conversation_history"] = []
    return out


def redact_sensitive(value: ConversationContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "self_service_conversation_history" in value:
        import capo_qconnect.types.self_service_conversation_history_list

        out["self_service_conversation_history"] = (
            capo_qconnect.types.self_service_conversation_history_list.redact_sensitive(
                value["self_service_conversation_history"]
            )
        )
    return out

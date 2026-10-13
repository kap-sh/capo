"""Generated from Smithy shape ``com.amazonaws.qconnect#SelfServiceConversationHistoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.self_service_conversation_history

SelfServiceConversationHistoryList: TypeAlias = list[
    "capo_qconnect.types.self_service_conversation_history.SelfServiceConversationHistory"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfServiceConversationHistoryList) -> list:
    import capo_qconnect.types.self_service_conversation_history

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.self_service_conversation_history.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SelfServiceConversationHistoryList:
    import capo_qconnect.types.self_service_conversation_history

    out: SelfServiceConversationHistoryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_qconnect.types.self_service_conversation_history.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SelfServiceConversationHistoryList) -> list[Any]:
    import capo_qconnect.types.self_service_conversation_history

    return [
        capo_qconnect.types.self_service_conversation_history.redact_sensitive(item)
        for item in value
    ]

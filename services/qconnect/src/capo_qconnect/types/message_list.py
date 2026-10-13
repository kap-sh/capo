"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_output

MessageList: TypeAlias = list["capo_qconnect.types.message_output.MessageOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageList) -> list:
    import capo_qconnect.types.message_output

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.message_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageList:
    import capo_qconnect.types.message_output

    out: MessageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.message_output.deserialize_json(item))
    return out


def redact_sensitive(value: MessageList) -> list[Any]:
    import capo_qconnect.types.message_output

    return [capo_qconnect.types.message_output.redact_sensitive(item) for item in value]

"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanMessageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.span_message

SpanMessageList: TypeAlias = list["capo_qconnect.types.span_message.SpanMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanMessageList) -> list:
    import capo_qconnect.types.span_message

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.span_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanMessageList:
    import capo_qconnect.types.span_message

    out: SpanMessageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.span_message.deserialize_json(item))
    return out


def redact_sensitive(value: SpanMessageList) -> list[Any]:
    import capo_qconnect.types.span_message

    return [capo_qconnect.types.span_message.redact_sensitive(item) for item in value]

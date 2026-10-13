"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanMessageValueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.span_message_value

SpanMessageValueList: TypeAlias = list[
    "capo_qconnect.types.span_message_value.SpanMessageValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpanMessageValueList) -> list:
    import capo_qconnect.types.span_message_value

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.span_message_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanMessageValueList:
    import capo_qconnect.types.span_message_value

    out: SpanMessageValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.span_message_value.deserialize_json(item))
    return out


def redact_sensitive(value: SpanMessageValueList) -> list[Any]:
    import capo_qconnect.types.span_message_value

    return [
        capo_qconnect.types.span_message_value.redact_sensitive(item) for item in value
    ]

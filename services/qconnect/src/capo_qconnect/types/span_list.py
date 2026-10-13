"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.span

SpanList: TypeAlias = list["capo_qconnect.types.span.Span"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanList) -> list:
    import capo_qconnect.types.span

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.span.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanList:
    import capo_qconnect.types.span

    out: SpanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.span.deserialize_json(item))
    return out


def redact_sensitive(value: SpanList) -> list[Any]:
    import capo_qconnect.types.span

    return [capo_qconnect.types.span.redact_sensitive(item) for item in value]

"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanCitationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.span_citation

SpanCitationList: TypeAlias = list["capo_qconnect.types.span_citation.SpanCitation"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanCitationList) -> list:
    import capo_qconnect.types.span_citation

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.span_citation.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanCitationList:
    import capo_qconnect.types.span_citation

    out: SpanCitationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.span_citation.deserialize_json(item))
    return out


def redact_sensitive(value: SpanCitationList) -> list[Any]:
    import capo_qconnect.types.span_citation

    return [capo_qconnect.types.span_citation.redact_sensitive(item) for item in value]

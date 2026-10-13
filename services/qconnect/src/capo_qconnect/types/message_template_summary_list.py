"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_summary

MessageTemplateSummaryList: TypeAlias = list[
    "capo_qconnect.types.message_template_summary.MessageTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSummaryList) -> list:
    import capo_qconnect.types.message_template_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.message_template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageTemplateSummaryList:
    import capo_qconnect.types.message_template_summary

    out: MessageTemplateSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.message_template_summary.deserialize_json(item))
    return out


def redact_sensitive(value: MessageTemplateSummaryList) -> list[Any]:
    import capo_qconnect.types.message_template_summary

    return [
        capo_qconnect.types.message_template_summary.redact_sensitive(item)
        for item in value
    ]

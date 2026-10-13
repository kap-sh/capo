"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttachmentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attachment

MessageTemplateAttachmentList: TypeAlias = list[
    "capo_qconnect.types.message_template_attachment.MessageTemplateAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttachmentList) -> list:
    import capo_qconnect.types.message_template_attachment

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.message_template_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageTemplateAttachmentList:
    import capo_qconnect.types.message_template_attachment

    out: MessageTemplateAttachmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_qconnect.types.message_template_attachment.deserialize_json(item)
        )
    return out


def redact_sensitive(value: MessageTemplateAttachmentList) -> list[Any]:
    import capo_qconnect.types.message_template_attachment

    return [
        capo_qconnect.types.message_template_attachment.redact_sensitive(item)
        for item in value
    ]

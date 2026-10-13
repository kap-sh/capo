"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateMessageTemplateAttachmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attachment


class CreateMessageTemplateAttachmentResponse(TypedDict, closed=True):
    attachment: NotRequired[
        "capo_qconnect.types.message_template_attachment.MessageTemplateAttachment"
    ]
    """<p>The message template attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMessageTemplateAttachmentResponse) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_qconnect.types.message_template_attachment

        out["attachment"] = (
            capo_qconnect.types.message_template_attachment.serialize_json(
                value["attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMessageTemplateAttachmentResponse:
    out: CreateMessageTemplateAttachmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("attachment") is not None:
        import capo_qconnect.types.message_template_attachment

        out["attachment"] = (
            capo_qconnect.types.message_template_attachment.deserialize_json(
                data["attachment"]
            )
        )
    return out


def redact_sensitive(value: CreateMessageTemplateAttachmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attachment" in value:
        import capo_qconnect.types.message_template_attachment

        out["attachment"] = (
            capo_qconnect.types.message_template_attachment.redact_sensitive(
                value["attachment"]
            )
        )
    return out

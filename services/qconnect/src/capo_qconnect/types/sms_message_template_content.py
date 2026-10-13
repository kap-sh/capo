"""Generated from Smithy shape ``com.amazonaws.qconnect#SMSMessageTemplateContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.sms_message_template_content_body


class SMSMessageTemplateContent(TypedDict, closed=True):
    body: NotRequired[
        "capo_qconnect.types.sms_message_template_content_body.SMSMessageTemplateContentBody"
    ]
    """<p>The body to use in SMS messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSMessageTemplateContent) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_qconnect.types.sms_message_template_content_body

        out["body"] = (
            capo_qconnect.types.sms_message_template_content_body.serialize_json(
                value["body"]
            )
        )
    return out


def deserialize_json(data: dict) -> SMSMessageTemplateContent:
    out: SMSMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_qconnect.types.sms_message_template_content_body

        out["body"] = (
            capo_qconnect.types.sms_message_template_content_body.deserialize_json(
                data["body"]
            )
        )
    return out


def redact_sensitive(value: SMSMessageTemplateContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        import capo_qconnect.types.sms_message_template_content_body

        out["body"] = (
            capo_qconnect.types.sms_message_template_content_body.redact_sensitive(
                value["body"]
            )
        )
    return out

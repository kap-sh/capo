"""Generated from Smithy shape ``com.amazonaws.qconnect#SMSMessageTemplateContentBody``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_body_content_provider


class SMSMessageTemplateContentBody(TypedDict, closed=True):
    plain_text: NotRequired[
        "capo_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The message body to use in SMS messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSMessageTemplateContentBody) -> dict:
    out: dict = {}
    if "plain_text" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["plainText"] = (
            capo_qconnect.types.message_template_body_content_provider.serialize_json(
                value["plain_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> SMSMessageTemplateContentBody:
    out: SMSMessageTemplateContentBody = {}  # type: ignore[typeddict-item]
    if data.get("plainText") is not None:
        import capo_qconnect.types.message_template_body_content_provider

        out["plain_text"] = (
            capo_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["plainText"]
            )
        )
    return out


def redact_sensitive(value: SMSMessageTemplateContentBody) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "plain_text" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["plain_text"] = (
            capo_qconnect.types.message_template_body_content_provider.redact_sensitive(
                value["plain_text"]
            )
        )
    return out

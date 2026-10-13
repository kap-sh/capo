"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailMessageTemplateContentBody``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_body_content_provider


class EmailMessageTemplateContentBody(TypedDict, closed=True):
    plain_text: NotRequired[
        "capo_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.</p>"""
    html: NotRequired[
        "capo_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailMessageTemplateContentBody) -> dict:
    out: dict = {}
    if "plain_text" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["plainText"] = (
            capo_qconnect.types.message_template_body_content_provider.serialize_json(
                value["plain_text"]
            )
        )
    if "html" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["html"] = (
            capo_qconnect.types.message_template_body_content_provider.serialize_json(
                value["html"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailMessageTemplateContentBody:
    out: EmailMessageTemplateContentBody = {}  # type: ignore[typeddict-item]
    if data.get("plainText") is not None:
        import capo_qconnect.types.message_template_body_content_provider

        out["plain_text"] = (
            capo_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["plainText"]
            )
        )
    if data.get("html") is not None:
        import capo_qconnect.types.message_template_body_content_provider

        out["html"] = (
            capo_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["html"]
            )
        )
    return out


def redact_sensitive(value: EmailMessageTemplateContentBody) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "plain_text" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["plain_text"] = (
            capo_qconnect.types.message_template_body_content_provider.redact_sensitive(
                value["plain_text"]
            )
        )
    if "html" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["html"] = (
            capo_qconnect.types.message_template_body_content_provider.redact_sensitive(
                value["html"]
            )
        )
    return out

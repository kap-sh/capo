"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailMessageTemplateContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.email_headers
    import capo_qconnect.types.email_message_template_content_body
    import capo_qconnect.types.non_empty_unlimited_string


class EmailMessageTemplateContent(TypedDict, closed=True):
    subject: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The subject line, or title, to use in email messages.</p>"""
    body: NotRequired[
        "capo_qconnect.types.email_message_template_content_body.EmailMessageTemplateContentBody"
    ]
    """<p>The body to use in email messages.</p>"""
    headers: NotRequired["capo_qconnect.types.email_headers.EmailHeaders"]
    """<p>The email headers to include in email messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailMessageTemplateContent) -> dict:
    out: dict = {}
    if "subject" in value:
        out["subject"] = value["subject"]
    if "body" in value:
        import capo_qconnect.types.email_message_template_content_body

        out["body"] = (
            capo_qconnect.types.email_message_template_content_body.serialize_json(
                value["body"]
            )
        )
    if "headers" in value:
        import capo_qconnect.types.email_headers

        out["headers"] = capo_qconnect.types.email_headers.serialize_json(
            value["headers"]
        )
    return out


def deserialize_json(data: dict) -> EmailMessageTemplateContent:
    out: EmailMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if data.get("subject") is not None:
        out["subject"] = data["subject"]
    if data.get("body") is not None:
        import capo_qconnect.types.email_message_template_content_body

        out["body"] = (
            capo_qconnect.types.email_message_template_content_body.deserialize_json(
                data["body"]
            )
        )
    if data.get("headers") is not None:
        import capo_qconnect.types.email_headers

        out["headers"] = capo_qconnect.types.email_headers.deserialize_json(
            data["headers"]
        )
    return out


def redact_sensitive(value: EmailMessageTemplateContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subject" in value:
        out["subject"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        import capo_qconnect.types.email_message_template_content_body

        out["body"] = (
            capo_qconnect.types.email_message_template_content_body.redact_sensitive(
                value["body"]
            )
        )
    if "headers" in value:
        import capo_qconnect.types.email_headers

        out["headers"] = capo_qconnect.types.email_headers.redact_sensitive(
            value["headers"]
        )
    return out

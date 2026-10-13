"""Generated from Smithy shape ``com.amazonaws.connect#OutboundRawMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.body
    import capo_connect.types.email_message_content_type
    import capo_connect.types.outbound_subject


class OutboundRawMessage(TypedDict, closed=True):
    subject: "capo_connect.types.outbound_subject.OutboundSubject"
    """<p>The email subject.</p>"""
    body: "capo_connect.types.body.Body"
    """<p>The email message body.</p>"""
    content_type: (
        "capo_connect.types.email_message_content_type.EmailMessageContentType"
    )
    """<p>Type of content, that is, <code>text/plain</code> or <code>text/html</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundRawMessage) -> dict:
    out: dict = {}
    out["Subject"] = value["subject"]
    out["Body"] = value["body"]
    out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> OutboundRawMessage:
    out: OutboundRawMessage = {}  # type: ignore[typeddict-item]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    else:
        raise DeserializationError("OutboundRawMessage.subject required")
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    else:
        raise DeserializationError("OutboundRawMessage.body required")
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("OutboundRawMessage.content_type required")
    return out


def redact_sensitive(value: OutboundRawMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subject" in value:
        out["subject"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out

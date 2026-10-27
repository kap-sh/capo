"""Generated from Smithy shape ``com.amazonaws.connect#UpdateOutboundRawMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.body
    import capo_connect.types.email_message_content_type


class UpdateOutboundRawMessage(TypedDict, closed=True):
    body: "capo_connect.types.body.Body"
    """<p>The email message body.</p>"""
    content_type: (
        "capo_connect.types.email_message_content_type.EmailMessageContentType"
    )
    """<p>The content type of the email body. Valid values:</p> <ul> <li> <p> <code>text/plain</code> – Plain text content.</p> </li> <li> <p> <code>text/html</code> – HTML-formatted content.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutboundRawMessage) -> dict:
    out: dict = {}
    out["Body"] = value["body"]
    out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> UpdateOutboundRawMessage:
    out: UpdateOutboundRawMessage = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    else:
        out["body"] = ""
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        out["content_type"] = ""
    return out


def redact_sensitive(value: UpdateOutboundRawMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out

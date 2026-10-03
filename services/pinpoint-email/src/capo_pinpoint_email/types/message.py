"""Generated from Smithy shape ``com.amazonaws.pinpointemail#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.body
    import capo_pinpoint_email.types.content


class Message(TypedDict, closed=True):
    subject: "capo_pinpoint_email.types.content.Content"
    """<p>The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in <a href="https://tools.ietf.org/html/rfc2047">RFC 2047</a>.</p>"""
    body: "capo_pinpoint_email.types.body.Body"
    """<p>The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import capo_pinpoint_email.types.content

    out["Subject"] = capo_pinpoint_email.types.content.serialize_json(value["subject"])
    import capo_pinpoint_email.types.body

    out["Body"] = capo_pinpoint_email.types.body.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("Subject") is not None:
        import capo_pinpoint_email.types.content

        out["subject"] = capo_pinpoint_email.types.content.deserialize_json(
            data["Subject"]
        )
    else:
        raise DeserializationError("Message.subject required")
    if data.get("Body") is not None:
        import capo_pinpoint_email.types.body

        out["body"] = capo_pinpoint_email.types.body.deserialize_json(data["Body"])
    else:
        raise DeserializationError("Message.body required")
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.attachment_list
    import capo_sesv2.types.body
    import capo_sesv2.types.content
    import capo_sesv2.types.message_header_list


class Message(TypedDict, closed=True):
    subject: "capo_sesv2.types.content.Content"
    """<p>The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in <a href="https://tools.ietf.org/html/rfc2047">RFC 2047</a>.</p>"""
    body: "capo_sesv2.types.body.Body"
    """<p>The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.</p>"""
    headers: NotRequired["capo_sesv2.types.message_header_list.MessageHeaderList"]
    """<p>The list of message headers that will be added to the email message.</p>"""
    attachments: NotRequired["capo_sesv2.types.attachment_list.AttachmentList"]
    """<p> The List of attachments to include in your email. All recipients will receive the same attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import capo_sesv2.types.content

    out["Subject"] = capo_sesv2.types.content.serialize_json(value["subject"])
    import capo_sesv2.types.body

    out["Body"] = capo_sesv2.types.body.serialize_json(value["body"])
    if "headers" in value:
        import capo_sesv2.types.message_header_list

        out["Headers"] = capo_sesv2.types.message_header_list.serialize_json(
            value["headers"]
        )
    if "attachments" in value:
        import capo_sesv2.types.attachment_list

        out["Attachments"] = capo_sesv2.types.attachment_list.serialize_json(
            value["attachments"]
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("Subject") is not None:
        import capo_sesv2.types.content

        out["subject"] = capo_sesv2.types.content.deserialize_json(data["Subject"])
    else:
        raise DeserializationError("Message.subject required")
    if data.get("Body") is not None:
        import capo_sesv2.types.body

        out["body"] = capo_sesv2.types.body.deserialize_json(data["Body"])
    else:
        raise DeserializationError("Message.body required")
    if data.get("Headers") is not None:
        import capo_sesv2.types.message_header_list

        out["headers"] = capo_sesv2.types.message_header_list.deserialize_json(
            data["Headers"]
        )
    if data.get("Attachments") is not None:
        import capo_sesv2.types.attachment_list

        out["attachments"] = capo_sesv2.types.attachment_list.deserialize_json(
            data["Attachments"]
        )
    return out

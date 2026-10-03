"""Generated from Smithy shape ``com.amazonaws.pinpointemail#EmailContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.message
    import capo_pinpoint_email.types.raw_message
    import capo_pinpoint_email.types.template


class EmailContent(TypedDict, closed=True):
    simple: NotRequired["capo_pinpoint_email.types.message.Message"]
    """<p>The simple email message. The message consists of a subject and a message body.</p>"""
    raw: NotRequired["capo_pinpoint_email.types.raw_message.RawMessage"]
    """<p>The raw email message. The message has to meet the following criteria:</p> <ul> <li> <p>The message has to contain a header and a body, separated by one blank line.</p> </li> <li> <p>All of the required header fields must be present in the message.</p> </li> <li> <p>Each part of a multipart MIME message must be formatted properly.</p> </li> <li> <p>If you include attachments, they must be in a file format that Amazon Pinpoint supports. </p> </li> <li> <p>The entire message must be Base64 encoded.</p> </li> <li> <p>If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.</p> </li> <li> <p>The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in <a href="https://tools.ietf.org/html/rfc5321">RFC 5321</a>.</p> </li> </ul>"""
    template: NotRequired["capo_pinpoint_email.types.template.Template"]
    """<p>The template to use for the email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailContent) -> dict:
    out: dict = {}
    if "simple" in value:
        import capo_pinpoint_email.types.message

        out["Simple"] = capo_pinpoint_email.types.message.serialize_json(
            value["simple"]
        )
    if "raw" in value:
        import capo_pinpoint_email.types.raw_message

        out["Raw"] = capo_pinpoint_email.types.raw_message.serialize_json(value["raw"])
    if "template" in value:
        import capo_pinpoint_email.types.template

        out["Template"] = capo_pinpoint_email.types.template.serialize_json(
            value["template"]
        )
    return out


def deserialize_json(data: dict) -> EmailContent:
    out: EmailContent = {}  # type: ignore[typeddict-item]
    if data.get("Simple") is not None:
        import capo_pinpoint_email.types.message

        out["simple"] = capo_pinpoint_email.types.message.deserialize_json(
            data["Simple"]
        )
    if data.get("Raw") is not None:
        import capo_pinpoint_email.types.raw_message

        out["raw"] = capo_pinpoint_email.types.raw_message.deserialize_json(data["Raw"])
    if data.get("Template") is not None:
        import capo_pinpoint_email.types.template

        out["template"] = capo_pinpoint_email.types.template.deserialize_json(
            data["Template"]
        )
    return out

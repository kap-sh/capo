"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.message
    import capo_sesv2.types.raw_message
    import capo_sesv2.types.template


class EmailContent(TypedDict, closed=True):
    simple: NotRequired["capo_sesv2.types.message.Message"]
    """<p>The simple email message. The message consists of a subject, message body and attachments list.</p>"""
    raw: NotRequired["capo_sesv2.types.raw_message.RawMessage"]
    """<p>The raw email message. The message has to meet the following criteria:</p> <ul> <li> <p>The message has to contain a header and a body, separated by one blank line.</p> </li> <li> <p>All of the required header fields must be present in the message.</p> </li> <li> <p>Each part of a multipart MIME message must be formatted properly.</p> </li> <li> <p>If you include attachments, they must be in a file format that the Amazon SES API v2 supports. </p> </li> <li> <p>The raw data of the message needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.</p> </li> <li> <p>If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.</p> </li> <li> <p>The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in <a href="https://tools.ietf.org/html/rfc5321">RFC 5321</a>.</p> </li> </ul>"""
    template: NotRequired["capo_sesv2.types.template.Template"]
    """<p>The template to use for the email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailContent) -> dict:
    out: dict = {}
    if "simple" in value:
        import capo_sesv2.types.message

        out["Simple"] = capo_sesv2.types.message.serialize_json(value["simple"])
    if "raw" in value:
        import capo_sesv2.types.raw_message

        out["Raw"] = capo_sesv2.types.raw_message.serialize_json(value["raw"])
    if "template" in value:
        import capo_sesv2.types.template

        out["Template"] = capo_sesv2.types.template.serialize_json(value["template"])
    return out


def deserialize_json(data: dict) -> EmailContent:
    out: EmailContent = {}  # type: ignore[typeddict-item]
    if data.get("Simple") is not None:
        import capo_sesv2.types.message

        out["simple"] = capo_sesv2.types.message.deserialize_json(data["Simple"])
    if data.get("Raw") is not None:
        import capo_sesv2.types.raw_message

        out["raw"] = capo_sesv2.types.raw_message.deserialize_json(data["Raw"])
    if data.get("Template") is not None:
        import capo_sesv2.types.template

        out["template"] = capo_sesv2.types.template.deserialize_json(data["Template"])
    return out

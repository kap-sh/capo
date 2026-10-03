"""Generated from Smithy shape ``com.amazonaws.sesv2#BulkEmailEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.destination
    import capo_sesv2.types.message_header_list
    import capo_sesv2.types.message_tag_list
    import capo_sesv2.types.replacement_email_content


class BulkEmailEntry(TypedDict, closed=True):
    destination: "capo_sesv2.types.destination.Destination"
    """<p>Represents the destination of the message, consisting of To:, CC:, and BCC: fields.</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in <a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain <a href="https://en.wikipedia.org/wiki/Email_address#Local-part">7-bit ASCII characters</a>. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in <a href="https://tools.ietf.org/html/rfc3492.html">RFC3492</a>.</p> </note>"""
    replacement_tags: NotRequired["capo_sesv2.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendBulkTemplatedEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>"""
    replacement_email_content: NotRequired[
        "capo_sesv2.types.replacement_email_content.ReplacementEmailContent"
    ]
    """<p>The <code>ReplacementEmailContent</code> associated with a <code>BulkEmailEntry</code>.</p>"""
    replacement_headers: NotRequired[
        "capo_sesv2.types.message_header_list.MessageHeaderList"
    ]
    """<p>The list of message headers associated with the <code>BulkEmailEntry</code> data type.</p> <ul> <li> <p>Headers Not Present in <code>BulkEmailEntry</code>: If a header is specified in <a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html"> <code>Template</code> </a> but not in <code>BulkEmailEntry</code>, the header from <code>Template</code> will be added to the outgoing email.</p> </li> <li> <p>Headers Present in <code>BulkEmailEntry</code>: If a header is specified in <code>BulkEmailEntry</code>, it takes precedence over any header of the same name specified in <a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html"> <code>Template</code> </a>:</p> <ul> <li> <p>If the header is also defined within <code>Template</code>, the value from <code>BulkEmailEntry</code> will replace the header's value in the email.</p> </li> <li> <p>If the header is not defined within <code>Template</code>, it will simply be added to the email as specified in <code>BulkEmailEntry</code>.</p> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BulkEmailEntry) -> dict:
    out: dict = {}
    import capo_sesv2.types.destination

    out["Destination"] = capo_sesv2.types.destination.serialize_json(
        value["destination"]
    )
    if "replacement_tags" in value:
        import capo_sesv2.types.message_tag_list

        out["ReplacementTags"] = capo_sesv2.types.message_tag_list.serialize_json(
            value["replacement_tags"]
        )
    if "replacement_email_content" in value:
        import capo_sesv2.types.replacement_email_content

        out["ReplacementEmailContent"] = (
            capo_sesv2.types.replacement_email_content.serialize_json(
                value["replacement_email_content"]
            )
        )
    if "replacement_headers" in value:
        import capo_sesv2.types.message_header_list

        out["ReplacementHeaders"] = capo_sesv2.types.message_header_list.serialize_json(
            value["replacement_headers"]
        )
    return out


def deserialize_json(data: dict) -> BulkEmailEntry:
    out: BulkEmailEntry = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        import capo_sesv2.types.destination

        out["destination"] = capo_sesv2.types.destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("BulkEmailEntry.destination required")
    if data.get("ReplacementTags") is not None:
        import capo_sesv2.types.message_tag_list

        out["replacement_tags"] = capo_sesv2.types.message_tag_list.deserialize_json(
            data["ReplacementTags"]
        )
    if data.get("ReplacementEmailContent") is not None:
        import capo_sesv2.types.replacement_email_content

        out["replacement_email_content"] = (
            capo_sesv2.types.replacement_email_content.deserialize_json(
                data["ReplacementEmailContent"]
            )
        )
    if data.get("ReplacementHeaders") is not None:
        import capo_sesv2.types.message_header_list

        out["replacement_headers"] = (
            capo_sesv2.types.message_header_list.deserialize_json(
                data["ReplacementHeaders"]
            )
        )
    return out

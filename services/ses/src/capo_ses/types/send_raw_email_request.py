"""Generated from Smithy shape ``com.amazonaws.ses#SendRawEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.address_list
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.configuration_set_name
    import capo_ses.types.message_tag_list
    import capo_ses.types.raw_message


class SendRawEmailRequest(TypedDict, closed=True):
    source: NotRequired["capo_ses.types.address.Address"]
    """<p>The identity's email address. If you do not provide a value for this parameter, you must specify a "From" address in the raw text of the message. (You can also specify both.)</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in<a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending raw email using the Amazon SES API</a>. For more information about Punycode, see <a href="http://tools.ietf.org/html/rfc3492">RFC 3492</a>.</p> </note> <p>If you specify the <code>Source</code> parameter and have feedback forwarding enabled, then bounces and complaints are sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.</p>"""
    destinations: NotRequired["capo_ses.types.address_list.AddressList"]
    """<p>A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.</p>"""
    raw_message: "capo_ses.types.raw_message.RawMessage"
    """<p>The raw email message itself. The message has to meet the following criteria:</p> <ul> <li> <p>The message has to contain a header and a body, separated by a blank line.</p> </li> <li> <p>All of the required header fields must be present in the message.</p> </li> <li> <p>Each part of a multipart MIME message must be formatted properly.</p> </li> <li> <p>Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see <a href="https://docs.aws.amazon.com/ses/latest/dg/mime-types.html">Unsupported Attachment Types</a> in the <i>Amazon SES Developer Guide</i>.</p> </li> <li> <p>The entire message must be base64-encoded.</p> </li> <li> <p>If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending Raw Email</a> in the <i>Amazon SES Developer Guide</i>.</p> </li> <li> <p>Per <a href="https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6">RFC 5321</a>, the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters.</p> </li> </ul>"""
    from_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular "From" address in the header of the raw email.</p> <p>Instead of using this parameter, you can use the X-header <code>X-SES-FROM-ARN</code> in the raw message of the email. If you use both the <code>FromArn</code> parameter and the corresponding X-header, Amazon SES uses the value of the <code>FromArn</code> parameter.</p> <note> <p>For information about when to use this parameter, see the description of <code>SendRawEmail</code> in this guide, or see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html">Amazon SES Developer Guide</a>.</p> </note>"""
    source_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the <code>Source</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to send from <code>user@example.com</code>, then you would specify the <code>SourceArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>Source</code> to be <code>user@example.com</code>.</p> <p>Instead of using this parameter, you can use the X-header <code>X-SES-SOURCE-ARN</code> in the raw message of the email. If you use both the <code>SourceArn</code> parameter and the corresponding X-header, Amazon SES uses the value of the <code>SourceArn</code> parameter.</p> <note> <p>For information about when to use this parameter, see the description of <code>SendRawEmail</code> in this guide, or see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html">Amazon SES Developer Guide</a>.</p> </note>"""
    return_path_arn: NotRequired[
        "capo_ses.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>ReturnPath</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to use <code>feedback@example.com</code>, then you would specify the <code>ReturnPathArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>ReturnPath</code> to be <code>feedback@example.com</code>.</p> <p>Instead of using this parameter, you can use the X-header <code>X-SES-RETURN-PATH-ARN</code> in the raw message of the email. If you use both the <code>ReturnPathArn</code> parameter and the corresponding X-header, Amazon SES uses the value of the <code>ReturnPathArn</code> parameter.</p> <note> <p>For information about when to use this parameter, see the description of <code>SendRawEmail</code> in this guide, or see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html">Amazon SES Developer Guide</a>.</p> </note>"""
    tags: NotRequired["capo_ses.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using <code>SendRawEmail</code>. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>"""
    configuration_set_name: NotRequired[
        "capo_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set to use when you send an email using <code>SendRawEmail</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendRawEmailRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "destinations" in value:
        import capo_ses.types.address_list

        capo_ses.types.address_list.serialize_query(
            value["destinations"], pairs, f"{key_prefix}Destinations"
        )
    import capo_ses.types.raw_message

    capo_ses.types.raw_message.serialize_query(
        value["raw_message"], pairs, f"{key_prefix}RawMessage"
    )
    if "from_arn" in value:
        pairs.append((f"{key_prefix}FromArn", str(value["from_arn"])))
    if "source_arn" in value:
        pairs.append((f"{key_prefix}SourceArn", str(value["source_arn"])))
    if "return_path_arn" in value:
        pairs.append((f"{key_prefix}ReturnPathArn", str(value["return_path_arn"])))
    if "tags" in value:
        import capo_ses.types.message_tag_list

        capo_ses.types.message_tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "configuration_set_name" in value:
        pairs.append(
            (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
        )


def deserialize_query(el: Element) -> SendRawEmailRequest:
    out: SendRawEmailRequest = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_destinations = el.find("Destinations")
    if child_destinations is not None:
        import capo_ses.types.address_list

        out["destinations"] = capo_ses.types.address_list.deserialize_query(
            child_destinations
        )
    child_raw_message = el.find("RawMessage")
    if child_raw_message is not None:
        import capo_ses.types.raw_message

        out["raw_message"] = capo_ses.types.raw_message.deserialize_query(
            child_raw_message
        )
    else:
        raise DeserializationError("SendRawEmailRequest.raw_message required")
    child_from_arn = el.find("FromArn")
    if child_from_arn is not None:
        out["from_arn"] = str(child_from_arn.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_return_path_arn = el.find("ReturnPathArn")
    if child_return_path_arn is not None:
        out["return_path_arn"] = str(child_return_path_arn.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_ses.types.message_tag_list

        out["tags"] = capo_ses.types.message_tag_list.deserialize_query(child_tags)
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    return out

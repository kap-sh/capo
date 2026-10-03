"""Generated from Smithy shape ``com.amazonaws.ses#SendEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.address_list
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.configuration_set_name
    import capo_ses.types.destination
    import capo_ses.types.message
    import capo_ses.types.message_tag_list


class SendEmailRequest(TypedDict, closed=True):
    source: "capo_ses.types.address.Address"
    """<p>The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html">Amazon SES Developer Guide</a>.</p> <p>If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the <code>SourceArn</code> parameter. For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <note> <p>Amazon SES does not support the SMTPUTF8 extension, as described in <a href="https://tools.ietf.org/html/rfc6531">RFC6531</a>. For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Sending raw email using the Amazon SES API</a>. For more information about Punycode, see <a href="http://tools.ietf.org/html/rfc3492">RFC 3492</a>.</p> </note>"""
    destination: "capo_ses.types.destination.Destination"
    """<p>The destination for this email, composed of To:, CC:, and BCC: fields.</p>"""
    message: "capo_ses.types.message.Message"
    """<p>The message to be sent.</p>"""
    reply_to_addresses: NotRequired["capo_ses.types.address_list.AddressList"]
    """<p>The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.</p>"""
    return_path: NotRequired["capo_ses.types.address.Address"]
    """<p>The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipient's ISP; this message is forwarded to the email address specified by the <code>ReturnPath</code> parameter. The <code>ReturnPath</code> parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. </p>"""
    source_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the <code>Source</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to send from <code>user@example.com</code>, then you would specify the <code>SourceArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>Source</code> to be <code>user@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>"""
    return_path_arn: NotRequired[
        "capo_ses.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>ReturnPath</code> parameter.</p> <p>For example, if the owner of <code>example.com</code> (which has ARN <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>) attaches a policy to it that authorizes you to use <code>feedback@example.com</code>, then you would specify the <code>ReturnPathArn</code> to be <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>, and the <code>ReturnPath</code> to be <code>feedback@example.com</code>.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>"""
    tags: NotRequired["capo_ses.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using <code>SendEmail</code>. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>"""
    configuration_set_name: NotRequired[
        "capo_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set to use when you send an email using <code>SendEmail</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendEmailRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Source", str(value["source"])))
    import capo_ses.types.destination

    capo_ses.types.destination.serialize_query(
        value["destination"], pairs, f"{key_prefix}Destination"
    )
    import capo_ses.types.message

    capo_ses.types.message.serialize_query(
        value["message"], pairs, f"{key_prefix}Message"
    )
    if "reply_to_addresses" in value:
        import capo_ses.types.address_list

        capo_ses.types.address_list.serialize_query(
            value["reply_to_addresses"], pairs, f"{key_prefix}ReplyToAddresses"
        )
    if "return_path" in value:
        pairs.append((f"{key_prefix}ReturnPath", str(value["return_path"])))
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


def deserialize_query(el: Element) -> SendEmailRequest:
    out: SendEmailRequest = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    else:
        raise DeserializationError("SendEmailRequest.source required")
    child_destination = el.find("Destination")
    if child_destination is not None:
        import capo_ses.types.destination

        out["destination"] = capo_ses.types.destination.deserialize_query(
            child_destination
        )
    else:
        raise DeserializationError("SendEmailRequest.destination required")
    child_message = el.find("Message")
    if child_message is not None:
        import capo_ses.types.message

        out["message"] = capo_ses.types.message.deserialize_query(child_message)
    else:
        raise DeserializationError("SendEmailRequest.message required")
    child_reply_to_addresses = el.find("ReplyToAddresses")
    if child_reply_to_addresses is not None:
        import capo_ses.types.address_list

        out["reply_to_addresses"] = capo_ses.types.address_list.deserialize_query(
            child_reply_to_addresses
        )
    child_return_path = el.find("ReturnPath")
    if child_return_path is not None:
        out["return_path"] = str(child_return_path.text or "")
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

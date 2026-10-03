"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.configuration_set_name
    import capo_pinpoint_email.types.destination
    import capo_pinpoint_email.types.email_address
    import capo_pinpoint_email.types.email_address_list
    import capo_pinpoint_email.types.email_content
    import capo_pinpoint_email.types.message_tag_list


class SendEmailRequest(TypedDict, closed=True):
    from_email_address: NotRequired[
        "capo_pinpoint_email.types.email_address.EmailAddress"
    ]
    """<p>The email address that you want to use as the "From" address for the email. The address that you specify has to be verified. </p>"""
    destination: "capo_pinpoint_email.types.destination.Destination"
    """<p>An object that contains the recipients of the email message.</p>"""
    reply_to_addresses: NotRequired[
        "capo_pinpoint_email.types.email_address_list.EmailAddressList"
    ]
    """<p>The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.</p>"""
    feedback_forwarding_email_address: NotRequired[
        "capo_pinpoint_email.types.email_address.EmailAddress"
    ]
    """<p>The address that Amazon Pinpoint should send bounce and complaint notifications to.</p>"""
    content: "capo_pinpoint_email.types.email_content.EmailContent"
    """<p>An object that contains the body of the message. You can send either a Simple message or a Raw message.</p>"""
    email_tags: NotRequired["capo_pinpoint_email.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. </p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set that you want to use when sending the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEmailRequest) -> dict:
    out: dict = {}
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    import capo_pinpoint_email.types.destination

    out["Destination"] = capo_pinpoint_email.types.destination.serialize_json(
        value["destination"]
    )
    if "reply_to_addresses" in value:
        import capo_pinpoint_email.types.email_address_list

        out["ReplyToAddresses"] = (
            capo_pinpoint_email.types.email_address_list.serialize_json(
                value["reply_to_addresses"]
            )
        )
    if "feedback_forwarding_email_address" in value:
        out["FeedbackForwardingEmailAddress"] = value[
            "feedback_forwarding_email_address"
        ]
    import capo_pinpoint_email.types.email_content

    out["Content"] = capo_pinpoint_email.types.email_content.serialize_json(
        value["content"]
    )
    if "email_tags" in value:
        import capo_pinpoint_email.types.message_tag_list

        out["EmailTags"] = capo_pinpoint_email.types.message_tag_list.serialize_json(
            value["email_tags"]
        )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> SendEmailRequest:
    out: SendEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    if data.get("Destination") is not None:
        import capo_pinpoint_email.types.destination

        out["destination"] = capo_pinpoint_email.types.destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("SendEmailRequest.destination required")
    if data.get("ReplyToAddresses") is not None:
        import capo_pinpoint_email.types.email_address_list

        out["reply_to_addresses"] = (
            capo_pinpoint_email.types.email_address_list.deserialize_json(
                data["ReplyToAddresses"]
            )
        )
    if data.get("FeedbackForwardingEmailAddress") is not None:
        out["feedback_forwarding_email_address"] = data[
            "FeedbackForwardingEmailAddress"
        ]
    if data.get("Content") is not None:
        import capo_pinpoint_email.types.email_content

        out["content"] = capo_pinpoint_email.types.email_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("SendEmailRequest.content required")
    if data.get("EmailTags") is not None:
        import capo_pinpoint_email.types.message_tag_list

        out["email_tags"] = capo_pinpoint_email.types.message_tag_list.deserialize_json(
            data["EmailTags"]
        )
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out

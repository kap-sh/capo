"""Generated from Smithy shape ``com.amazonaws.sesv2#SendEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.configuration_overrides
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.destination
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_address_list
    import capo_sesv2.types.email_content
    import capo_sesv2.types.endpoint_id
    import capo_sesv2.types.list_management_options
    import capo_sesv2.types.message_tag_list
    import capo_sesv2.types.tenant_name


class SendEmailRequest(TypedDict, closed=True):
    from_email_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address to use as the "From" address for the email. The address that you specify has to be verified. </p>"""
    from_email_address_identity_arn: NotRequired[
        "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FromEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the <code>FromEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FromEmailAddress</code> to be sender@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>For Raw emails, the <code>FromEmailAddressIdentityArn</code> value overrides the X-SES-SOURCE-ARN and X-SES-FROM-ARN headers specified in raw email message content.</p>"""
    destination: NotRequired["capo_sesv2.types.destination.Destination"]
    """<p>An object that contains the recipients of the email message.</p>"""
    reply_to_addresses: NotRequired[
        "capo_sesv2.types.email_address_list.EmailAddressList"
    ]
    """<p>The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.</p>"""
    feedback_forwarding_email_address: NotRequired[
        "capo_sesv2.types.email_address.EmailAddress"
    ]
    """<p>The address that you want bounce and complaint notifications to be sent to.</p>"""
    feedback_forwarding_email_address_identity_arn: NotRequired[
        "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FeedbackForwardingEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the <code>FeedbackForwardingEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FeedbackForwardingEmailAddress</code> to be feedback@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p>"""
    content: "capo_sesv2.types.email_content.EmailContent"
    """<p>An object that contains the body of the message. You can send either a Simple message, Raw message, or a Templated message.</p>"""
    email_tags: NotRequired["capo_sesv2.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. </p>"""
    configuration_set_name: NotRequired[
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set to use when sending the email.</p>"""
    endpoint_id: NotRequired["capo_sesv2.types.endpoint_id.EndpointId"]
    """<p>The ID of the multi-region endpoint (global-endpoint).</p>"""
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant through which this email will be sent.</p> <note> <p>The email sending operation will only succeed if all referenced resources (identities, configuration sets, and templates) are associated with this tenant. </p> </note>"""
    list_management_options: NotRequired[
        "capo_sesv2.types.list_management_options.ListManagementOptions"
    ]
    """<p>An object used to specify a list or topic to which an email belongs, which will be used when a contact chooses to unsubscribe.</p>"""
    configuration_overrides: NotRequired[
        "capo_sesv2.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>An object that overrides, for this message only, settings that would otherwise apply to it. Each setting that you don't override keeps the value that already applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEmailRequest) -> dict:
    out: dict = {}
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "from_email_address_identity_arn" in value:
        out["FromEmailAddressIdentityArn"] = value["from_email_address_identity_arn"]
    if "destination" in value:
        import capo_sesv2.types.destination

        out["Destination"] = capo_sesv2.types.destination.serialize_json(
            value["destination"]
        )
    if "reply_to_addresses" in value:
        import capo_sesv2.types.email_address_list

        out["ReplyToAddresses"] = capo_sesv2.types.email_address_list.serialize_json(
            value["reply_to_addresses"]
        )
    if "feedback_forwarding_email_address" in value:
        out["FeedbackForwardingEmailAddress"] = value[
            "feedback_forwarding_email_address"
        ]
    if "feedback_forwarding_email_address_identity_arn" in value:
        out["FeedbackForwardingEmailAddressIdentityArn"] = value[
            "feedback_forwarding_email_address_identity_arn"
        ]
    import capo_sesv2.types.email_content

    out["Content"] = capo_sesv2.types.email_content.serialize_json(value["content"])
    if "email_tags" in value:
        import capo_sesv2.types.message_tag_list

        out["EmailTags"] = capo_sesv2.types.message_tag_list.serialize_json(
            value["email_tags"]
        )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    if "list_management_options" in value:
        import capo_sesv2.types.list_management_options

        out["ListManagementOptions"] = (
            capo_sesv2.types.list_management_options.serialize_json(
                value["list_management_options"]
            )
        )
    if "configuration_overrides" in value:
        import capo_sesv2.types.configuration_overrides

        out["ConfigurationOverrides"] = (
            capo_sesv2.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendEmailRequest:
    out: SendEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    if data.get("FromEmailAddressIdentityArn") is not None:
        out["from_email_address_identity_arn"] = data["FromEmailAddressIdentityArn"]
    if data.get("Destination") is not None:
        import capo_sesv2.types.destination

        out["destination"] = capo_sesv2.types.destination.deserialize_json(
            data["Destination"]
        )
    if data.get("ReplyToAddresses") is not None:
        import capo_sesv2.types.email_address_list

        out["reply_to_addresses"] = (
            capo_sesv2.types.email_address_list.deserialize_json(
                data["ReplyToAddresses"]
            )
        )
    if data.get("FeedbackForwardingEmailAddress") is not None:
        out["feedback_forwarding_email_address"] = data[
            "FeedbackForwardingEmailAddress"
        ]
    if data.get("FeedbackForwardingEmailAddressIdentityArn") is not None:
        out["feedback_forwarding_email_address_identity_arn"] = data[
            "FeedbackForwardingEmailAddressIdentityArn"
        ]
    if data.get("Content") is not None:
        import capo_sesv2.types.email_content

        out["content"] = capo_sesv2.types.email_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("SendEmailRequest.content required")
    if data.get("EmailTags") is not None:
        import capo_sesv2.types.message_tag_list

        out["email_tags"] = capo_sesv2.types.message_tag_list.deserialize_json(
            data["EmailTags"]
        )
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("EndpointId") is not None:
        out["endpoint_id"] = data["EndpointId"]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    if data.get("ListManagementOptions") is not None:
        import capo_sesv2.types.list_management_options

        out["list_management_options"] = (
            capo_sesv2.types.list_management_options.deserialize_json(
                data["ListManagementOptions"]
            )
        )
    if data.get("ConfigurationOverrides") is not None:
        import capo_sesv2.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_sesv2.types.configuration_overrides.deserialize_json(
                data["ConfigurationOverrides"]
            )
        )
    return out

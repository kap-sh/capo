"""Generated from Smithy shape ``com.amazonaws.sesv2#SendBulkEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.bulk_email_content
    import capo_sesv2.types.bulk_email_entry_list
    import capo_sesv2.types.configuration_overrides
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_address_list
    import capo_sesv2.types.endpoint_id
    import capo_sesv2.types.message_tag_list
    import capo_sesv2.types.tenant_name


class SendBulkEmailRequest(TypedDict, closed=True):
    from_email_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address to use as the "From" address for the email. The address that you specify has to be verified.</p>"""
    from_email_address_identity_arn: NotRequired[
        "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FromEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the <code>FromEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FromEmailAddress</code> to be sender@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p>"""
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
    default_email_tags: NotRequired["capo_sesv2.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>"""
    default_content: "capo_sesv2.types.bulk_email_content.BulkEmailContent"
    """<p>An object that contains the body of the message. You can specify a template message.</p>"""
    bulk_email_entries: "capo_sesv2.types.bulk_email_entry_list.BulkEmailEntryList"
    """<p>The list of bulk email entry objects.</p>"""
    configuration_set_name: NotRequired[
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set to use when sending the email.</p>"""
    endpoint_id: NotRequired["capo_sesv2.types.endpoint_id.EndpointId"]
    """<p>The ID of the multi-region endpoint (global-endpoint).</p>"""
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant through which this bulk email will be sent.</p> <note> <p> The email sending operation will only succeed if all referenced resources (identities, configuration sets, and templates) are associated with this tenant. </p> </note>"""
    configuration_overrides: NotRequired[
        "capo_sesv2.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>An object that overrides, for the messages in this request only, settings that would otherwise apply to them. The overrides apply to every message in the request. Each setting that you don't override keeps the value that already applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendBulkEmailRequest) -> dict:
    out: dict = {}
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "from_email_address_identity_arn" in value:
        out["FromEmailAddressIdentityArn"] = value["from_email_address_identity_arn"]
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
    if "default_email_tags" in value:
        import capo_sesv2.types.message_tag_list

        out["DefaultEmailTags"] = capo_sesv2.types.message_tag_list.serialize_json(
            value["default_email_tags"]
        )
    import capo_sesv2.types.bulk_email_content

    out["DefaultContent"] = capo_sesv2.types.bulk_email_content.serialize_json(
        value["default_content"]
    )
    import capo_sesv2.types.bulk_email_entry_list

    out["BulkEmailEntries"] = capo_sesv2.types.bulk_email_entry_list.serialize_json(
        value["bulk_email_entries"]
    )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    if "configuration_overrides" in value:
        import capo_sesv2.types.configuration_overrides

        out["ConfigurationOverrides"] = (
            capo_sesv2.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendBulkEmailRequest:
    out: SendBulkEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    if data.get("FromEmailAddressIdentityArn") is not None:
        out["from_email_address_identity_arn"] = data["FromEmailAddressIdentityArn"]
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
    if data.get("DefaultEmailTags") is not None:
        import capo_sesv2.types.message_tag_list

        out["default_email_tags"] = capo_sesv2.types.message_tag_list.deserialize_json(
            data["DefaultEmailTags"]
        )
    if data.get("DefaultContent") is not None:
        import capo_sesv2.types.bulk_email_content

        out["default_content"] = capo_sesv2.types.bulk_email_content.deserialize_json(
            data["DefaultContent"]
        )
    else:
        raise DeserializationError("SendBulkEmailRequest.default_content required")
    if data.get("BulkEmailEntries") is not None:
        import capo_sesv2.types.bulk_email_entry_list

        out["bulk_email_entries"] = (
            capo_sesv2.types.bulk_email_entry_list.deserialize_json(
                data["BulkEmailEntries"]
            )
        )
    else:
        raise DeserializationError("SendBulkEmailRequest.bulk_email_entries required")
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("EndpointId") is not None:
        out["endpoint_id"] = data["EndpointId"]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    if data.get("ConfigurationOverrides") is not None:
        import capo_sesv2.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_sesv2.types.configuration_overrides.deserialize_json(
                data["ConfigurationOverrides"]
            )
        )
    return out

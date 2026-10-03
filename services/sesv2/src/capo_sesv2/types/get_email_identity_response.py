"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.dkim_attributes
    import capo_sesv2.types.enabled
    import capo_sesv2.types.identity_type
    import capo_sesv2.types.mail_from_attributes
    import capo_sesv2.types.policy_map
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.verification_info
    import capo_sesv2.types.verification_status


class GetEmailIdentityResponse(TypedDict, closed=True):
    identity_type: NotRequired["capo_sesv2.types.identity_type.IdentityType"]
    """<p>The email identity type. Note: the <code>MANAGED_DOMAIN</code> identity type is not supported.</p>"""
    feedback_forwarding_status: "capo_sesv2.types.enabled.Enabled"
    """<p>The feedback forwarding configuration for the identity.</p> <p>If the value is <code>true</code>, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the <code>Return-Path</code> header of the original email.</p> <p>You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).</p>"""
    verified_for_sending_status: "capo_sesv2.types.enabled.Enabled"
    """<p>Specifies whether or not the identity is verified. You can only send email from verified email addresses or domains. For more information about verifying identities, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html">Amazon Pinpoint User Guide</a>.</p>"""
    dkim_attributes: NotRequired["capo_sesv2.types.dkim_attributes.DkimAttributes"]
    """<p>An object that contains information about the DKIM attributes for the identity.</p>"""
    mail_from_attributes: NotRequired[
        "capo_sesv2.types.mail_from_attributes.MailFromAttributes"
    ]
    """<p>An object that contains information about the Mail-From attributes for the email identity.</p>"""
    policies: NotRequired["capo_sesv2.types.policy_map.PolicyMap"]
    """<p>A map of policy names to policies.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that are associated with the email identity.</p>"""
    configuration_set_name: NotRequired[
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The configuration set used by default when sending from this identity.</p>"""
    verification_status: NotRequired[
        "capo_sesv2.types.verification_status.VerificationStatus"
    ]
    """<p>The verification status of the identity. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – The verification process was initiated, but Amazon SES hasn't yet been able to verify the identity.</p> </li> <li> <p> <code>SUCCESS</code> – The verification process completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The verification process failed.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue is preventing Amazon SES from determining the verification status of the identity.</p> </li> <li> <p> <code>NOT_STARTED</code> – The verification process hasn't been initiated for the identity.</p> </li> </ul>"""
    verification_info: NotRequired[
        "capo_sesv2.types.verification_info.VerificationInfo"
    ]
    """<p>An object that contains additional information about the verification status for the identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailIdentityResponse) -> dict:
    out: dict = {}
    if "identity_type" in value:
        import capo_sesv2.types.identity_type

        out["IdentityType"] = capo_sesv2.types.identity_type.serialize_json(
            value["identity_type"]
        )
    out["FeedbackForwardingStatus"] = value.get("feedback_forwarding_status", False)
    out["VerifiedForSendingStatus"] = value.get("verified_for_sending_status", False)
    if "dkim_attributes" in value:
        import capo_sesv2.types.dkim_attributes

        out["DkimAttributes"] = capo_sesv2.types.dkim_attributes.serialize_json(
            value["dkim_attributes"]
        )
    if "mail_from_attributes" in value:
        import capo_sesv2.types.mail_from_attributes

        out["MailFromAttributes"] = (
            capo_sesv2.types.mail_from_attributes.serialize_json(
                value["mail_from_attributes"]
            )
        )
    if "policies" in value:
        import capo_sesv2.types.policy_map

        out["Policies"] = capo_sesv2.types.policy_map.serialize_json(value["policies"])
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "verification_status" in value:
        import capo_sesv2.types.verification_status

        out["VerificationStatus"] = capo_sesv2.types.verification_status.serialize_json(
            value["verification_status"]
        )
    if "verification_info" in value:
        import capo_sesv2.types.verification_info

        out["VerificationInfo"] = capo_sesv2.types.verification_info.serialize_json(
            value["verification_info"]
        )
    return out


def deserialize_json(data: dict) -> GetEmailIdentityResponse:
    out: GetEmailIdentityResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityType") is not None:
        import capo_sesv2.types.identity_type

        out["identity_type"] = capo_sesv2.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    if data.get("FeedbackForwardingStatus") is not None:
        out["feedback_forwarding_status"] = data["FeedbackForwardingStatus"]
    else:
        out["feedback_forwarding_status"] = False
    if data.get("VerifiedForSendingStatus") is not None:
        out["verified_for_sending_status"] = data["VerifiedForSendingStatus"]
    else:
        out["verified_for_sending_status"] = False
    if data.get("DkimAttributes") is not None:
        import capo_sesv2.types.dkim_attributes

        out["dkim_attributes"] = capo_sesv2.types.dkim_attributes.deserialize_json(
            data["DkimAttributes"]
        )
    if data.get("MailFromAttributes") is not None:
        import capo_sesv2.types.mail_from_attributes

        out["mail_from_attributes"] = (
            capo_sesv2.types.mail_from_attributes.deserialize_json(
                data["MailFromAttributes"]
            )
        )
    if data.get("Policies") is not None:
        import capo_sesv2.types.policy_map

        out["policies"] = capo_sesv2.types.policy_map.deserialize_json(data["Policies"])
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("VerificationStatus") is not None:
        import capo_sesv2.types.verification_status

        out["verification_status"] = (
            capo_sesv2.types.verification_status.deserialize_json(
                data["VerificationStatus"]
            )
        )
    if data.get("VerificationInfo") is not None:
        import capo_sesv2.types.verification_info

        out["verification_info"] = capo_sesv2.types.verification_info.deserialize_json(
            data["VerificationInfo"]
        )
    return out

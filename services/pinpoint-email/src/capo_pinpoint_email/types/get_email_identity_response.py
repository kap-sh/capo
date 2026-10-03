"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetEmailIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.dkim_attributes
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.identity_type
    import capo_pinpoint_email.types.mail_from_attributes
    import capo_pinpoint_email.types.tag_list


class GetEmailIdentityResponse(TypedDict, closed=True):
    identity_type: NotRequired["capo_pinpoint_email.types.identity_type.IdentityType"]
    """<p>The email identity type.</p>"""
    feedback_forwarding_status: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>The feedback forwarding configuration for the identity.</p> <p>If the value is <code>true</code>, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.</p> <p>When you set this value to <code>false</code>, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).</p>"""
    verified_for_sending_status: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html">Amazon Pinpoint User Guide</a>.</p>"""
    dkim_attributes: NotRequired[
        "capo_pinpoint_email.types.dkim_attributes.DkimAttributes"
    ]
    """<p>An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.</p>"""
    mail_from_attributes: NotRequired[
        "capo_pinpoint_email.types.mail_from_attributes.MailFromAttributes"
    ]
    """<p>An object that contains information about the Mail-From attributes for the email identity.</p>"""
    tags: NotRequired["capo_pinpoint_email.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that are associated with the email identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailIdentityResponse) -> dict:
    out: dict = {}
    if "identity_type" in value:
        import capo_pinpoint_email.types.identity_type

        out["IdentityType"] = capo_pinpoint_email.types.identity_type.serialize_json(
            value["identity_type"]
        )
    out["FeedbackForwardingStatus"] = value.get("feedback_forwarding_status", False)
    out["VerifiedForSendingStatus"] = value.get("verified_for_sending_status", False)
    if "dkim_attributes" in value:
        import capo_pinpoint_email.types.dkim_attributes

        out["DkimAttributes"] = (
            capo_pinpoint_email.types.dkim_attributes.serialize_json(
                value["dkim_attributes"]
            )
        )
    if "mail_from_attributes" in value:
        import capo_pinpoint_email.types.mail_from_attributes

        out["MailFromAttributes"] = (
            capo_pinpoint_email.types.mail_from_attributes.serialize_json(
                value["mail_from_attributes"]
            )
        )
    if "tags" in value:
        import capo_pinpoint_email.types.tag_list

        out["Tags"] = capo_pinpoint_email.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetEmailIdentityResponse:
    out: GetEmailIdentityResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityType") is not None:
        import capo_pinpoint_email.types.identity_type

        out["identity_type"] = capo_pinpoint_email.types.identity_type.deserialize_json(
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
        import capo_pinpoint_email.types.dkim_attributes

        out["dkim_attributes"] = (
            capo_pinpoint_email.types.dkim_attributes.deserialize_json(
                data["DkimAttributes"]
            )
        )
    if data.get("MailFromAttributes") is not None:
        import capo_pinpoint_email.types.mail_from_attributes

        out["mail_from_attributes"] = (
            capo_pinpoint_email.types.mail_from_attributes.deserialize_json(
                data["MailFromAttributes"]
            )
        )
    if data.get("Tags") is not None:
        import capo_pinpoint_email.types.tag_list

        out["tags"] = capo_pinpoint_email.types.tag_list.deserialize_json(data["Tags"])
    return out

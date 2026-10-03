"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutEmailIdentityMailFromAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.behavior_on_mx_failure
    import capo_pinpoint_email.types.identity
    import capo_pinpoint_email.types.mail_from_domain_name


class PutEmailIdentityMailFromAttributesRequest(TypedDict, closed=True):
    email_identity: "capo_pinpoint_email.types.identity.Identity"
    """<p>The verified email identity that you want to set up the custom MAIL FROM domain for.</p>"""
    mail_from_domain: NotRequired[
        "capo_pinpoint_email.types.mail_from_domain_name.MailFromDomainName"
    ]
    """<p> The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:</p> <ul> <li> <p>It has to be a subdomain of the verified identity.</p> </li> <li> <p>It can't be used to receive email.</p> </li> <li> <p>It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails.</p> </li> </ul>"""
    behavior_on_mx_failure: NotRequired[
        "capo_pinpoint_email.types.behavior_on_mx_failure.BehaviorOnMxFailure"
    ]
    """<p>The action that you want Amazon Pinpoint to take if it can't read the required MX record when you send an email. When you set this value to <code>UseDefaultValue</code>, Amazon Pinpoint uses <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>RejectMessage</code>, Amazon Pinpoint returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityMailFromAttributesRequest) -> dict:
    out: dict = {}
    if "mail_from_domain" in value:
        out["MailFromDomain"] = value["mail_from_domain"]
    if "behavior_on_mx_failure" in value:
        import capo_pinpoint_email.types.behavior_on_mx_failure

        out["BehaviorOnMxFailure"] = (
            capo_pinpoint_email.types.behavior_on_mx_failure.serialize_json(
                value["behavior_on_mx_failure"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutEmailIdentityMailFromAttributesRequest:
    out: PutEmailIdentityMailFromAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MailFromDomain") is not None:
        out["mail_from_domain"] = data["MailFromDomain"]
    if data.get("BehaviorOnMxFailure") is not None:
        import capo_pinpoint_email.types.behavior_on_mx_failure

        out["behavior_on_mx_failure"] = (
            capo_pinpoint_email.types.behavior_on_mx_failure.deserialize_json(
                data["BehaviorOnMxFailure"]
            )
        )
    return out

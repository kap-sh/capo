"""Generated from Smithy shape ``com.amazonaws.pinpointemail#MailFromAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.behavior_on_mx_failure
    import capo_pinpoint_email.types.mail_from_domain_name
    import capo_pinpoint_email.types.mail_from_domain_status


class MailFromAttributes(TypedDict, closed=True):
    mail_from_domain: (
        "capo_pinpoint_email.types.mail_from_domain_name.MailFromDomainName"
    )
    """<p>The name of a domain that an email identity uses as a custom MAIL FROM domain.</p>"""
    mail_from_domain_status: (
        "capo_pinpoint_email.types.mail_from_domain_status.MailFromDomainStatus"
    )
    """<p>The status of the MAIL FROM domain. This status can have the following values:</p> <ul> <li> <p> <code>PENDING</code> – Amazon Pinpoint hasn't started searching for the MX record yet.</p> </li> <li> <p> <code>SUCCESS</code> – Amazon Pinpoint detected the required MX record for the MAIL FROM domain.</p> </li> <li> <p> <code>FAILED</code> – Amazon Pinpoint can't find the required MX record, or the record no longer exists.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue occurred, which prevented Amazon Pinpoint from determining the status of the MAIL FROM domain.</p> </li> </ul>"""
    behavior_on_mx_failure: (
        "capo_pinpoint_email.types.behavior_on_mx_failure.BehaviorOnMxFailure"
    )
    """<p>The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain. When you set this value to <code>UseDefaultValue</code>, Amazon Pinpoint uses <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>RejectMessage</code>, Amazon Pinpoint returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MailFromAttributes) -> dict:
    out: dict = {}
    out["MailFromDomain"] = value["mail_from_domain"]
    import capo_pinpoint_email.types.mail_from_domain_status

    out["MailFromDomainStatus"] = (
        capo_pinpoint_email.types.mail_from_domain_status.serialize_json(
            value["mail_from_domain_status"]
        )
    )
    import capo_pinpoint_email.types.behavior_on_mx_failure

    out["BehaviorOnMxFailure"] = (
        capo_pinpoint_email.types.behavior_on_mx_failure.serialize_json(
            value["behavior_on_mx_failure"]
        )
    )
    return out


def deserialize_json(data: dict) -> MailFromAttributes:
    out: MailFromAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MailFromDomain") is not None:
        out["mail_from_domain"] = data["MailFromDomain"]
    else:
        out["mail_from_domain"] = ""
    if data.get("MailFromDomainStatus") is not None:
        import capo_pinpoint_email.types.mail_from_domain_status

        out["mail_from_domain_status"] = (
            capo_pinpoint_email.types.mail_from_domain_status.deserialize_json(
                data["MailFromDomainStatus"]
            )
        )
    else:
        import typing

        out["mail_from_domain_status"] = typing.cast(
            "capo_pinpoint_email.types.mail_from_domain_status.MailFromDomainStatus", ""
        )
    if data.get("BehaviorOnMxFailure") is not None:
        import capo_pinpoint_email.types.behavior_on_mx_failure

        out["behavior_on_mx_failure"] = (
            capo_pinpoint_email.types.behavior_on_mx_failure.deserialize_json(
                data["BehaviorOnMxFailure"]
            )
        )
    else:
        import typing

        out["behavior_on_mx_failure"] = typing.cast(
            "capo_pinpoint_email.types.behavior_on_mx_failure.BehaviorOnMxFailure", ""
        )
    return out

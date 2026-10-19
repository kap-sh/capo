"""Generated from Smithy shape ``com.amazonaws.sesv2#MailFromAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.behavior_on_mx_failure
    import capo_sesv2.types.mail_from_domain_name
    import capo_sesv2.types.mail_from_domain_status


class MailFromAttributes(TypedDict, closed=True):
    mail_from_domain: "capo_sesv2.types.mail_from_domain_name.MailFromDomainName"
    """<p>The name of a domain that an email identity uses as a custom MAIL FROM domain.</p>"""
    mail_from_domain_status: (
        "capo_sesv2.types.mail_from_domain_status.MailFromDomainStatus"
    )
    """<p>The status of the MAIL FROM domain. This status can have the following values:</p> <ul> <li> <p> <code>PENDING</code> – Amazon SES hasn't started searching for the MX record yet.</p> </li> <li> <p> <code>SUCCESS</code> – Amazon SES detected the required MX record for the MAIL FROM domain.</p> </li> <li> <p> <code>FAILED</code> – Amazon SES can't find the required MX record, or the record no longer exists.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue occurred, which prevented Amazon SES from determining the status of the MAIL FROM domain.</p> </li> </ul>"""
    behavior_on_mx_failure: (
        "capo_sesv2.types.behavior_on_mx_failure.BehaviorOnMxFailure"
    )
    """<p>The action to take if the required MX record can't be found when you send an email. When you set this value to <code>USE_DEFAULT_VALUE</code>, the mail is sent using <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>REJECT_MESSAGE</code>, the Amazon SES API v2 returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MailFromAttributes) -> dict:
    out: dict = {}
    out["MailFromDomain"] = value["mail_from_domain"]
    import capo_sesv2.types.mail_from_domain_status

    out["MailFromDomainStatus"] = (
        capo_sesv2.types.mail_from_domain_status.serialize_json(
            value["mail_from_domain_status"]
        )
    )
    import capo_sesv2.types.behavior_on_mx_failure

    out["BehaviorOnMxFailure"] = capo_sesv2.types.behavior_on_mx_failure.serialize_json(
        value["behavior_on_mx_failure"]
    )
    return out


def deserialize_json(data: dict) -> MailFromAttributes:
    out: MailFromAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MailFromDomain") is not None:
        out["mail_from_domain"] = data["MailFromDomain"]
    else:
        out["mail_from_domain"] = ""
    if data.get("MailFromDomainStatus") is not None:
        import capo_sesv2.types.mail_from_domain_status

        out["mail_from_domain_status"] = (
            capo_sesv2.types.mail_from_domain_status.deserialize_json(
                data["MailFromDomainStatus"]
            )
        )
    else:
        import typing

        out["mail_from_domain_status"] = typing.cast(
            "capo_sesv2.types.mail_from_domain_status.MailFromDomainStatus", ""
        )
    if data.get("BehaviorOnMxFailure") is not None:
        import capo_sesv2.types.behavior_on_mx_failure

        out["behavior_on_mx_failure"] = (
            capo_sesv2.types.behavior_on_mx_failure.deserialize_json(
                data["BehaviorOnMxFailure"]
            )
        )
    else:
        import typing

        out["behavior_on_mx_failure"] = typing.cast(
            "capo_sesv2.types.behavior_on_mx_failure.BehaviorOnMxFailure", ""
        )
    return out

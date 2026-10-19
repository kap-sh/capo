"""Generated from Smithy shape ``com.amazonaws.ses#IdentityMailFromDomainAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.behavior_on_mx_failure
    import capo_ses.types.custom_mail_from_status
    import capo_ses.types.mail_from_domain_name


class IdentityMailFromDomainAttributes(TypedDict, closed=True):
    mail_from_domain: "capo_ses.types.mail_from_domain_name.MailFromDomainName"
    """<p>The custom MAIL FROM domain that the identity is configured to use.</p>"""
    mail_from_domain_status: (
        "capo_ses.types.custom_mail_from_status.CustomMailFromStatus"
    )
    """<p>The state that indicates whether Amazon SES has successfully read the MX record required for custom MAIL FROM domain setup. If the state is <code>Success</code>, Amazon SES uses the specified custom MAIL FROM domain when the verified identity sends an email. All other states indicate that Amazon SES takes the action described by <code>BehaviorOnMXFailure</code>.</p>"""
    behavior_on_mx_failure: "capo_ses.types.behavior_on_mx_failure.BehaviorOnMXFailure"
    """<p>The action that Amazon SES takes if it cannot successfully read the required MX record when you send an email. A value of <code>UseDefaultValue</code> indicates that if Amazon SES cannot read the required MX record, it uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. A value of <code>RejectMessage</code> indicates that if Amazon SES cannot read the required MX record, Amazon SES returns a <code>MailFromDomainNotVerified</code> error and does not send the email.</p> <p>The custom MAIL FROM setup states that result in this behavior are <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IdentityMailFromDomainAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}MailFromDomain", str(value["mail_from_domain"])))
    import capo_ses.types.custom_mail_from_status

    capo_ses.types.custom_mail_from_status.serialize_query(
        value["mail_from_domain_status"], pairs, f"{key_prefix}MailFromDomainStatus"
    )
    import capo_ses.types.behavior_on_mx_failure

    capo_ses.types.behavior_on_mx_failure.serialize_query(
        value["behavior_on_mx_failure"], pairs, f"{key_prefix}BehaviorOnMXFailure"
    )


def deserialize_query(el: Element) -> IdentityMailFromDomainAttributes:
    out: IdentityMailFromDomainAttributes = {}  # type: ignore[typeddict-item]
    child_mail_from_domain = el.find("MailFromDomain")
    if child_mail_from_domain is not None:
        out["mail_from_domain"] = str(child_mail_from_domain.text or "")
    else:
        out["mail_from_domain"] = ""
    child_mail_from_domain_status = el.find("MailFromDomainStatus")
    if child_mail_from_domain_status is not None:
        import capo_ses.types.custom_mail_from_status

        out["mail_from_domain_status"] = (
            capo_ses.types.custom_mail_from_status.deserialize_query(
                child_mail_from_domain_status
            )
        )
    else:
        import typing

        out["mail_from_domain_status"] = typing.cast(
            "capo_ses.types.custom_mail_from_status.CustomMailFromStatus", ""
        )
    child_behavior_on_mx_failure = el.find("BehaviorOnMXFailure")
    if child_behavior_on_mx_failure is not None:
        import capo_ses.types.behavior_on_mx_failure

        out["behavior_on_mx_failure"] = (
            capo_ses.types.behavior_on_mx_failure.deserialize_query(
                child_behavior_on_mx_failure
            )
        )
    else:
        import typing

        out["behavior_on_mx_failure"] = typing.cast(
            "capo_ses.types.behavior_on_mx_failure.BehaviorOnMXFailure", ""
        )
    return out

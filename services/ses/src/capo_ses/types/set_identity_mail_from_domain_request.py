"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityMailFromDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.behavior_on_mx_failure
    import capo_ses.types.identity
    import capo_ses.types.mail_from_domain_name


class SetIdentityMailFromDomainRequest(TypedDict, closed=True):
    identity: "capo_ses.types.identity.Identity"
    """<p>The verified identity.</p>"""
    mail_from_domain: NotRequired[
        "capo_ses.types.mail_from_domain_name.MailFromDomainName"
    ]
    """<p>The custom MAIL FROM domain for the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a "From" address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/mail-from.html">Amazon SES Developer Guide</a>), and 3) not be used to receive emails. A value of <code>null</code> disables the custom MAIL FROM setting for the identity.</p>"""
    behavior_on_mx_failure: NotRequired[
        "capo_ses.types.behavior_on_mx_failure.BehaviorOnMXFailure"
    ]
    """<p>The action for Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose <code>UseDefaultValue</code>, Amazon SES uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose <code>RejectMessage</code>, Amazon SES returns a <code>MailFromDomainNotVerified</code> error and not send the email.</p> <p>The action specified in <code>BehaviorOnMXFailure</code> is taken when the custom MAIL FROM domain setup is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityMailFromDomainRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Identity", str(value["identity"])))
    if "mail_from_domain" in value:
        pairs.append((f"{key_prefix}MailFromDomain", str(value["mail_from_domain"])))
    if "behavior_on_mx_failure" in value:
        import capo_ses.types.behavior_on_mx_failure

        capo_ses.types.behavior_on_mx_failure.serialize_query(
            value["behavior_on_mx_failure"], pairs, f"{key_prefix}BehaviorOnMXFailure"
        )


def deserialize_query(el: Element) -> SetIdentityMailFromDomainRequest:
    out: SetIdentityMailFromDomainRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError("SetIdentityMailFromDomainRequest.identity required")
    child_mail_from_domain = el.find("MailFromDomain")
    if child_mail_from_domain is not None:
        out["mail_from_domain"] = str(child_mail_from_domain.text or "")
    child_behavior_on_mx_failure = el.find("BehaviorOnMXFailure")
    if child_behavior_on_mx_failure is not None:
        import capo_ses.types.behavior_on_mx_failure

        out["behavior_on_mx_failure"] = (
            capo_ses.types.behavior_on_mx_failure.deserialize_query(
                child_behavior_on_mx_failure
            )
        )
    return out

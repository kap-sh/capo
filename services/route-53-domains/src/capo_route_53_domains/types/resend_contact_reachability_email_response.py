"""Generated from Smithy shape ``com.amazonaws.route53domains#ResendContactReachabilityEmailResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.boolean
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.email


class ResendContactReachabilityEmailResponse(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The domain name for which you requested a confirmation email.</p>"""
    email_address: NotRequired["capo_route_53_domains.types.email.Email"]
    """<p>The email address for the registrant contact at the time that we sent the verification email.</p>"""
    is_already_verified: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p> <code>True</code> if the email address for the registrant contact has already been verified, and <code>false</code> otherwise. If the email address has already been verified, we don't send another confirmation email.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResendContactReachabilityEmailResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "is_already_verified" in value:
        out["isAlreadyVerified"] = value["is_already_verified"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResendContactReachabilityEmailResponse:
    out: ResendContactReachabilityEmailResponse = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    if data.get("isAlreadyVerified") is not None:
        out["is_already_verified"] = data["isAlreadyVerified"]
    return out


def redact_sensitive(value: ResendContactReachabilityEmailResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out

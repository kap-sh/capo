"""Generated from Smithy shape ``com.amazonaws.sesv2#AssociateEmailIdentityCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.certificate_arn
    import capo_sesv2.types.email_address
    import capo_sesv2.types.identity


class AssociateEmailIdentityCertificateRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity, either an email address or a domain, to associate the certificate with.</p>"""
    from_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address that the certificate applies to. This value is required when the email identity is a domain, and the address must belong to that domain or one of its subdomains. When the email identity is an email address, this value is optional. If you specify it, it must exactly match the email identity.</p>"""
    certificate_arn: "capo_sesv2.types.certificate_arn.CertificateArn"
    """<p>The Amazon Resource Name (ARN) of the Certificate Manager (ACM) certificate to associate with the email identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEmailIdentityCertificateRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_json(data: dict) -> AssociateEmailIdentityCertificateRequest:
    out: AssociateEmailIdentityCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailIdentity") is not None:
        out["email_identity"] = data["EmailIdentity"]
    else:
        out["email_identity"] = ""
    if data.get("FromAddress") is not None:
        out["from_address"] = data["FromAddress"]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        out["certificate_arn"] = ""
    return out

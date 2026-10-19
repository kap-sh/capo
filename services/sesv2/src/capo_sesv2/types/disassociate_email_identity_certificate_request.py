"""Generated from Smithy shape ``com.amazonaws.sesv2#DisassociateEmailIdentityCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.identity


class DisassociateEmailIdentityCertificateRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity whose certificate association you want to remove.</p>"""
    from_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address whose certificate association you want to remove. This value is required when the email identity is a domain. When the email identity is an email address, this value is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateEmailIdentityCertificateRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    return out


def deserialize_json(data: dict) -> DisassociateEmailIdentityCertificateRequest:
    out: DisassociateEmailIdentityCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailIdentity") is not None:
        out["email_identity"] = data["EmailIdentity"]
    else:
        out["email_identity"] = ""
    if data.get("FromAddress") is not None:
        out["from_address"] = data["FromAddress"]
    return out

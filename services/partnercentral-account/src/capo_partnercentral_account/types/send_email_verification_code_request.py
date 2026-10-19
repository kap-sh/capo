"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#SendEmailVerificationCodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.email


class SendEmailVerificationCodeRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    email: "capo_partnercentral_account.types.email.Email"
    """<p>The email address to send the verification code to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendEmailVerificationCodeRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendEmailVerificationCodeRequest:
    out: SendEmailVerificationCodeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        out["email"] = ""
    return out

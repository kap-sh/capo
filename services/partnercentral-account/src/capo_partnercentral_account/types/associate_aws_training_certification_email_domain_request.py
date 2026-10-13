"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AssociateAwsTrainingCertificationEmailDomainRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.email_verification_code
    import capo_partnercentral_account.types.partner_identifier


class AssociateAwsTrainingCertificationEmailDomainRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>The unique identifier of the partner account.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    email: "capo_partnercentral_account.types.email.Email"
    """<p>The email address used to verify domain ownership for AWS training and certification association.</p>"""
    email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode"
    """<p>The verification code sent to the email address to confirm domain ownership.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: AssociateAwsTrainingCertificationEmailDomainRequest,
) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Email"] = value["email"]
    out["EmailVerificationCode"] = value["email_verification_code"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> AssociateAwsTrainingCertificationEmailDomainRequest:
    out: AssociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.catalog required"
        )
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.identifier required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.email required"
        )
    if data.get("EmailVerificationCode") is not None:
        out["email_verification_code"] = data["EmailVerificationCode"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.email_verification_code required"
        )
    return out


def redact_sensitive(
    value: AssociateAwsTrainingCertificationEmailDomainRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_verification_code" in value:
        out["email_verification_code"] = "*** Sensitive Data Redacted ***"
    return out

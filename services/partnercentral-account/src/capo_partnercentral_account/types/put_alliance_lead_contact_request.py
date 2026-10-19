"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PutAllianceLeadContactRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.alliance_lead_contact
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.email_verification_code
    import capo_partnercentral_account.types.partner_identifier


class PutAllianceLeadContactRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>The unique identifier of the partner account.</p>"""
    alliance_lead_contact: (
        "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The alliance lead contact information to set for the partner account.</p>"""
    email_verification_code: NotRequired[
        "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode"
    ]
    """<p>The verification code sent to the alliance lead contact's email to confirm the update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAllianceLeadContactRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import capo_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        capo_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    if "email_verification_code" in value:
        out["EmailVerificationCode"] = value["email_verification_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAllianceLeadContactRequest:
    out: PutAllianceLeadContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("AllianceLeadContact") is not None:
        import capo_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            capo_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "PutAllianceLeadContactRequest.alliance_lead_contact required"
        )
    if data.get("EmailVerificationCode") is not None:
        out["email_verification_code"] = data["EmailVerificationCode"]
    return out


def redact_sensitive(value: PutAllianceLeadContactRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alliance_lead_contact" in value:
        import capo_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            capo_partnercentral_account.types.alliance_lead_contact.redact_sensitive(
                value["alliance_lead_contact"]
            )
        )
    if "email_verification_code" in value:
        out["email_verification_code"] = "*** Sensitive Data Redacted ***"
    return out

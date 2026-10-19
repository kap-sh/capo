"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CreatePartnerRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.alliance_lead_contact
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.email_verification_code
    import capo_partnercentral_account.types.primary_solution_type
    import capo_partnercentral_account.types.sensitive_unicode_string
    import capo_partnercentral_account.types.tag_list


class CreatePartnerRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the partner account will be created.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    legal_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The legal name of the organization becoming a partner.</p>"""
    primary_solution_type: (
        "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType"
    )
    """<p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>"""
    alliance_lead_contact: (
        "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The primary contact person for alliance and partnership matters.</p>"""
    email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode"
    """<p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>"""
    tags: NotRequired["capo_partnercentral_account.types.tag_list.TagList"]
    """<p>A list of tags to associate with the partner account for organization and billing purposes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePartnerRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["LegalName"] = value["legal_name"]
    import capo_partnercentral_account.types.primary_solution_type

    out["PrimarySolutionType"] = (
        capo_partnercentral_account.types.primary_solution_type.serialize_aws_json_1_0(
            value["primary_solution_type"]
        )
    )
    import capo_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        capo_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    out["EmailVerificationCode"] = value["email_verification_code"]
    if "tags" in value:
        import capo_partnercentral_account.types.tag_list

        out["Tags"] = capo_partnercentral_account.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePartnerRequest:
    out: CreatePartnerRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("LegalName") is not None:
        out["legal_name"] = data["LegalName"]
    else:
        out["legal_name"] = ""
    if data.get("PrimarySolutionType") is not None:
        import capo_partnercentral_account.types.primary_solution_type

        out["primary_solution_type"] = (
            capo_partnercentral_account.types.primary_solution_type.deserialize_aws_json_1_0(
                data["PrimarySolutionType"]
            )
        )
    else:
        import typing

        out["primary_solution_type"] = typing.cast(
            "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
            "",
        )
    if data.get("AllianceLeadContact") is not None:
        import capo_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            capo_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePartnerRequest.alliance_lead_contact required"
        )
    if data.get("EmailVerificationCode") is not None:
        out["email_verification_code"] = data["EmailVerificationCode"]
    else:
        out["email_verification_code"] = ""
    if data.get("Tags") is not None:
        import capo_partnercentral_account.types.tag_list

        out["tags"] = (
            capo_partnercentral_account.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out


def redact_sensitive(value: CreatePartnerRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "legal_name" in value:
        out["legal_name"] = "*** Sensitive Data Redacted ***"
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

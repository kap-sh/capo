"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetAllianceLeadContactResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.alliance_lead_contact
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id


class GetAllianceLeadContactResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    alliance_lead_contact: (
        "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The alliance lead contact information including name, email, and business title.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAllianceLeadContactResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    import capo_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        capo_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAllianceLeadContactResponse:
    out: GetAllianceLeadContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("AllianceLeadContact") is not None:
        import capo_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            capo_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "GetAllianceLeadContactResponse.alliance_lead_contact required"
        )
    return out


def redact_sensitive(value: GetAllianceLeadContactResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alliance_lead_contact" in value:
        import capo_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            capo_partnercentral_account.types.alliance_lead_contact.redact_sensitive(
                value["alliance_lead_contact"]
            )
        )
    return out

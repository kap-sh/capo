"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateOpportunityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.opportunity_identifier


class CreateOpportunityResponse(TypedDict, closed=True):
    id: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    """<p>Read-only, system-generated <code>Opportunity</code> unique identifier. Amazon Web Services creates this identifier, and it's used for all subsequent opportunity actions, such as updates, associations, and submissions. It helps to ensure that each opportunity is accurately tracked and managed.</p>"""
    partner_opportunity_identifier: NotRequired["str"]
    """<p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.</p>"""
    last_modified_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p> <code>DateTime</code> when the opportunity was last modified. When the <code>Opportunity</code> is created, its value is <code>CreatedDate</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOpportunityResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "partner_opportunity_identifier" in value:
        out["PartnerOpportunityIdentifier"] = value["partner_opportunity_identifier"]
    if "last_modified_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["LastModifiedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOpportunityResponse:
    out: CreateOpportunityResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("PartnerOpportunityIdentifier") is not None:
        out["partner_opportunity_identifier"] = data["PartnerOpportunityIdentifier"]
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["last_modified_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    return out

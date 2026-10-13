"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.customer_summary
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.life_cycle_summary
    import capo_partnercentral_selling.types.opportunity_arn
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.opportunity_type
    import capo_partnercentral_selling.types.project_summary


class OpportunitySummary(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the opportunity, either <code>AWS</code> or <code>Sandbox</code>. This indicates the environment in which the opportunity is managed.</p>"""
    id: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Read-only, system-generated <code>Opportunity</code> unique identifier.</p>"""
    arn: NotRequired["capo_partnercentral_selling.types.opportunity_arn.OpportunityArn"]
    """<p> The Amazon Resource Name (ARN) for the opportunity. This globally unique identifier can be used for IAM policies and cross-service references. </p>"""
    partner_opportunity_identifier: NotRequired["str"]
    """<p>Specifies the <code>Opportunity</code>'s unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner. It allows partners to link an opportunity to their CRM.</p>"""
    opportunity_type: NotRequired[
        "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
    ]
    """<p>Specifies opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New Opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal Opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion Opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>"""
    last_modified_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p> <code>DateTime</code> when the <code>Opportunity</code> was last modified.</p>"""
    created_date: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p> <code>DateTime</code> when the <code>Opportunity</code> was last created.</p>"""
    life_cycle: NotRequired[
        "capo_partnercentral_selling.types.life_cycle_summary.LifeCycleSummary"
    ]
    """<p>An object that contains the <code>Opportunity</code>'s lifecycle details.</p>"""
    customer: NotRequired[
        "capo_partnercentral_selling.types.customer_summary.CustomerSummary"
    ]
    """<p>An object that contains the <code>Opportunity</code>'s customer details.</p>"""
    project: NotRequired[
        "capo_partnercentral_selling.types.project_summary.ProjectSummary"
    ]
    """<p>An object that contains the <code>Opportunity</code>'s project details summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySummary) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "partner_opportunity_identifier" in value:
        out["PartnerOpportunityIdentifier"] = value["partner_opportunity_identifier"]
    if "opportunity_type" in value:
        import capo_partnercentral_selling.types.opportunity_type

        out["OpportunityType"] = (
            capo_partnercentral_selling.types.opportunity_type.serialize_aws_json_1_0(
                value["opportunity_type"]
            )
        )
    if "last_modified_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["LastModifiedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["last_modified_date"]
            )
        )
    if "created_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["CreatedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["created_date"]
            )
        )
    if "life_cycle" in value:
        import capo_partnercentral_selling.types.life_cycle_summary

        out["LifeCycle"] = (
            capo_partnercentral_selling.types.life_cycle_summary.serialize_aws_json_1_0(
                value["life_cycle"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.customer_summary

        out["Customer"] = (
            capo_partnercentral_selling.types.customer_summary.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.project_summary

        out["Project"] = (
            capo_partnercentral_selling.types.project_summary.serialize_aws_json_1_0(
                value["project"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunitySummary:
    out: OpportunitySummary = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("OpportunitySummary.catalog required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("PartnerOpportunityIdentifier") is not None:
        out["partner_opportunity_identifier"] = data["PartnerOpportunityIdentifier"]
    if data.get("OpportunityType") is not None:
        import capo_partnercentral_selling.types.opportunity_type

        out["opportunity_type"] = (
            capo_partnercentral_selling.types.opportunity_type.deserialize_aws_json_1_0(
                data["OpportunityType"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["last_modified_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    if data.get("CreatedDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["created_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    if data.get("LifeCycle") is not None:
        import capo_partnercentral_selling.types.life_cycle_summary

        out["life_cycle"] = (
            capo_partnercentral_selling.types.life_cycle_summary.deserialize_aws_json_1_0(
                data["LifeCycle"]
            )
        )
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.customer_summary

        out["customer"] = (
            capo_partnercentral_selling.types.customer_summary.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Project") is not None:
        import capo_partnercentral_selling.types.project_summary

        out["project"] = (
            capo_partnercentral_selling.types.project_summary.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    return out


def redact_sensitive(value: OpportunitySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "life_cycle" in value:
        import capo_partnercentral_selling.types.life_cycle_summary

        out["life_cycle"] = (
            capo_partnercentral_selling.types.life_cycle_summary.redact_sensitive(
                value["life_cycle"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.customer_summary

        out["customer"] = (
            capo_partnercentral_selling.types.customer_summary.redact_sensitive(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.project_summary

        out["project"] = (
            capo_partnercentral_selling.types.project_summary.redact_sensitive(
                value["project"]
            )
        )
    return out

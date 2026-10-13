"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunitySummaryFullView``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_opportunity_customer
    import capo_partnercentral_selling.types.aws_opportunity_insights
    import capo_partnercentral_selling.types.aws_opportunity_life_cycle
    import capo_partnercentral_selling.types.aws_opportunity_project
    import capo_partnercentral_selling.types.aws_opportunity_related_entities
    import capo_partnercentral_selling.types.aws_opportunity_team_members_list
    import capo_partnercentral_selling.types.aws_software_revenue
    import capo_partnercentral_selling.types.involvement_type_change_reason
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.opportunity_origin
    import capo_partnercentral_selling.types.sales_involvement_type
    import capo_partnercentral_selling.types.visibility


class AwsOpportunitySummaryFullView(TypedDict, closed=True):
    related_opportunity_id: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Identifier of the related partner opportunity.</p>"""
    origin: NotRequired[
        "capo_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
    ]
    """<p>Source origin of the AWS opportunity.</p>"""
    involvement_type: NotRequired[
        "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    ]
    """<p>Type of AWS involvement in the opportunity.</p>"""
    visibility: NotRequired["capo_partnercentral_selling.types.visibility.Visibility"]
    """<p>Visibility level for the AWS opportunity.</p>"""
    life_cycle: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_life_cycle.AwsOpportunityLifeCycle"
    ]
    opportunity_team: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_team_members_list.AwsOpportunityTeamMembersList"
    ]
    """<p>AWS team members involved in the opportunity.</p>"""
    insights: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_insights.AwsOpportunityInsights"
    ]
    involvement_type_change_reason: NotRequired[
        "capo_partnercentral_selling.types.involvement_type_change_reason.InvolvementTypeChangeReason"
    ]
    """<p>Reason for changes in AWS involvement type for the opportunity.</p>"""
    related_entity_ids: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_related_entities.AwsOpportunityRelatedEntities"
    ]
    customer: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_customer.AwsOpportunityCustomer"
    ]
    project: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_project.AwsOpportunityProject"
    ]
    cosell_motion: NotRequired["str"]
    """<p>Engagement classification for this opportunity. Read-only. Null before scoring. Known values: <code>AWS Field-engaged</code>, <code>Agent-engaged</code>, <code>Partner-led</code>.</p>"""
    software_revenue: NotRequired[
        "capo_partnercentral_selling.types.aws_software_revenue.AwsSoftwareRevenue"
    ]
    """<p>Seller-provided PARC deal terms: commitment value, discount, and contract dates.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunitySummaryFullView) -> dict:
    out: dict = {}
    if "related_opportunity_id" in value:
        out["RelatedOpportunityId"] = value["related_opportunity_id"]
    if "origin" in value:
        import capo_partnercentral_selling.types.opportunity_origin

        out["Origin"] = (
            capo_partnercentral_selling.types.opportunity_origin.serialize_aws_json_1_0(
                value["origin"]
            )
        )
    if "involvement_type" in value:
        import capo_partnercentral_selling.types.sales_involvement_type

        out["InvolvementType"] = (
            capo_partnercentral_selling.types.sales_involvement_type.serialize_aws_json_1_0(
                value["involvement_type"]
            )
        )
    if "visibility" in value:
        import capo_partnercentral_selling.types.visibility

        out["Visibility"] = (
            capo_partnercentral_selling.types.visibility.serialize_aws_json_1_0(
                value["visibility"]
            )
        )
    if "life_cycle" in value:
        import capo_partnercentral_selling.types.aws_opportunity_life_cycle

        out["LifeCycle"] = (
            capo_partnercentral_selling.types.aws_opportunity_life_cycle.serialize_aws_json_1_0(
                value["life_cycle"]
            )
        )
    if "opportunity_team" in value:
        import capo_partnercentral_selling.types.aws_opportunity_team_members_list

        out["OpportunityTeam"] = (
            capo_partnercentral_selling.types.aws_opportunity_team_members_list.serialize_aws_json_1_0(
                value["opportunity_team"]
            )
        )
    if "insights" in value:
        import capo_partnercentral_selling.types.aws_opportunity_insights

        out["Insights"] = (
            capo_partnercentral_selling.types.aws_opportunity_insights.serialize_aws_json_1_0(
                value["insights"]
            )
        )
    if "involvement_type_change_reason" in value:
        import capo_partnercentral_selling.types.involvement_type_change_reason

        out["InvolvementTypeChangeReason"] = (
            capo_partnercentral_selling.types.involvement_type_change_reason.serialize_aws_json_1_0(
                value["involvement_type_change_reason"]
            )
        )
    if "related_entity_ids" in value:
        import capo_partnercentral_selling.types.aws_opportunity_related_entities

        out["RelatedEntityIds"] = (
            capo_partnercentral_selling.types.aws_opportunity_related_entities.serialize_aws_json_1_0(
                value["related_entity_ids"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.aws_opportunity_customer

        out["Customer"] = (
            capo_partnercentral_selling.types.aws_opportunity_customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.aws_opportunity_project

        out["Project"] = (
            capo_partnercentral_selling.types.aws_opportunity_project.serialize_aws_json_1_0(
                value["project"]
            )
        )
    if "cosell_motion" in value:
        out["CosellMotion"] = value["cosell_motion"]
    if "software_revenue" in value:
        import capo_partnercentral_selling.types.aws_software_revenue

        out["SoftwareRevenue"] = (
            capo_partnercentral_selling.types.aws_software_revenue.serialize_aws_json_1_0(
                value["software_revenue"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunitySummaryFullView:
    out: AwsOpportunitySummaryFullView = {}  # type: ignore[typeddict-item]
    if data.get("RelatedOpportunityId") is not None:
        out["related_opportunity_id"] = data["RelatedOpportunityId"]
    if data.get("Origin") is not None:
        import capo_partnercentral_selling.types.opportunity_origin

        out["origin"] = (
            capo_partnercentral_selling.types.opportunity_origin.deserialize_aws_json_1_0(
                data["Origin"]
            )
        )
    if data.get("InvolvementType") is not None:
        import capo_partnercentral_selling.types.sales_involvement_type

        out["involvement_type"] = (
            capo_partnercentral_selling.types.sales_involvement_type.deserialize_aws_json_1_0(
                data["InvolvementType"]
            )
        )
    if data.get("Visibility") is not None:
        import capo_partnercentral_selling.types.visibility

        out["visibility"] = (
            capo_partnercentral_selling.types.visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    if data.get("LifeCycle") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_life_cycle

        out["life_cycle"] = (
            capo_partnercentral_selling.types.aws_opportunity_life_cycle.deserialize_aws_json_1_0(
                data["LifeCycle"]
            )
        )
    if data.get("OpportunityTeam") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_team_members_list

        out["opportunity_team"] = (
            capo_partnercentral_selling.types.aws_opportunity_team_members_list.deserialize_aws_json_1_0(
                data["OpportunityTeam"]
            )
        )
    if data.get("Insights") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_insights

        out["insights"] = (
            capo_partnercentral_selling.types.aws_opportunity_insights.deserialize_aws_json_1_0(
                data["Insights"]
            )
        )
    if data.get("InvolvementTypeChangeReason") is not None:
        import capo_partnercentral_selling.types.involvement_type_change_reason

        out["involvement_type_change_reason"] = (
            capo_partnercentral_selling.types.involvement_type_change_reason.deserialize_aws_json_1_0(
                data["InvolvementTypeChangeReason"]
            )
        )
    if data.get("RelatedEntityIds") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_related_entities

        out["related_entity_ids"] = (
            capo_partnercentral_selling.types.aws_opportunity_related_entities.deserialize_aws_json_1_0(
                data["RelatedEntityIds"]
            )
        )
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_customer

        out["customer"] = (
            capo_partnercentral_selling.types.aws_opportunity_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Project") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_project

        out["project"] = (
            capo_partnercentral_selling.types.aws_opportunity_project.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    if data.get("CosellMotion") is not None:
        out["cosell_motion"] = data["CosellMotion"]
    if data.get("SoftwareRevenue") is not None:
        import capo_partnercentral_selling.types.aws_software_revenue

        out["software_revenue"] = (
            capo_partnercentral_selling.types.aws_software_revenue.deserialize_aws_json_1_0(
                data["SoftwareRevenue"]
            )
        )
    return out


def redact_sensitive(value: AwsOpportunitySummaryFullView) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "life_cycle" in value:
        import capo_partnercentral_selling.types.aws_opportunity_life_cycle

        out["life_cycle"] = (
            capo_partnercentral_selling.types.aws_opportunity_life_cycle.redact_sensitive(
                value["life_cycle"]
            )
        )
    if "opportunity_team" in value:
        import capo_partnercentral_selling.types.aws_opportunity_team_members_list

        out["opportunity_team"] = (
            capo_partnercentral_selling.types.aws_opportunity_team_members_list.redact_sensitive(
                value["opportunity_team"]
            )
        )
    if "insights" in value:
        import capo_partnercentral_selling.types.aws_opportunity_insights

        out["insights"] = (
            capo_partnercentral_selling.types.aws_opportunity_insights.redact_sensitive(
                value["insights"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.aws_opportunity_customer

        out["customer"] = (
            capo_partnercentral_selling.types.aws_opportunity_customer.redact_sensitive(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.aws_opportunity_project

        out["project"] = (
            capo_partnercentral_selling.types.aws_opportunity_project.redact_sensitive(
                value["project"]
            )
        )
    if "software_revenue" in value:
        import capo_partnercentral_selling.types.aws_software_revenue

        out["software_revenue"] = (
            capo_partnercentral_selling.types.aws_software_revenue.redact_sensitive(
                value["software_revenue"]
            )
        )
    return out

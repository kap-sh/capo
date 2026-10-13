"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetAwsOpportunitySummaryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_opportunity_customer
    import capo_partnercentral_selling.types.aws_opportunity_insights
    import capo_partnercentral_selling.types.aws_opportunity_life_cycle
    import capo_partnercentral_selling.types.aws_opportunity_project
    import capo_partnercentral_selling.types.aws_opportunity_related_entities
    import capo_partnercentral_selling.types.aws_opportunity_team_members_list
    import capo_partnercentral_selling.types.aws_software_revenue
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.involvement_type_change_reason
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.opportunity_origin
    import capo_partnercentral_selling.types.sales_involvement_type
    import capo_partnercentral_selling.types.visibility


class GetAwsOpportunitySummaryResponse(TypedDict, closed=True):
    related_opportunity_id: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Provides the unique identifier of the related partner opportunity, allowing partners to link the AWS Opportunity to their corresponding opportunity in their CRM system.</p>"""
    origin: NotRequired[
        "capo_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
    ]
    """<p>Specifies whether the AWS Opportunity originated from AWS or the partner. This helps distinguish between opportunities that were sourced by AWS and those referred by the partner.</p>"""
    involvement_type: NotRequired[
        "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    ]
    """<p>Specifies the type of involvement AWS has in the opportunity, such as direct cosell or advisory support. This field helps partners understand the role AWS plays in advancing the opportunity.</p>"""
    visibility: NotRequired["capo_partnercentral_selling.types.visibility.Visibility"]
    """<p>Defines the visibility level for the AWS Opportunity. Use <code>Full</code> visibility for most cases, while <code>Limited</code> visibility is reserved for special programs or sensitive opportunities.</p>"""
    life_cycle: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_life_cycle.AwsOpportunityLifeCycle"
    ]
    """<p>Contains lifecycle information for the AWS Opportunity, including review status, stage, and target close date. This field is crucial for partners to monitor the progression of the opportunity.</p>"""
    opportunity_team: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_team_members_list.AwsOpportunityTeamMembersList"
    ]
    """<p>Details the AWS opportunity team, including members involved. This information helps partners know who from AWS is engaged and what their role is.</p>"""
    insights: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_insights.AwsOpportunityInsights"
    ]
    """<p>Provides insights into the AWS Opportunity, including engagement score and recommended actions that AWS suggests for the partner.</p>"""
    involvement_type_change_reason: NotRequired[
        "capo_partnercentral_selling.types.involvement_type_change_reason.InvolvementTypeChangeReason"
    ]
    """<p>Provides a reason for any changes in the involvement type of AWS in the opportunity. This field is used to track why the level of AWS engagement has changed from <code>For Visibility Only</code> to <code>Co-sell</code> offering transparency into the partnership dynamics.</p>"""
    related_entity_ids: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_related_entities.AwsOpportunityRelatedEntities"
    ]
    """<p>Lists related entity identifiers, such as AWS products or partner solutions, associated with the AWS Opportunity. These identifiers provide additional context and help partners understand which AWS services are involved.</p>"""
    customer: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_customer.AwsOpportunityCustomer"
    ]
    """<p>Provides details about the customer associated with the AWS Opportunity, including account information, industry, and other customer data. These details help partners understand the business context of the opportunity.</p>"""
    project: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_project.AwsOpportunityProject"
    ]
    """<p>Provides details about the project associated with the AWS Opportunity, including the customer’s business problem, expected outcomes, and project scope. This information is crucial for understanding the broader context of the opportunity.</p>"""
    cosell_motion: NotRequired["str"]
    """<p>Engagement classification for this opportunity. Read-only. Null before scoring. Known values: <code>AWS Field-engaged</code>, <code>Agent-engaged</code>, <code>Partner-led</code>.</p>"""
    software_revenue: NotRequired[
        "capo_partnercentral_selling.types.aws_software_revenue.AwsSoftwareRevenue"
    ]
    """<p>Seller-provided PARC deal terms: commitment value, discount, and contract dates.</p>"""
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the AWS Opportunity exists. This is the environment (e.g., <code>AWS</code> or <code>Sandbox</code>) where the opportunity is being managed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAwsOpportunitySummaryResponse) -> dict:
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
    out["Catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAwsOpportunitySummaryResponse:
    out: GetAwsOpportunitySummaryResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetAwsOpportunitySummaryResponse.catalog required")
    return out


def redact_sensitive(value: GetAwsOpportunitySummaryResponse) -> dict[str, Any]:
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

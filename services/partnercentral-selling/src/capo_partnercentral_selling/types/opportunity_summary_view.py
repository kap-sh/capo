"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySummaryView``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.customer
    import capo_partnercentral_selling.types.life_cycle_for_view
    import capo_partnercentral_selling.types.opportunity_type
    import capo_partnercentral_selling.types.partner_opportunity_team_members_list
    import capo_partnercentral_selling.types.primary_needs_from_aws
    import capo_partnercentral_selling.types.project_view
    import capo_partnercentral_selling.types.related_entity_identifiers


class OpportunitySummaryView(TypedDict, closed=True):
    opportunity_type: NotRequired[
        "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
    ]
    """<p> Specifies the opportunity type. </p>"""
    lifecycle: NotRequired[
        "capo_partnercentral_selling.types.life_cycle_for_view.LifeCycleForView"
    ]
    """<p> Contains information about the opportunity's lifecycle, including its current stage, status, and important dates such as creation and last modification times. </p>"""
    opportunity_team: NotRequired[
        "capo_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
    ]
    """<p> Represents the internal team handling the opportunity. Specify the members involved in collaborating on an opportunity within the partner's organization. </p>"""
    primary_needs_from_aws: NotRequired[
        "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
    ]
    """<p> Identifies the type of support the partner needs from AWS. </p>"""
    customer: NotRequired["capo_partnercentral_selling.types.customer.Customer"]
    project: NotRequired["capo_partnercentral_selling.types.project_view.ProjectView"]
    """<p> Contains summary information about the project associated with the opportunity, including project name, description, timeline, and other relevant details. </p>"""
    related_entity_identifiers: NotRequired[
        "capo_partnercentral_selling.types.related_entity_identifiers.RelatedEntityIdentifiers"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySummaryView) -> dict:
    out: dict = {}
    if "opportunity_type" in value:
        import capo_partnercentral_selling.types.opportunity_type

        out["OpportunityType"] = (
            capo_partnercentral_selling.types.opportunity_type.serialize_aws_json_1_0(
                value["opportunity_type"]
            )
        )
    if "lifecycle" in value:
        import capo_partnercentral_selling.types.life_cycle_for_view

        out["Lifecycle"] = (
            capo_partnercentral_selling.types.life_cycle_for_view.serialize_aws_json_1_0(
                value["lifecycle"]
            )
        )
    if "opportunity_team" in value:
        import capo_partnercentral_selling.types.partner_opportunity_team_members_list

        out["OpportunityTeam"] = (
            capo_partnercentral_selling.types.partner_opportunity_team_members_list.serialize_aws_json_1_0(
                value["opportunity_team"]
            )
        )
    if "primary_needs_from_aws" in value:
        import capo_partnercentral_selling.types.primary_needs_from_aws

        out["PrimaryNeedsFromAws"] = (
            capo_partnercentral_selling.types.primary_needs_from_aws.serialize_aws_json_1_0(
                value["primary_needs_from_aws"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.customer

        out["Customer"] = (
            capo_partnercentral_selling.types.customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.project_view

        out["Project"] = (
            capo_partnercentral_selling.types.project_view.serialize_aws_json_1_0(
                value["project"]
            )
        )
    if "related_entity_identifiers" in value:
        import capo_partnercentral_selling.types.related_entity_identifiers

        out["RelatedEntityIdentifiers"] = (
            capo_partnercentral_selling.types.related_entity_identifiers.serialize_aws_json_1_0(
                value["related_entity_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunitySummaryView:
    out: OpportunitySummaryView = {}  # type: ignore[typeddict-item]
    if data.get("OpportunityType") is not None:
        import capo_partnercentral_selling.types.opportunity_type

        out["opportunity_type"] = (
            capo_partnercentral_selling.types.opportunity_type.deserialize_aws_json_1_0(
                data["OpportunityType"]
            )
        )
    if data.get("Lifecycle") is not None:
        import capo_partnercentral_selling.types.life_cycle_for_view

        out["lifecycle"] = (
            capo_partnercentral_selling.types.life_cycle_for_view.deserialize_aws_json_1_0(
                data["Lifecycle"]
            )
        )
    if data.get("OpportunityTeam") is not None:
        import capo_partnercentral_selling.types.partner_opportunity_team_members_list

        out["opportunity_team"] = (
            capo_partnercentral_selling.types.partner_opportunity_team_members_list.deserialize_aws_json_1_0(
                data["OpportunityTeam"]
            )
        )
    if data.get("PrimaryNeedsFromAws") is not None:
        import capo_partnercentral_selling.types.primary_needs_from_aws

        out["primary_needs_from_aws"] = (
            capo_partnercentral_selling.types.primary_needs_from_aws.deserialize_aws_json_1_0(
                data["PrimaryNeedsFromAws"]
            )
        )
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.customer

        out["customer"] = (
            capo_partnercentral_selling.types.customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Project") is not None:
        import capo_partnercentral_selling.types.project_view

        out["project"] = (
            capo_partnercentral_selling.types.project_view.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    if data.get("RelatedEntityIdentifiers") is not None:
        import capo_partnercentral_selling.types.related_entity_identifiers

        out["related_entity_identifiers"] = (
            capo_partnercentral_selling.types.related_entity_identifiers.deserialize_aws_json_1_0(
                data["RelatedEntityIdentifiers"]
            )
        )
    return out


def redact_sensitive(value: OpportunitySummaryView) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "lifecycle" in value:
        import capo_partnercentral_selling.types.life_cycle_for_view

        out["lifecycle"] = (
            capo_partnercentral_selling.types.life_cycle_for_view.redact_sensitive(
                value["lifecycle"]
            )
        )
    if "opportunity_team" in value:
        import capo_partnercentral_selling.types.partner_opportunity_team_members_list

        out["opportunity_team"] = (
            capo_partnercentral_selling.types.partner_opportunity_team_members_list.redact_sensitive(
                value["opportunity_team"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.customer

        out["customer"] = capo_partnercentral_selling.types.customer.redact_sensitive(
            value["customer"]
        )
    if "project" in value:
        import capo_partnercentral_selling.types.project_view

        out["project"] = (
            capo_partnercentral_selling.types.project_view.redact_sensitive(
                value["project"]
            )
        )
    return out

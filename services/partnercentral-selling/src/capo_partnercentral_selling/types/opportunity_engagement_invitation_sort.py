"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityEngagementInvitationSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name
    import capo_partnercentral_selling.types.sort_order


class OpportunityEngagementInvitationSort(TypedDict, closed=True):
    sort_order: "capo_partnercentral_selling.types.sort_order.SortOrder"
    """<p>Defines the order in which the Engagement Invitations are sorted. The values can be <code>ASC</code> (ascending) or <code>DESC</code> (descending).</p>"""
    sort_by: "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.OpportunityEngagementInvitationSortName"
    """<p>Specifies the field by which the Engagement Invitations are sorted. Common values include <code>InvitationDate</code> and <code>Status</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityEngagementInvitationSort) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.sort_order

    out["SortOrder"] = (
        capo_partnercentral_selling.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name

    out["SortBy"] = (
        capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunityEngagementInvitationSort:
    out: OpportunityEngagementInvitationSort = {}  # type: ignore[typeddict-item]
    if data.get("SortOrder") is not None:
        import capo_partnercentral_selling.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_selling.types.sort_order.deserialize_aws_json_1_0(
                data["SortOrder"]
            )
        )
    else:
        import typing

        out["sort_order"] = typing.cast(
            "capo_partnercentral_selling.types.sort_order.SortOrder", ""
        )
    if data.get("SortBy") is not None:
        import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name

        out["sort_by"] = (
            capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.deserialize_aws_json_1_0(
                data["SortBy"]
            )
        )
    else:
        import typing

        out["sort_by"] = typing.cast(
            "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.OpportunityEngagementInvitationSortName",
            "",
        )
    return out

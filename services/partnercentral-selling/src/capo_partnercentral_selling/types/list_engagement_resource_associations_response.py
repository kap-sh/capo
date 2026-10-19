"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementResourceAssociationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_resource_association_summary_list


class ListEngagementResourceAssociationsResponse(TypedDict, closed=True):
    engagement_resource_association_summaries: "capo_partnercentral_selling.types.engagement_resource_association_summary_list.EngagementResourceAssociationSummaryList"
    """<p> A list of engagement-resource association summaries. </p>"""
    next_token: NotRequired["str"]
    """<p> A token to retrieve the next set of results. Use this token in a subsequent request to retrieve additional results if the response was truncated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementResourceAssociationsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.engagement_resource_association_summary_list

    out["EngagementResourceAssociationSummaries"] = (
        capo_partnercentral_selling.types.engagement_resource_association_summary_list.serialize_aws_json_1_0(
            value["engagement_resource_association_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementResourceAssociationsResponse:
    out: ListEngagementResourceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EngagementResourceAssociationSummaries") is not None:
        import capo_partnercentral_selling.types.engagement_resource_association_summary_list

        out["engagement_resource_association_summaries"] = (
            capo_partnercentral_selling.types.engagement_resource_association_summary_list.deserialize_aws_json_1_0(
                data["EngagementResourceAssociationSummaries"]
            )
        )
    else:
        out["engagement_resource_association_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListEngagementResourceAssociationsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "engagement_resource_association_summaries" in value:
        import capo_partnercentral_selling.types.engagement_resource_association_summary_list

        out["engagement_resource_association_summaries"] = (
            capo_partnercentral_selling.types.engagement_resource_association_summary_list.redact_sensitive(
                value["engagement_resource_association_summaries"]
            )
        )
    return out

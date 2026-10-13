"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementInvitationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_invitation_summaries


class ListEngagementInvitationsResponse(TypedDict, closed=True):
    engagement_invitation_summaries: NotRequired[
        "capo_partnercentral_selling.types.engagement_invitation_summaries.EngagementInvitationSummaries"
    ]
    """<p>An array containing summaries of engagement invitations. Each summary includes information such as the invitation title, invitation date, and the current status of the invitation.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token returned when there are more results available than can be returned in a single call. Use this token to retrieve additional pages of engagement invitation summaries.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementInvitationsResponse) -> dict:
    out: dict = {}
    if "engagement_invitation_summaries" in value:
        import capo_partnercentral_selling.types.engagement_invitation_summaries

        out["EngagementInvitationSummaries"] = (
            capo_partnercentral_selling.types.engagement_invitation_summaries.serialize_aws_json_1_0(
                value["engagement_invitation_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementInvitationsResponse:
    out: ListEngagementInvitationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EngagementInvitationSummaries") is not None:
        import capo_partnercentral_selling.types.engagement_invitation_summaries

        out["engagement_invitation_summaries"] = (
            capo_partnercentral_selling.types.engagement_invitation_summaries.deserialize_aws_json_1_0(
                data["EngagementInvitationSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListEngagementInvitationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "engagement_invitation_summaries" in value:
        import capo_partnercentral_selling.types.engagement_invitation_summaries

        out["engagement_invitation_summaries"] = (
            capo_partnercentral_selling.types.engagement_invitation_summaries.redact_sensitive(
                value["engagement_invitation_summaries"]
            )
        )
    return out

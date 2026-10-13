"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_invitation_summary

EngagementInvitationSummaries: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_invitation_summary.EngagementInvitationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementInvitationSummaries) -> list:
    import capo_partnercentral_selling.types.engagement_invitation_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_invitation_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementInvitationSummaries:
    import capo_partnercentral_selling.types.engagement_invitation_summary

    out: EngagementInvitationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.engagement_invitation_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EngagementInvitationSummaries) -> list[Any]:
    import capo_partnercentral_selling.types.engagement_invitation_summary

    return [
        capo_partnercentral_selling.types.engagement_invitation_summary.redact_sensitive(
            item
        )
        for item in value
    ]

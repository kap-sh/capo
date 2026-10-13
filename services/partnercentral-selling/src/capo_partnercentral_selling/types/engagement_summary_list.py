"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_summary

EngagementSummaryList: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_summary.EngagementSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementSummaryList) -> list:
    import capo_partnercentral_selling.types.engagement_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementSummaryList:
    import capo_partnercentral_selling.types.engagement_summary

    out: EngagementSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.engagement_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EngagementSummaryList) -> list[Any]:
    import capo_partnercentral_selling.types.engagement_summary

    return [
        capo_partnercentral_selling.types.engagement_summary.redact_sensitive(item)
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementResourceAssociationSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_resource_association_summary

EngagementResourceAssociationSummaryList: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_resource_association_summary.EngagementResourceAssociationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementResourceAssociationSummaryList) -> list:
    import capo_partnercentral_selling.types.engagement_resource_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_resource_association_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementResourceAssociationSummaryList:
    import capo_partnercentral_selling.types.engagement_resource_association_summary

    out: EngagementResourceAssociationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.engagement_resource_association_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EngagementResourceAssociationSummaryList) -> list[Any]:
    import capo_partnercentral_selling.types.engagement_resource_association_summary

    return [
        capo_partnercentral_selling.types.engagement_resource_association_summary.redact_sensitive(
            item
        )
        for item in value
    ]

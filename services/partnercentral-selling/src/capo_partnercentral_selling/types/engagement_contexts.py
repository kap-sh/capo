"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContexts``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_context_details

EngagementContexts: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_context_details.EngagementContextDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementContexts) -> list:
    import capo_partnercentral_selling.types.engagement_context_details

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_context_details.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementContexts:
    import capo_partnercentral_selling.types.engagement_context_details

    out: EngagementContexts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.engagement_context_details.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EngagementContexts) -> list[Any]:
    import capo_partnercentral_selling.types.engagement_context_details

    return [
        capo_partnercentral_selling.types.engagement_context_details.redact_sensitive(
            item
        )
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.opportunity_summary

OpportunitySummaries: TypeAlias = list[
    "capo_partnercentral_selling.types.opportunity_summary.OpportunitySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySummaries) -> list:
    import capo_partnercentral_selling.types.opportunity_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.opportunity_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OpportunitySummaries:
    import capo_partnercentral_selling.types.opportunity_summary

    out: OpportunitySummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.opportunity_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: OpportunitySummaries) -> list[Any]:
    import capo_partnercentral_selling.types.opportunity_summary

    return [
        capo_partnercentral_selling.types.opportunity_summary.redact_sensitive(item)
        for item in value
    ]

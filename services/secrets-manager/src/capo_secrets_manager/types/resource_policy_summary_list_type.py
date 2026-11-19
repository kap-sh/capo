"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ResourcePolicySummaryListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.resource_policy_summary

ResourcePolicySummaryListType: TypeAlias = list[
    "capo_secrets_manager.types.resource_policy_summary.ResourcePolicySummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicySummaryListType) -> list:
    import capo_secrets_manager.types.resource_policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.resource_policy_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourcePolicySummaryListType:
    import capo_secrets_manager.types.resource_policy_summary

    out: ResourcePolicySummaryListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_secrets_manager.types.resource_policy_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

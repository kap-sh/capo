"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.environment_summary

EnvironmentSummaryList: TypeAlias = list[
    "capo_proton.types.environment_summary.EnvironmentSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentSummaryList) -> list:
    import capo_proton.types.environment_summary

    out: list = []
    for item in value:
        out.append(capo_proton.types.environment_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentSummaryList:
    import capo_proton.types.environment_summary

    out: EnvironmentSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_proton.types.environment_summary.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: EnvironmentSummaryList) -> list[Any]:
    import capo_proton.types.environment_summary

    return [
        capo_proton.types.environment_summary.redact_sensitive(item) for item in value
    ]

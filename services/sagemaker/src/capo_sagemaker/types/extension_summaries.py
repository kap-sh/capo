"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_summary

ExtensionSummaries: TypeAlias = list[
    "capo_sagemaker.types.extension_summary.ExtensionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionSummaries) -> list:
    import capo_sagemaker.types.extension_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.extension_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExtensionSummaries:
    import capo_sagemaker.types.extension_summary

    out: ExtensionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.extension_summary.deserialize_aws_json_1_1(item)
        )
    return out

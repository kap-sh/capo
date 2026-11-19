"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_version_summary

ExtensionVersionSummaries: TypeAlias = list[
    "capo_sagemaker.types.extension_version_summary.ExtensionVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionVersionSummaries) -> list:
    import capo_sagemaker.types.extension_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.extension_version_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExtensionVersionSummaries:
    import capo_sagemaker.types.extension_version_summary

    out: ExtensionVersionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.extension_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

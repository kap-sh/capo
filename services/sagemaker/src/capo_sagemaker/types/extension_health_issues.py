"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionHealthIssues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_health_issue

ExtensionHealthIssues: TypeAlias = list[
    "capo_sagemaker.types.extension_health_issue.ExtensionHealthIssue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionHealthIssues) -> list:
    import capo_sagemaker.types.extension_health_issue

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.extension_health_issue.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExtensionHealthIssues:
    import capo_sagemaker.types.extension_health_issue

    out: ExtensionHealthIssues = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.extension_health_issue.deserialize_aws_json_1_1(item)
        )
    return out

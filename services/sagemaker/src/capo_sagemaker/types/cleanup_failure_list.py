"""Generated from Smithy shape ``com.amazonaws.sagemaker#CleanupFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cleanup_failure

CleanupFailureList: TypeAlias = list[
    "capo_sagemaker.types.cleanup_failure.CleanupFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CleanupFailureList) -> list:
    import capo_sagemaker.types.cleanup_failure

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.cleanup_failure.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CleanupFailureList:
    import capo_sagemaker.types.cleanup_failure

    out: CleanupFailureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sagemaker.types.cleanup_failure.deserialize_aws_json_1_1(item))
    return out

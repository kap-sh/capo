"""Generated from Smithy shape ``com.amazonaws.sagemaker#CleanupStepNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.string256

CleanupStepNameList: TypeAlias = list["capo_sagemaker.types.string256.String256"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CleanupStepNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CleanupStepNameList:
    return [item for item in data if item is not None]

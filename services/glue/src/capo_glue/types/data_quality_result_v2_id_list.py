"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultV2IdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.hash_string

DataQualityResultV2IdList: TypeAlias = list["capo_glue.types.hash_string.HashString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultV2IdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataQualityResultV2IdList:
    return [item for item in data if item is not None]

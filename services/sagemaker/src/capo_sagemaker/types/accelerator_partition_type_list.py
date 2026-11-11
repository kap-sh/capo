"""Generated from Smithy shape ``com.amazonaws.sagemaker#AcceleratorPartitionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.accelerator_partition_type

AcceleratorPartitionTypeList: TypeAlias = list[
    "capo_sagemaker.types.accelerator_partition_type.AcceleratorPartitionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorPartitionTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AcceleratorPartitionTypeList:
    return [item for item in data if item is not None]

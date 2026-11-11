"""Generated from Smithy shape ``com.amazonaws.sagemaker#AcceleratorPartitionLayouts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.accelerator_partition_layout

AcceleratorPartitionLayouts: TypeAlias = list[
    "capo_sagemaker.types.accelerator_partition_layout.AcceleratorPartitionLayout"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorPartitionLayouts) -> list:
    import capo_sagemaker.types.accelerator_partition_layout

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.accelerator_partition_layout.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AcceleratorPartitionLayouts:
    import capo_sagemaker.types.accelerator_partition_layout

    out: AcceleratorPartitionLayouts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.accelerator_partition_layout.deserialize_aws_json_1_1(
                item
            )
        )
    return out

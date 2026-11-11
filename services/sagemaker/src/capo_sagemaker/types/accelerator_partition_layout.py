"""Generated from Smithy shape ``com.amazonaws.sagemaker#AcceleratorPartitionLayout``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.accelerator_partition_type_list


class AcceleratorPartitionLayout(TypedDict, closed=True):
    accelerator_partition_types: NotRequired[
        "capo_sagemaker.types.accelerator_partition_type_list.AcceleratorPartitionTypeList"
    ]
    """<p>The list of partition profiles to carve on each accelerator that this layout applies to. On NVIDIA GPUs these are Multi-Instance GPU (MIG) profiles, for example <code>["mig-3g.40gb", "mig-4g.40gb"]</code>. The order of the profiles doesn't change how the accelerator is partitioned. However, when you update an endpoint, a layout with the same profiles in a different order counts as a different layout, and the update is rejected. Repeat a profile to request more than one partition of that size: for example, <code>["mig-3g.40gb", "mig-3g.40gb"]</code> requests two <code>mig-3g.40gb</code> partitions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorPartitionLayout) -> dict:
    out: dict = {}
    if "accelerator_partition_types" in value:
        import capo_sagemaker.types.accelerator_partition_type_list

        out["AcceleratorPartitionTypes"] = (
            capo_sagemaker.types.accelerator_partition_type_list.serialize_aws_json_1_1(
                value["accelerator_partition_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceleratorPartitionLayout:
    out: AcceleratorPartitionLayout = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorPartitionTypes") is not None:
        import capo_sagemaker.types.accelerator_partition_type_list

        out["accelerator_partition_types"] = (
            capo_sagemaker.types.accelerator_partition_type_list.deserialize_aws_json_1_1(
                data["AcceleratorPartitionTypes"]
            )
        )
    return out

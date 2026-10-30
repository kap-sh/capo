"""Generated from Smithy shape ``com.amazonaws.ecs#GpuDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gpu_sharing_mode
    import capo_ecs.types.string


class GpuDevice(TypedDict, closed=True):
    gpu_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the GPU. This ID matches the GPU IDs in the <code>gpuIds</code> of the containers that Amazon ECS assigned to the GPU.</p>"""
    sharing_mode: NotRequired["capo_ecs.types.gpu_sharing_mode.GpuSharingMode"]
    """<p>How the GPU is shared between containers.</p> <p>Valid values:</p> <ul> <li> <p> <code>IDLE</code> - No containers are assigned to the GPU, and all of its memory is available.</p> </li> <li> <p> <code>NVIDIA_MPS</code> - One or more containers share the GPU by using NVIDIA Multi-Process Service (MPS).</p> </li> <li> <p> <code>DEDICATED</code> - One container has exclusive use of the GPU.</p> </li> </ul>"""
    total_memory_in_mi_b: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The total amount of GPU memory, in MiB, that the Amazon ECS container agent reported for the GPU. This is the memory that's available to containers, and it can be less than the nominal memory of the GPU.</p>"""
    remaining_memory_in_mi_b: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The amount of GPU memory, in MiB, that's available to allocate to new containers that use the <code>nvidiaMps</code> sharing strategy. Amazon ECS calculates this value from the memory that it allocated to containers on the GPU, not from the memory that the containers use.</p>"""
    container_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of containers that Amazon ECS assigned to the GPU. This value is <code>0</code> when the sharing mode is <code>IDLE</code> and <code>1</code> when the sharing mode is <code>DEDICATED</code>. Amazon ECS counts the containers that it assigned to the GPU, not the processes that are running on it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GpuDevice) -> dict:
    out: dict = {}
    if "gpu_id" in value:
        out["gpuId"] = value["gpu_id"]
    if "sharing_mode" in value:
        import capo_ecs.types.gpu_sharing_mode

        out["sharingMode"] = capo_ecs.types.gpu_sharing_mode.serialize_aws_json_1_1(
            value["sharing_mode"]
        )
    if "total_memory_in_mi_b" in value:
        out["totalMemoryInMiB"] = value["total_memory_in_mi_b"]
    if "remaining_memory_in_mi_b" in value:
        out["remainingMemoryInMiB"] = value["remaining_memory_in_mi_b"]
    if "container_count" in value:
        out["containerCount"] = value["container_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GpuDevice:
    out: GpuDevice = {}  # type: ignore[typeddict-item]
    if data.get("gpuId") is not None:
        out["gpu_id"] = data["gpuId"]
    if data.get("sharingMode") is not None:
        import capo_ecs.types.gpu_sharing_mode

        out["sharing_mode"] = capo_ecs.types.gpu_sharing_mode.deserialize_aws_json_1_1(
            data["sharingMode"]
        )
    if data.get("totalMemoryInMiB") is not None:
        out["total_memory_in_mi_b"] = data["totalMemoryInMiB"]
    if data.get("remainingMemoryInMiB") is not None:
        out["remaining_memory_in_mi_b"] = data["remainingMemoryInMiB"]
    if data.get("containerCount") is not None:
        out["container_count"] = data["containerCount"]
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#NvidiaMpsAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer


class NvidiaMpsAllocation(TypedDict, closed=True):
    memory: "capo_ecs.types.boxed_integer.BoxedInteger"
    """<p>The amount of GPU memory, in MiB, to allocate to the container. Amazon ECS assigns the container a GPU that has at least the specified amount of memory available, and sets the <code>CUDA_MPS_PINNED_DEVICE_MEM_LIMIT</code> environment variable in the container to limit its memory to this amount. The memory must be available on a single GPU. If more than one container in a task uses <code>nvidiaMps</code>, Amazon ECS assigns them the same GPU, which must have enough memory available for all of them.</p>"""
    max_compute_percent: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum percentage of the GPU's compute capacity that the container can use. Amazon ECS sets the <code>CUDA_MPS_ACTIVE_THREAD_PERCENTAGE</code> environment variable in the container to this value. This value is a limit, not a reservation.</p> <p>If you don't specify this parameter, Amazon ECS doesn't set <code>CUDA_MPS_ACTIVE_THREAD_PERCENTAGE</code>, and the active thread percentage of the MPS server on the container instance applies. By default, this is 100 percent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NvidiaMpsAllocation) -> dict:
    out: dict = {}
    out["memory"] = value["memory"]
    if "max_compute_percent" in value:
        out["maxComputePercent"] = value["max_compute_percent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NvidiaMpsAllocation:
    out: NvidiaMpsAllocation = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    else:
        out["memory"] = 0
    if data.get("maxComputePercent") is not None:
        out["max_compute_percent"] = data["maxComputePercent"]
    return out

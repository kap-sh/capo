"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Gpu``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.gpu_count
    import capo_compute_optimizer.types.gpu_memory_size_in_mi_b


class Gpu(TypedDict, closed=True):
    gpu_count: "capo_compute_optimizer.types.gpu_count.GpuCount"
    """<p> The number of GPUs for the instance type. </p>"""
    gpu_memory_size_in_mi_b: (
        "capo_compute_optimizer.types.gpu_memory_size_in_mi_b.GpuMemorySizeInMiB"
    )
    """<p> The total size of the memory for the GPU accelerators for the instance type, in MiB. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Gpu) -> dict:
    out: dict = {}
    out["gpuCount"] = value.get("gpu_count", 0)
    out["gpuMemorySizeInMiB"] = value.get("gpu_memory_size_in_mi_b", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Gpu:
    out: Gpu = {}  # type: ignore[typeddict-item]
    if data.get("gpuCount") is not None:
        out["gpu_count"] = data["gpuCount"]
    else:
        out["gpu_count"] = 0
    if data.get("gpuMemorySizeInMiB") is not None:
        out["gpu_memory_size_in_mi_b"] = data["gpuMemorySizeInMiB"]
    else:
        out["gpu_memory_size_in_mi_b"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Gpu) -> dict:
    out: dict = {}
    out["gpuCount"] = value.get("gpu_count", 0)
    out["gpuMemorySizeInMiB"] = value.get("gpu_memory_size_in_mi_b", 0)
    return out


def deserialize_cbor(data: dict) -> Gpu:
    out: Gpu = {}  # type: ignore[typeddict-item]
    if data.get("gpuCount") is not None:
        out["gpu_count"] = data["gpuCount"]
    else:
        out["gpu_count"] = 0
    if data.get("gpuMemorySizeInMiB") is not None:
        out["gpu_memory_size_in_mi_b"] = data["gpuMemorySizeInMiB"]
    else:
        out["gpu_memory_size_in_mi_b"] = 0
    return out

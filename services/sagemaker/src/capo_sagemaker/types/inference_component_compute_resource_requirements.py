"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentComputeResourceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.memory_in_mb
    import capo_sagemaker.types.number_of_accelerator_devices
    import capo_sagemaker.types.number_of_cpu_cores


class InferenceComponentComputeResourceRequirements(TypedDict, closed=True):
    number_of_cpu_cores_required: NotRequired[
        "capo_sagemaker.types.number_of_cpu_cores.NumberOfCpuCores"
    ]
    """<p>The number of CPU cores to allocate to run a model that you assign to an inference component.</p>"""
    number_of_accelerator_devices_required: NotRequired[
        "capo_sagemaker.types.number_of_accelerator_devices.NumberOfAcceleratorDevices"
    ]
    """<p>The number of accelerators to allocate to run a model that you assign to an inference component. Accelerators include GPUs and Amazon Web Services Inferentia.</p>"""
    min_memory_required_in_mb: NotRequired[
        "capo_sagemaker.types.memory_in_mb.MemoryInMb"
    ]
    """<p>The minimum MB of memory to allocate to run a model that you assign to an inference component.</p>"""
    max_memory_required_in_mb: NotRequired[
        "capo_sagemaker.types.memory_in_mb.MemoryInMb"
    ]
    """<p>The maximum MB of memory to allocate to run a model that you assign to an inference component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InferenceComponentComputeResourceRequirements,
) -> dict:
    out: dict = {}
    if "number_of_cpu_cores_required" in value:
        out["NumberOfCpuCoresRequired"] = (
            "NaN"
            if value["number_of_cpu_cores_required"]
            != value["number_of_cpu_cores_required"]
            else "Infinity"
            if value["number_of_cpu_cores_required"] == float("inf")
            else "-Infinity"
            if value["number_of_cpu_cores_required"] == float("-inf")
            else value["number_of_cpu_cores_required"]
        )
    if "number_of_accelerator_devices_required" in value:
        out["NumberOfAcceleratorDevicesRequired"] = (
            "NaN"
            if value["number_of_accelerator_devices_required"]
            != value["number_of_accelerator_devices_required"]
            else "Infinity"
            if value["number_of_accelerator_devices_required"] == float("inf")
            else "-Infinity"
            if value["number_of_accelerator_devices_required"] == float("-inf")
            else value["number_of_accelerator_devices_required"]
        )
    if "min_memory_required_in_mb" in value:
        out["MinMemoryRequiredInMb"] = value["min_memory_required_in_mb"]
    if "max_memory_required_in_mb" in value:
        out["MaxMemoryRequiredInMb"] = value["max_memory_required_in_mb"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InferenceComponentComputeResourceRequirements:
    out: InferenceComponentComputeResourceRequirements = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfCpuCoresRequired") is not None:
        out["number_of_cpu_cores_required"] = float(data["NumberOfCpuCoresRequired"])
    if data.get("NumberOfAcceleratorDevicesRequired") is not None:
        out["number_of_accelerator_devices_required"] = float(
            data["NumberOfAcceleratorDevicesRequired"]
        )
    if data.get("MinMemoryRequiredInMb") is not None:
        out["min_memory_required_in_mb"] = data["MinMemoryRequiredInMb"]
    if data.get("MaxMemoryRequiredInMb") is not None:
        out["max_memory_required_in_mb"] = data["MaxMemoryRequiredInMb"]
    return out

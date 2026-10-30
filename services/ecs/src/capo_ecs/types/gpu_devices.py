"""Generated from Smithy shape ``com.amazonaws.ecs#GpuDevices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gpu_device

GpuDevices: TypeAlias = list["capo_ecs.types.gpu_device.GpuDevice"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GpuDevices) -> list:
    import capo_ecs.types.gpu_device

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gpu_device.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GpuDevices:
    import capo_ecs.types.gpu_device

    out: GpuDevices = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gpu_device.deserialize_aws_json_1_1(item))
    return out

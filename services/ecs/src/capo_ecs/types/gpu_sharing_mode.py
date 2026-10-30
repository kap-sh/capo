"""Generated from Smithy shape ``com.amazonaws.ecs#GpuSharingMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Describes how a GPU on a container instance is shared between containers.</p>"""
GpuSharingMode: TypeAlias = Literal[
    "IDLE",
    "NVIDIA_MPS",
    "DEDICATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GpuSharingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GpuSharingMode:
    return cast(GpuSharingMode, data)

"""Generated from Smithy shape ``com.amazonaws.odb#VmStorageType``."""

from typing import Literal, TypeAlias, cast

VmStorageType: TypeAlias = Literal[
    "LOCAL",
    "EXASCALE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmStorageType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VmStorageType:
    return cast(VmStorageType, data)

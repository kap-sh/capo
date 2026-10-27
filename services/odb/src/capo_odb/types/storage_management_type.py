"""Generated from Smithy shape ``com.amazonaws.odb#StorageManagementType``."""

from typing import Literal, TypeAlias, cast

StorageManagementType: TypeAlias = Literal[
    "ASM",
    "EXASCALE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageManagementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StorageManagementType:
    return cast(StorageManagementType, data)

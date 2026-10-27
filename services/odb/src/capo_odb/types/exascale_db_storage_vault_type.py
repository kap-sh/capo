"""Generated from Smithy shape ``com.amazonaws.odb#ExascaleDbStorageVaultType``."""

from typing import Literal, TypeAlias, cast

ExascaleDbStorageVaultType: TypeAlias = Literal[
    "EXASCALE_INFRASTRUCTURE",
    "DEDICATED_INFRASTRUCTURE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExascaleDbStorageVaultType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExascaleDbStorageVaultType:
    return cast(ExascaleDbStorageVaultType, data)

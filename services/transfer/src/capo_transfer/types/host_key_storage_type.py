"""Generated from Smithy shape ``com.amazonaws.transfer#HostKeyStorageType``."""

from typing import Literal, TypeAlias, cast

HostKeyStorageType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostKeyStorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HostKeyStorageType:
    return cast(HostKeyStorageType, data)

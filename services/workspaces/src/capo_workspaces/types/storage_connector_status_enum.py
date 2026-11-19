"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnectorStatusEnum``."""

from typing import Literal, TypeAlias, cast

StorageConnectorStatusEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnectorStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorStatusEnum:
    return cast(StorageConnectorStatusEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConnectorStatusEnum) -> str:
    return value


def deserialize_cbor(data: str) -> StorageConnectorStatusEnum:
    return cast(StorageConnectorStatusEnum, data)

"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnectorTypeEnum``."""

from typing import Literal, TypeAlias, cast

StorageConnectorTypeEnum: TypeAlias = Literal["HOME_FOLDER",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnectorTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorTypeEnum:
    return cast(StorageConnectorTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConnectorTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> StorageConnectorTypeEnum:
    return cast(StorageConnectorTypeEnum, data)

"""Generated from Smithy shape ``com.amazonaws.snowball#DeviceServiceName``."""

from typing import Literal, TypeAlias, cast

DeviceServiceName: TypeAlias = Literal[
    "NFS_ON_DEVICE_SERVICE",
    "S3_ON_DEVICE_SERVICE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceServiceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceServiceName:
    return cast(DeviceServiceName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeviceServiceName) -> str:
    return value


def deserialize_cbor(data: str) -> DeviceServiceName:
    return cast(DeviceServiceName, data)

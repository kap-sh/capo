"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientDeviceType``."""

from typing import Literal, TypeAlias, cast

ClientDeviceType: TypeAlias = Literal[
    "DeviceTypeWindows",
    "DeviceTypeOsx",
    "DeviceTypeAndroid",
    "DeviceTypeIos",
    "DeviceTypeLinux",
    "DeviceTypeWeb",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientDeviceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientDeviceType:
    return cast(ClientDeviceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientDeviceType) -> str:
    return value


def deserialize_cbor(data: str) -> ClientDeviceType:
    return cast(ClientDeviceType, data)

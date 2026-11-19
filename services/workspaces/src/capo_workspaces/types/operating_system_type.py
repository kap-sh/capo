"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemType``."""

from typing import Literal, TypeAlias, cast

OperatingSystemType: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystemType:
    return cast(OperatingSystemType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperatingSystemType) -> str:
    return value


def deserialize_cbor(data: str) -> OperatingSystemType:
    return cast(OperatingSystemType, data)

"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerMountPointAccessLevel``."""

from typing import Literal, TypeAlias, cast

ContainerMountPointAccessLevel: TypeAlias = Literal[
    "READ_ONLY",
    "READ_AND_WRITE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerMountPointAccessLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerMountPointAccessLevel:
    return cast(ContainerMountPointAccessLevel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerMountPointAccessLevel) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerMountPointAccessLevel:
    return cast(ContainerMountPointAccessLevel, data)

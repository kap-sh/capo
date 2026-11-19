"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ResourceTypeEnum``."""

from typing import Literal, TypeAlias, cast

ResourceTypeEnum: TypeAlias = Literal[
    "instance",
    "volume",
    "spot-instances-request",
    "network-interface",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceTypeEnum:
    return cast(ResourceTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceTypeEnum:
    return cast(ResourceTypeEnum, data)

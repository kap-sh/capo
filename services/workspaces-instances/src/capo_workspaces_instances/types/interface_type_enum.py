"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InterfaceTypeEnum``."""

from typing import Literal, TypeAlias, cast

InterfaceTypeEnum: TypeAlias = Literal[
    "interface",
    "efa",
    "efa-only",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterfaceTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InterfaceTypeEnum:
    return cast(InterfaceTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InterfaceTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> InterfaceTypeEnum:
    return cast(InterfaceTypeEnum, data)

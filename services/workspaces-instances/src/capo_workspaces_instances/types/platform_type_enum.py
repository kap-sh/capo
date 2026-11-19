"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PlatformTypeEnum``."""

from typing import Literal, TypeAlias, cast

PlatformTypeEnum: TypeAlias = Literal[
    "Windows",
    "Windows BYOL",
    "Linux/UNIX",
    "Ubuntu Pro Linux",
    "Red Hat Enterprise Linux",
    "Red Hat BYOL Linux",
    "SUSE Linux",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlatformTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PlatformTypeEnum:
    return cast(PlatformTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlatformTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> PlatformTypeEnum:
    return cast(PlatformTypeEnum, data)

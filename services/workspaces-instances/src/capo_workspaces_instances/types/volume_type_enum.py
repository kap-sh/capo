"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#VolumeTypeEnum``."""

from typing import Literal, TypeAlias, cast

VolumeTypeEnum: TypeAlias = Literal[
    "standard",
    "io1",
    "io2",
    "gp2",
    "sc1",
    "st1",
    "gp3",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VolumeTypeEnum:
    return cast(VolumeTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VolumeTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> VolumeTypeEnum:
    return cast(VolumeTypeEnum, data)

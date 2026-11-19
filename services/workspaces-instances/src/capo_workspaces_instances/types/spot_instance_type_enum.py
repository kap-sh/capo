"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SpotInstanceTypeEnum``."""

from typing import Literal, TypeAlias, cast

SpotInstanceTypeEnum: TypeAlias = Literal[
    "one-time",
    "persistent",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpotInstanceTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpotInstanceTypeEnum:
    return cast(SpotInstanceTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SpotInstanceTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> SpotInstanceTypeEnum:
    return cast(SpotInstanceTypeEnum, data)

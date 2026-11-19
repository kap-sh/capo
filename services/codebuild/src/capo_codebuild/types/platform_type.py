"""Generated from Smithy shape ``com.amazonaws.codebuild#PlatformType``."""

from typing import Literal, TypeAlias, cast

PlatformType: TypeAlias = Literal[
    "DEBIAN",
    "AMAZON_LINUX",
    "UBUNTU",
    "WINDOWS_SERVER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformType:
    return cast(PlatformType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlatformType) -> str:
    return value


def deserialize_cbor(data: str) -> PlatformType:
    return cast(PlatformType, data)

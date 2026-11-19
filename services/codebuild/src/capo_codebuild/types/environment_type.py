"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentType``."""

from typing import Literal, TypeAlias, cast

EnvironmentType: TypeAlias = Literal[
    "WINDOWS_CONTAINER",
    "LINUX_CONTAINER",
    "LINUX_GPU_CONTAINER",
    "ARM_CONTAINER",
    "WINDOWS_SERVER_2019_CONTAINER",
    "WINDOWS_SERVER_2022_CONTAINER",
    "LINUX_LAMBDA_CONTAINER",
    "ARM_LAMBDA_CONTAINER",
    "LINUX_EC2",
    "ARM_EC2",
    "WINDOWS_EC2",
    "MAC_ARM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentType:
    return cast(EnvironmentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentType) -> str:
    return value


def deserialize_cbor(data: str) -> EnvironmentType:
    return cast(EnvironmentType, data)

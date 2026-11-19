"""Generated from Smithy shape ``com.amazonaws.codebuild#ComputeType``."""

from typing import Literal, TypeAlias, cast

ComputeType: TypeAlias = Literal[
    "BUILD_GENERAL1_SMALL",
    "BUILD_GENERAL1_MEDIUM",
    "BUILD_GENERAL1_LARGE",
    "BUILD_GENERAL1_XLARGE",
    "BUILD_GENERAL1_2XLARGE",
    "BUILD_LAMBDA_1GB",
    "BUILD_LAMBDA_2GB",
    "BUILD_LAMBDA_4GB",
    "BUILD_LAMBDA_8GB",
    "BUILD_LAMBDA_10GB",
    "ATTRIBUTE_BASED_COMPUTE",
    "CUSTOM_INSTANCE_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeType:
    return cast(ComputeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComputeType) -> str:
    return value


def deserialize_cbor(data: str) -> ComputeType:
    return cast(ComputeType, data)

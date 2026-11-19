"""Generated from Smithy shape ``com.amazonaws.codebuild#RetryBuildBatchType``."""

from typing import Literal, TypeAlias, cast

RetryBuildBatchType: TypeAlias = Literal[
    "RETRY_ALL_BUILDS",
    "RETRY_FAILED_BUILDS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryBuildBatchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetryBuildBatchType:
    return cast(RetryBuildBatchType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryBuildBatchType) -> str:
    return value


def deserialize_cbor(data: str) -> RetryBuildBatchType:
    return cast(RetryBuildBatchType, data)

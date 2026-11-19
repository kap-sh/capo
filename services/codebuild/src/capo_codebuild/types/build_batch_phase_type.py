"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatchPhaseType``."""

from typing import Literal, TypeAlias, cast

BuildBatchPhaseType: TypeAlias = Literal[
    "SUBMITTED",
    "DOWNLOAD_BATCHSPEC",
    "IN_PROGRESS",
    "COMBINE_ARTIFACTS",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatchPhaseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BuildBatchPhaseType:
    return cast(BuildBatchPhaseType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildBatchPhaseType) -> str:
    return value


def deserialize_cbor(data: str) -> BuildBatchPhaseType:
    return cast(BuildBatchPhaseType, data)

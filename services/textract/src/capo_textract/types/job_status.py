"""Generated from Smithy shape ``com.amazonaws.textract#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "PARTIAL_SUCCESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    return cast(JobStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobStatus) -> str:
    return value


def deserialize_cbor(data: str) -> JobStatus:
    return cast(JobStatus, data)

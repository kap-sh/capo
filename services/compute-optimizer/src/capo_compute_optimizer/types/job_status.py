"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "Queued",
    "InProgress",
    "Complete",
    "Failed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> JobStatus:
    return cast(JobStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobStatus) -> str:
    return value


def deserialize_cbor(data: str) -> JobStatus:
    return cast(JobStatus, data)

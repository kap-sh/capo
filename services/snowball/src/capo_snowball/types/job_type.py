"""Generated from Smithy shape ``com.amazonaws.snowball#JobType``."""

from typing import Literal, TypeAlias, cast

JobType: TypeAlias = Literal[
    "IMPORT",
    "EXPORT",
    "LOCAL_USE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobType:
    return cast(JobType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobType) -> str:
    return value


def deserialize_cbor(data: str) -> JobType:
    return cast(JobType, data)

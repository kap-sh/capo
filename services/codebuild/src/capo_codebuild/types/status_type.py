"""Generated from Smithy shape ``com.amazonaws.codebuild#StatusType``."""

from typing import Literal, TypeAlias, cast

StatusType: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "FAULT",
    "TIMED_OUT",
    "IN_PROGRESS",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusType:
    return cast(StatusType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatusType) -> str:
    return value


def deserialize_cbor(data: str) -> StatusType:
    return cast(StatusType, data)

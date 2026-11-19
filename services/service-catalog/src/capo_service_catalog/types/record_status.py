"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordStatus``."""

from typing import Literal, TypeAlias, cast

RecordStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "IN_PROGRESS_IN_ERROR",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordStatus:
    return cast(RecordStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RecordStatus:
    return cast(RecordStatus, data)

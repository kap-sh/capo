"""Generated from Smithy shape ``com.amazonaws.pi#DetailStatus``."""

from typing import Literal, TypeAlias, cast

DetailStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PROCESSING",
    "UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetailStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailStatus:
    return cast(DetailStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetailStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DetailStatus:
    return cast(DetailStatus, data)

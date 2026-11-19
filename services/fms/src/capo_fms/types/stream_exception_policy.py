"""Generated from Smithy shape ``com.amazonaws.fms#StreamExceptionPolicy``."""

from typing import Literal, TypeAlias, cast

StreamExceptionPolicy: TypeAlias = Literal[
    "DROP",
    "CONTINUE",
    "REJECT",
    "FMS_IGNORE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamExceptionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamExceptionPolicy:
    return cast(StreamExceptionPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StreamExceptionPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> StreamExceptionPolicy:
    return cast(StreamExceptionPolicy, data)

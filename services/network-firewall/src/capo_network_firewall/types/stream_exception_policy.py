"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StreamExceptionPolicy``."""

from typing import Literal, TypeAlias, cast

StreamExceptionPolicy: TypeAlias = Literal[
    "DROP",
    "CONTINUE",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamExceptionPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamExceptionPolicy:
    return cast(StreamExceptionPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StreamExceptionPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> StreamExceptionPolicy:
    return cast(StreamExceptionPolicy, data)

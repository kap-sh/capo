"""Generated from Smithy shape ``com.amazonaws.gamelift#FlexMatchMode``."""

from typing import Literal, TypeAlias, cast

FlexMatchMode: TypeAlias = Literal[
    "STANDALONE",
    "WITH_QUEUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlexMatchMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlexMatchMode:
    return cast(FlexMatchMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlexMatchMode) -> str:
    return value


def deserialize_cbor(data: str) -> FlexMatchMode:
    return cast(FlexMatchMode, data)

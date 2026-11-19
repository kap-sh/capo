"""Generated from Smithy shape ``com.amazonaws.appstream#StreamView``."""

from typing import Literal, TypeAlias, cast

StreamView: TypeAlias = Literal[
    "APP",
    "DESKTOP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamView) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamView:
    return cast(StreamView, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StreamView) -> str:
    return value


def deserialize_cbor(data: str) -> StreamView:
    return cast(StreamView, data)

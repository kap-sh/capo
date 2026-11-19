"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessPropertyValue``."""

from typing import Literal, TypeAlias, cast

AccessPropertyValue: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessPropertyValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessPropertyValue:
    return cast(AccessPropertyValue, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessPropertyValue) -> str:
    return value


def deserialize_cbor(data: str) -> AccessPropertyValue:
    return cast(AccessPropertyValue, data)

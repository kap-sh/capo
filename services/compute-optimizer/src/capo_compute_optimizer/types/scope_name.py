"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ScopeName``."""

from typing import Literal, TypeAlias, cast

ScopeName: TypeAlias = Literal[
    "Organization",
    "AccountId",
    "ResourceArn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScopeName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScopeName:
    return cast(ScopeName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScopeName) -> str:
    return value


def deserialize_cbor(data: str) -> ScopeName:
    return cast(ScopeName, data)

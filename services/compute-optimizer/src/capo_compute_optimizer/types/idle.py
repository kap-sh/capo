"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Idle``."""

from typing import Literal, TypeAlias, cast

Idle: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Idle) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Idle:
    return cast(Idle, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Idle) -> str:
    return value


def deserialize_cbor(data: str) -> Idle:
    return cast(Idle, data)

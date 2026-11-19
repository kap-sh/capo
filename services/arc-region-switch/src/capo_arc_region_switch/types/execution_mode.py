"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

ExecutionMode: TypeAlias = Literal[
    "graceful",
    "ungraceful",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionMode:
    return cast(ExecutionMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionMode) -> str:
    return value


def deserialize_cbor(data: str) -> ExecutionMode:
    return cast(ExecutionMode, data)

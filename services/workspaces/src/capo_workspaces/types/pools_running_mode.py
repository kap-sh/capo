"""Generated from Smithy shape ``com.amazonaws.workspaces#PoolsRunningMode``."""

from typing import Literal, TypeAlias, cast

PoolsRunningMode: TypeAlias = Literal[
    "AUTO_STOP",
    "ALWAYS_ON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PoolsRunningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PoolsRunningMode:
    return cast(PoolsRunningMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PoolsRunningMode) -> str:
    return value


def deserialize_cbor(data: str) -> PoolsRunningMode:
    return cast(PoolsRunningMode, data)

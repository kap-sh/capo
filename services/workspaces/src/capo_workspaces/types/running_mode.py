"""Generated from Smithy shape ``com.amazonaws.workspaces#RunningMode``."""

from typing import Literal, TypeAlias, cast

RunningMode: TypeAlias = Literal[
    "AUTO_STOP",
    "ALWAYS_ON",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RunningMode:
    return cast(RunningMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RunningMode) -> str:
    return value


def deserialize_cbor(data: str) -> RunningMode:
    return cast(RunningMode, data)

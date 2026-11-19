"""Generated from Smithy shape ``com.amazonaws.directconnect#LagState``."""

from typing import Literal, TypeAlias, cast

LagState: TypeAlias = Literal[
    "requested",
    "pending",
    "available",
    "down",
    "deleting",
    "deleted",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LagState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LagState:
    return cast(LagState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LagState) -> str:
    return value


def deserialize_cbor(data: str) -> LagState:
    return cast(LagState, data)

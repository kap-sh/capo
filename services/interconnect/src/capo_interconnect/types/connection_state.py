"""Generated from Smithy shape ``com.amazonaws.interconnect#ConnectionState``."""

from typing import Literal, TypeAlias, cast

ConnectionState: TypeAlias = Literal[
    "available",
    "requested",
    "pending",
    "down",
    "deleting",
    "deleted",
    "failed",
    "updating",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionState:
    return cast(ConnectionState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionState) -> str:
    return value


def deserialize_cbor(data: str) -> ConnectionState:
    return cast(ConnectionState, data)

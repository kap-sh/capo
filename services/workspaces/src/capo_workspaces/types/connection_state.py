"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionState``."""

from typing import Literal, TypeAlias, cast

ConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionState:
    return cast(ConnectionState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionState) -> str:
    return value


def deserialize_cbor(data: str) -> ConnectionState:
    return cast(ConnectionState, data)

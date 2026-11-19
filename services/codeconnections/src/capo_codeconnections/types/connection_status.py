"""Generated from Smithy shape ``com.amazonaws.codeconnections#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionStatus: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)

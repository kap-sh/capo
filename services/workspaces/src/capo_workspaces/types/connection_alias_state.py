"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasState``."""

from typing import Literal, TypeAlias, cast

ConnectionAliasState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionAliasState:
    return cast(ConnectionAliasState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAliasState) -> str:
    return value


def deserialize_cbor(data: str) -> ConnectionAliasState:
    return cast(ConnectionAliasState, data)

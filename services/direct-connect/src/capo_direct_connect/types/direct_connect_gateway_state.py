"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayState``."""

from typing import Literal, TypeAlias, cast

DirectConnectGatewayState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayState:
    return cast(DirectConnectGatewayState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayState) -> str:
    return value


def deserialize_cbor(data: str) -> DirectConnectGatewayState:
    return cast(DirectConnectGatewayState, data)

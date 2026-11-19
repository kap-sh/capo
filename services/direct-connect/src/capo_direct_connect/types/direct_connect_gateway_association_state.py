"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationState``."""

from typing import Literal, TypeAlias, cast

DirectConnectGatewayAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "updating",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAssociationState:
    return cast(DirectConnectGatewayAssociationState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayAssociationState) -> str:
    return value


def deserialize_cbor(data: str) -> DirectConnectGatewayAssociationState:
    return cast(DirectConnectGatewayAssociationState, data)

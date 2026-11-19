"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationProposalState``."""

from typing import Literal, TypeAlias, cast

DirectConnectGatewayAssociationProposalState: TypeAlias = Literal[
    "requested",
    "accepted",
    "deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationProposalState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAssociationProposalState:
    return cast(DirectConnectGatewayAssociationProposalState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayAssociationProposalState) -> str:
    return value


def deserialize_cbor(data: str) -> DirectConnectGatewayAssociationProposalState:
    return cast(DirectConnectGatewayAssociationProposalState, data)

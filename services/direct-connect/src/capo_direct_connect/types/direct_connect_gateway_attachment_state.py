"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAttachmentState``."""

from typing import Literal, TypeAlias, cast

DirectConnectGatewayAttachmentState: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAttachmentState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAttachmentState:
    return cast(DirectConnectGatewayAttachmentState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayAttachmentState) -> str:
    return value


def deserialize_cbor(data: str) -> DirectConnectGatewayAttachmentState:
    return cast(DirectConnectGatewayAttachmentState, data)

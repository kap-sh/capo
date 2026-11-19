"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAttachmentType``."""

from typing import Literal, TypeAlias, cast

DirectConnectGatewayAttachmentType: TypeAlias = Literal[
    "TransitVirtualInterface",
    "PrivateVirtualInterface",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAttachmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAttachmentType:
    return cast(DirectConnectGatewayAttachmentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayAttachmentType) -> str:
    return value


def deserialize_cbor(data: str) -> DirectConnectGatewayAttachmentType:
    return cast(DirectConnectGatewayAttachmentType, data)

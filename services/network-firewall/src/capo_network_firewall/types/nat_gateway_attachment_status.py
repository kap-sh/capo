"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

NatGatewayAttachmentStatus: TypeAlias = Literal[
    "CREATING",
    "READY",
    "UPDATING",
    "FAILED",
    "DELETING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayAttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NatGatewayAttachmentStatus:
    return cast(NatGatewayAttachmentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NatGatewayAttachmentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> NatGatewayAttachmentStatus:
    return cast(NatGatewayAttachmentStatus, data)

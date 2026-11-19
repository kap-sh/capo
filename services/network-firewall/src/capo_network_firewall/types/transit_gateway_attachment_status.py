"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TransitGatewayAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

TransitGatewayAttachmentStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "DELETED",
    "FAILED",
    "ERROR",
    "READY",
    "PENDING_ACCEPTANCE",
    "REJECTING",
    "REJECTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransitGatewayAttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransitGatewayAttachmentStatus:
    return cast(TransitGatewayAttachmentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TransitGatewayAttachmentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> TransitGatewayAttachmentStatus:
    return cast(TransitGatewayAttachmentStatus, data)

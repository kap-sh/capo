"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ContainerAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContainerAssociationStatus:
    return cast(ContainerAssociationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerAssociationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerAssociationStatus:
    return cast(ContainerAssociationStatus, data)

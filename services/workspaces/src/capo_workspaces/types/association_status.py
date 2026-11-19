"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationStatus``."""

from typing import Literal, TypeAlias, cast

AssociationStatus: TypeAlias = Literal[
    "NOT_ASSOCIATED",
    "ASSOCIATED_WITH_OWNER_ACCOUNT",
    "ASSOCIATED_WITH_SHARED_ACCOUNT",
    "PENDING_ASSOCIATION",
    "PENDING_DISASSOCIATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationStatus:
    return cast(AssociationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AssociationStatus:
    return cast(AssociationStatus, data)

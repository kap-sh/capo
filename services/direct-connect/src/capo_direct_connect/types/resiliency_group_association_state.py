"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupAssociationState``."""

from typing import Literal, TypeAlias, cast

ResiliencyGroupAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupAssociationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResiliencyGroupAssociationState:
    return cast(ResiliencyGroupAssociationState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyGroupAssociationState) -> str:
    return value


def deserialize_cbor(data: str) -> ResiliencyGroupAssociationState:
    return cast(ResiliencyGroupAssociationState, data)

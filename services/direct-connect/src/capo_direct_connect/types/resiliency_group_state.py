"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupState``."""

from typing import Literal, TypeAlias, cast

ResiliencyGroupState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResiliencyGroupState:
    return cast(ResiliencyGroupState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyGroupState) -> str:
    return value


def deserialize_cbor(data: str) -> ResiliencyGroupState:
    return cast(ResiliencyGroupState, data)

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Approval``."""

from typing import Literal, TypeAlias, cast

Approval: TypeAlias = Literal[
    "approve",
    "decline",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Approval) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Approval:
    return cast(Approval, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Approval) -> str:
    return value


def deserialize_cbor(data: str) -> Approval:
    return cast(Approval, data)

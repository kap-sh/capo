"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    return cast(Status, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Status) -> str:
    return value


def deserialize_cbor(data: str) -> Status:
    return cast(Status, data)

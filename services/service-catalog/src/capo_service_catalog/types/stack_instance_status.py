"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackInstanceStatus``."""

from typing import Literal, TypeAlias, cast

StackInstanceStatus: TypeAlias = Literal[
    "CURRENT",
    "OUTDATED",
    "INOPERABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackInstanceStatus:
    return cast(StackInstanceStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackInstanceStatus) -> str:
    return value


def deserialize_cbor(data: str) -> StackInstanceStatus:
    return cast(StackInstanceStatus, data)

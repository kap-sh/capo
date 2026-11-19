"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackSetOperationType``."""

from typing import Literal, TypeAlias, cast

StackSetOperationType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackSetOperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackSetOperationType:
    return cast(StackSetOperationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackSetOperationType) -> str:
    return value


def deserialize_cbor(data: str) -> StackSetOperationType:
    return cast(StackSetOperationType, data)

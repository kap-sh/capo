"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationTargetType``."""

from typing import Literal, TypeAlias, cast

OperationTargetType: TypeAlias = Literal[
    "NAMESPACE",
    "SERVICE",
    "INSTANCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationTargetType:
    return cast(OperationTargetType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationTargetType) -> str:
    return value


def deserialize_cbor(data: str) -> OperationTargetType:
    return cast(OperationTargetType, data)

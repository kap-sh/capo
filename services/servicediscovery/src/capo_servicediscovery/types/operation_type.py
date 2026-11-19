"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationType``."""

from typing import Literal, TypeAlias, cast

OperationType: TypeAlias = Literal[
    "CREATE_NAMESPACE",
    "DELETE_NAMESPACE",
    "UPDATE_NAMESPACE",
    "UPDATE_SERVICE",
    "REGISTER_INSTANCE",
    "DEREGISTER_INSTANCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationType:
    return cast(OperationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationType) -> str:
    return value


def deserialize_cbor(data: str) -> OperationType:
    return cast(OperationType, data)

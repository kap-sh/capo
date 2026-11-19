"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationFilterName``."""

from typing import Literal, TypeAlias, cast

OperationFilterName: TypeAlias = Literal[
    "NAMESPACE_ID",
    "SERVICE_ID",
    "STATUS",
    "TYPE",
    "UPDATE_DATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationFilterName:
    return cast(OperationFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> OperationFilterName:
    return cast(OperationFilterName, data)

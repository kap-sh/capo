"""Generated from Smithy shape ``com.amazonaws.appstream#StackErrorCode``."""

from typing import Literal, TypeAlias, cast

StackErrorCode: TypeAlias = Literal[
    "STORAGE_CONNECTOR_ERROR",
    "INTERNAL_SERVICE_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackErrorCode:
    return cast(StackErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> StackErrorCode:
    return cast(StackErrorCode, data)

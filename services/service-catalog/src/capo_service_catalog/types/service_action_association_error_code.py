"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionAssociationErrorCode``."""

from typing import Literal, TypeAlias, cast

ServiceActionAssociationErrorCode: TypeAlias = Literal[
    "DUPLICATE_RESOURCE",
    "INTERNAL_FAILURE",
    "LIMIT_EXCEEDED",
    "RESOURCE_NOT_FOUND",
    "THROTTLING",
    "INVALID_PARAMETER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionAssociationErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceActionAssociationErrorCode:
    return cast(ServiceActionAssociationErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceActionAssociationErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceActionAssociationErrorCode:
    return cast(ServiceActionAssociationErrorCode, data)

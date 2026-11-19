"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationErrorCode``."""

from typing import Literal, TypeAlias, cast

UserStackAssociationErrorCode: TypeAlias = Literal[
    "STACK_NOT_FOUND",
    "USER_NAME_NOT_FOUND",
    "DIRECTORY_NOT_FOUND",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociationErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStackAssociationErrorCode:
    return cast(UserStackAssociationErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserStackAssociationErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> UserStackAssociationErrorCode:
    return cast(UserStackAssociationErrorCode, data)

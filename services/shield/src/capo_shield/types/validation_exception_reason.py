"""Generated from Smithy shape ``com.amazonaws.shield#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)

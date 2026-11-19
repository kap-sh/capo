"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "UNKNOWN_OPERATION",
    "UNSUPPORTED_OPERATION",
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "DEPENDENCY_FAILURE",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)

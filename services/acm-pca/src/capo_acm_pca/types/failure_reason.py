"""Generated from Smithy shape ``com.amazonaws.acmpca#FailureReason``."""

from typing import Literal, TypeAlias, cast

FailureReason: TypeAlias = Literal[
    "REQUEST_TIMED_OUT",
    "UNSUPPORTED_ALGORITHM",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureReason:
    return cast(FailureReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailureReason) -> str:
    return value


def deserialize_cbor(data: str) -> FailureReason:
    return cast(FailureReason, data)

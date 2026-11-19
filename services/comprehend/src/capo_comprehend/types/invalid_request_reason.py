"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestReason``."""

from typing import Literal, TypeAlias, cast

InvalidRequestReason: TypeAlias = Literal["INVALID_DOCUMENT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InvalidRequestReason:
    return cast(InvalidRequestReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvalidRequestReason) -> str:
    return value


def deserialize_cbor(data: str) -> InvalidRequestReason:
    return cast(InvalidRequestReason, data)

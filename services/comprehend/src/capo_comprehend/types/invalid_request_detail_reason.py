"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestDetailReason``."""

from typing import Literal, TypeAlias, cast

InvalidRequestDetailReason: TypeAlias = Literal[
    "DOCUMENT_SIZE_EXCEEDED",
    "UNSUPPORTED_DOC_TYPE",
    "PAGE_LIMIT_EXCEEDED",
    "TEXTRACT_ACCESS_DENIED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestDetailReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InvalidRequestDetailReason:
    return cast(InvalidRequestDetailReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvalidRequestDetailReason) -> str:
    return value


def deserialize_cbor(data: str) -> InvalidRequestDetailReason:
    return cast(InvalidRequestDetailReason, data)

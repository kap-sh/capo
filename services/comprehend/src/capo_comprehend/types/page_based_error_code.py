"""Generated from Smithy shape ``com.amazonaws.comprehend#PageBasedErrorCode``."""

from typing import Literal, TypeAlias, cast

PageBasedErrorCode: TypeAlias = Literal[
    "TEXTRACT_BAD_PAGE",
    "TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED",
    "PAGE_CHARACTERS_EXCEEDED",
    "PAGE_SIZE_EXCEEDED",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PageBasedErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PageBasedErrorCode:
    return cast(PageBasedErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PageBasedErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> PageBasedErrorCode:
    return cast(PageBasedErrorCode, data)

"""Generated from Smithy shape ``com.amazonaws.comprehend#PageBasedWarningCode``."""

from typing import Literal, TypeAlias, cast

PageBasedWarningCode: TypeAlias = Literal[
    "INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL",
    "INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PageBasedWarningCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PageBasedWarningCode:
    return cast(PageBasedWarningCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PageBasedWarningCode) -> str:
    return value


def deserialize_cbor(data: str) -> PageBasedWarningCode:
    return cast(PageBasedWarningCode, data)

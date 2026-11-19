"""Generated from Smithy shape ``com.amazonaws.textract#TextType``."""

from typing import Literal, TypeAlias, cast

TextType: TypeAlias = Literal[
    "HANDWRITING",
    "PRINTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextType:
    return cast(TextType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TextType) -> str:
    return value


def deserialize_cbor(data: str) -> TextType:
    return cast(TextType, data)

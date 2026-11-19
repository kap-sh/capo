"""Generated from Smithy shape ``com.amazonaws.comprehend#SyntaxLanguageCode``."""

from typing import Literal, TypeAlias, cast

SyntaxLanguageCode: TypeAlias = Literal[
    "en",
    "es",
    "fr",
    "de",
    "it",
    "pt",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyntaxLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SyntaxLanguageCode:
    return cast(SyntaxLanguageCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SyntaxLanguageCode) -> str:
    return value


def deserialize_cbor(data: str) -> SyntaxLanguageCode:
    return cast(SyntaxLanguageCode, data)

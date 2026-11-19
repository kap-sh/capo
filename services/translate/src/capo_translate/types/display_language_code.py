"""Generated from Smithy shape ``com.amazonaws.translate#DisplayLanguageCode``."""

from typing import Literal, TypeAlias, cast

DisplayLanguageCode: TypeAlias = Literal[
    "de",
    "en",
    "es",
    "fr",
    "it",
    "ja",
    "ko",
    "pt",
    "zh",
    "zh-TW",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisplayLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DisplayLanguageCode:
    return cast(DisplayLanguageCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisplayLanguageCode) -> str:
    return value


def deserialize_cbor(data: str) -> DisplayLanguageCode:
    return cast(DisplayLanguageCode, data)

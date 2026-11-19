"""Generated from Smithy shape ``com.amazonaws.transcribe#CLMLanguageCode``."""

from typing import Literal, TypeAlias, cast

CLMLanguageCode: TypeAlias = Literal[
    "en-US",
    "hi-IN",
    "es-US",
    "en-GB",
    "en-AU",
    "de-DE",
    "ja-JP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CLMLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CLMLanguageCode:
    return cast(CLMLanguageCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CLMLanguageCode) -> str:
    return value


def deserialize_cbor(data: str) -> CLMLanguageCode:
    return cast(CLMLanguageCode, data)

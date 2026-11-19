"""Generated from Smithy shape ``com.amazonaws.comprehend#ToxicContentType``."""

from typing import Literal, TypeAlias, cast

ToxicContentType: TypeAlias = Literal[
    "GRAPHIC",
    "HARASSMENT_OR_ABUSE",
    "HATE_SPEECH",
    "INSULT",
    "PROFANITY",
    "SEXUAL",
    "VIOLENCE_OR_THREAT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ToxicContentType:
    return cast(ToxicContentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ToxicContentType) -> str:
    return value


def deserialize_cbor(data: str) -> ToxicContentType:
    return cast(ToxicContentType, data)

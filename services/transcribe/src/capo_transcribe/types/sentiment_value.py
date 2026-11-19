"""Generated from Smithy shape ``com.amazonaws.transcribe#SentimentValue``."""

from typing import Literal, TypeAlias, cast

SentimentValue: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "NEUTRAL",
    "MIXED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SentimentValue:
    return cast(SentimentValue, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SentimentValue) -> str:
    return value


def deserialize_cbor(data: str) -> SentimentValue:
    return cast(SentimentValue, data)

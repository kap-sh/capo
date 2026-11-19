"""Generated from Smithy shape ``com.amazonaws.comprehend#SentimentType``."""

from typing import Literal, TypeAlias, cast

SentimentType: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "NEUTRAL",
    "MIXED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SentimentType:
    return cast(SentimentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SentimentType) -> str:
    return value


def deserialize_cbor(data: str) -> SentimentType:
    return cast(SentimentType, data)

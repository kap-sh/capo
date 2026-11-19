"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetedSentimentEntityType``."""

from typing import Literal, TypeAlias, cast

TargetedSentimentEntityType: TypeAlias = Literal[
    "PERSON",
    "LOCATION",
    "ORGANIZATION",
    "FACILITY",
    "BRAND",
    "COMMERCIAL_ITEM",
    "MOVIE",
    "MUSIC",
    "BOOK",
    "SOFTWARE",
    "GAME",
    "PERSONAL_TITLE",
    "EVENT",
    "DATE",
    "QUANTITY",
    "ATTRIBUTE",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetedSentimentEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetedSentimentEntityType:
    return cast(TargetedSentimentEntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetedSentimentEntityType) -> str:
    return value


def deserialize_cbor(data: str) -> TargetedSentimentEntityType:
    return cast(TargetedSentimentEntityType, data)

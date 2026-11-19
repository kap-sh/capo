"""Generated from Smithy shape ``com.amazonaws.applicationinsights#FeedbackValue``."""

from typing import Literal, TypeAlias, cast

FeedbackValue: TypeAlias = Literal[
    "NOT_SPECIFIED",
    "USEFUL",
    "NOT_USEFUL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeedbackValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackValue:
    return cast(FeedbackValue, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FeedbackValue) -> str:
    return value


def deserialize_cbor(data: str) -> FeedbackValue:
    return cast(FeedbackValue, data)

"""Generated from Smithy shape ``com.amazonaws.applicationinsights#FeedbackKey``."""

from typing import Literal, TypeAlias, cast

FeedbackKey: TypeAlias = Literal["INSIGHTS_FEEDBACK",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeedbackKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackKey:
    return cast(FeedbackKey, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FeedbackKey) -> str:
    return value


def deserialize_cbor(data: str) -> FeedbackKey:
    return cast(FeedbackKey, data)

"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsFeature``."""

from typing import Literal, TypeAlias, cast

CallAnalyticsFeature: TypeAlias = Literal["GENERATIVE_SUMMARIZATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsFeature) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CallAnalyticsFeature:
    return cast(CallAnalyticsFeature, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CallAnalyticsFeature) -> str:
    return value


def deserialize_cbor(data: str) -> CallAnalyticsFeature:
    return cast(CallAnalyticsFeature, data)

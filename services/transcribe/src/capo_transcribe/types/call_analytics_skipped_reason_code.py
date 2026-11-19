"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsSkippedReasonCode``."""

from typing import Literal, TypeAlias, cast

CallAnalyticsSkippedReasonCode: TypeAlias = Literal[
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsSkippedReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CallAnalyticsSkippedReasonCode:
    return cast(CallAnalyticsSkippedReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CallAnalyticsSkippedReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> CallAnalyticsSkippedReasonCode:
    return cast(CallAnalyticsSkippedReasonCode, data)

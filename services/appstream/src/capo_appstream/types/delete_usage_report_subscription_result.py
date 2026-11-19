"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteUsageReportSubscriptionResult``."""

from typing_extensions import TypedDict


class DeleteUsageReportSubscriptionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUsageReportSubscriptionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUsageReportSubscriptionResult:
    out: DeleteUsageReportSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteUsageReportSubscriptionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteUsageReportSubscriptionResult:
    out: DeleteUsageReportSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out

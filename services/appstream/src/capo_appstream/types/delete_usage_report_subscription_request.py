"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteUsageReportSubscriptionRequest``."""

from typing_extensions import TypedDict


class DeleteUsageReportSubscriptionRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUsageReportSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUsageReportSubscriptionRequest:
    out: DeleteUsageReportSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteUsageReportSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteUsageReportSubscriptionRequest:
    out: DeleteUsageReportSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out

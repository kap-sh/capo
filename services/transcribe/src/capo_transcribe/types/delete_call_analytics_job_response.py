"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteCallAnalyticsJobResponse``."""

from typing_extensions import TypedDict


class DeleteCallAnalyticsJobResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCallAnalyticsJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCallAnalyticsJobResponse:
    out: DeleteCallAnalyticsJobResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteCallAnalyticsJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteCallAnalyticsJobResponse:
    out: DeleteCallAnalyticsJobResponse = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteCallAnalyticsCategoryResponse``."""

from typing_extensions import TypedDict


class DeleteCallAnalyticsCategoryResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCallAnalyticsCategoryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCallAnalyticsCategoryResponse:
    out: DeleteCallAnalyticsCategoryResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteCallAnalyticsCategoryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteCallAnalyticsCategoryResponse:
    out: DeleteCallAnalyticsCategoryResponse = {}  # type: ignore[typeddict-item]
    return out

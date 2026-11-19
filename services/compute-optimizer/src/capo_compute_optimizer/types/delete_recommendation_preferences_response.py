"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DeleteRecommendationPreferencesResponse``."""

from typing_extensions import TypedDict


class DeleteRecommendationPreferencesResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRecommendationPreferencesResponse:
    out: DeleteRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteRecommendationPreferencesResponse:
    out: DeleteRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    return out

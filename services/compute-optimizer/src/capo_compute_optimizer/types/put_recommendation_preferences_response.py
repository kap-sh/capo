"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PutRecommendationPreferencesResponse``."""

from typing_extensions import TypedDict


class PutRecommendationPreferencesResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> PutRecommendationPreferencesResponse:
    out: PutRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> PutRecommendationPreferencesResponse:
    out: PutRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    return out

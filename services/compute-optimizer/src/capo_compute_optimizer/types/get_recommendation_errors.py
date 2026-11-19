"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.get_recommendation_error

GetRecommendationErrors: TypeAlias = list[
    "capo_compute_optimizer.types.get_recommendation_error.GetRecommendationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationErrors) -> list:
    import capo_compute_optimizer.types.get_recommendation_error

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.get_recommendation_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GetRecommendationErrors:
    import capo_compute_optimizer.types.get_recommendation_error

    out: GetRecommendationErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.get_recommendation_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRecommendationErrors) -> list:
    import capo_compute_optimizer.types.get_recommendation_error

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.get_recommendation_error.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> GetRecommendationErrors:
    import capo_compute_optimizer.types.get_recommendation_error

    out: GetRecommendationErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.get_recommendation_error.deserialize_cbor(item)
        )
    return out

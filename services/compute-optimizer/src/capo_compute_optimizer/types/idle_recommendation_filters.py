"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_recommendation_filter

IdleRecommendationFilters: TypeAlias = list[
    "capo_compute_optimizer.types.idle_recommendation_filter.IdleRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationFilters) -> list:
    import capo_compute_optimizer.types.idle_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleRecommendationFilters:
    import capo_compute_optimizer.types.idle_recommendation_filter

    out: IdleRecommendationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.idle_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleRecommendationFilters) -> list:
    import capo_compute_optimizer.types.idle_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_recommendation_filter.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> IdleRecommendationFilters:
    import capo_compute_optimizer.types.idle_recommendation_filter

    out: IdleRecommendationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.idle_recommendation_filter.deserialize_cbor(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_service_recommendation_filter

ECSServiceRecommendationFilters: TypeAlias = list[
    "capo_compute_optimizer.types.ecs_service_recommendation_filter.ECSServiceRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationFilters) -> list:
    import capo_compute_optimizer.types.ecs_service_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceRecommendationFilters:
    import capo_compute_optimizer.types.ecs_service_recommendation_filter

    out: ECSServiceRecommendationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceRecommendationFilters) -> list:
    import capo_compute_optimizer.types.ecs_service_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation_filter.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ECSServiceRecommendationFilters:
    import capo_compute_optimizer.types.ecs_service_recommendation_filter

    out: ECSServiceRecommendationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation_filter.deserialize_cbor(
                item
            )
        )
    return out

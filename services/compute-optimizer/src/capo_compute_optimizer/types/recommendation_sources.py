"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.recommendation_source

RecommendationSources: TypeAlias = list[
    "capo_compute_optimizer.types.recommendation_source.RecommendationSource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSources) -> list:
    import capo_compute_optimizer.types.recommendation_source

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_source.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationSources:
    import capo_compute_optimizer.types.recommendation_source

    out: RecommendationSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.recommendation_source.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationSources) -> list:
    import capo_compute_optimizer.types.recommendation_source

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_source.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> RecommendationSources:
    import capo_compute_optimizer.types.recommendation_source

    out: RecommendationSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.recommendation_source.deserialize_cbor(item)
        )
    return out

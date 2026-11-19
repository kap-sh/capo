"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferenceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.recommendation_preference_name

RecommendationPreferenceNames: TypeAlias = list[
    "capo_compute_optimizer.types.recommendation_preference_name.RecommendationPreferenceName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferenceNames) -> list:
    import capo_compute_optimizer.types.recommendation_preference_name

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_preference_name.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationPreferenceNames:
    import capo_compute_optimizer.types.recommendation_preference_name

    out: RecommendationPreferenceNames = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.recommendation_preference_name.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationPreferenceNames) -> list:
    import capo_compute_optimizer.types.recommendation_preference_name

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_preference_name.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RecommendationPreferenceNames:
    import capo_compute_optimizer.types.recommendation_preference_name

    out: RecommendationPreferenceNames = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.recommendation_preference_name.deserialize_cbor(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.volume_recommendation_option

VolumeRecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.volume_recommendation_option.VolumeRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeRecommendationOptions) -> list:
    import capo_compute_optimizer.types.volume_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.volume_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VolumeRecommendationOptions:
    import capo_compute_optimizer.types.volume_recommendation_option

    out: VolumeRecommendationOptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.volume_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VolumeRecommendationOptions) -> list:
    import capo_compute_optimizer.types.volume_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.volume_recommendation_option.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> VolumeRecommendationOptions:
    import capo_compute_optimizer.types.volume_recommendation_option

    out: VolumeRecommendationOptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.volume_recommendation_option.deserialize_cbor(
                item
            )
        )
    return out

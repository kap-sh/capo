"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.volume_recommendation

VolumeRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.volume_recommendation.VolumeRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeRecommendations) -> list:
    import capo_compute_optimizer.types.volume_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.volume_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VolumeRecommendations:
    import capo_compute_optimizer.types.volume_recommendation

    out: VolumeRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.volume_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VolumeRecommendations) -> list:
    import capo_compute_optimizer.types.volume_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.volume_recommendation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> VolumeRecommendations:
    import capo_compute_optimizer.types.volume_recommendation

    out: VolumeRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.volume_recommendation.deserialize_cbor(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ContainerRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.container_recommendation

ContainerRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.container_recommendation.ContainerRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerRecommendations) -> list:
    import capo_compute_optimizer.types.container_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.container_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContainerRecommendations:
    import capo_compute_optimizer.types.container_recommendation

    out: ContainerRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.container_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerRecommendations) -> list:
    import capo_compute_optimizer.types.container_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.container_recommendation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ContainerRecommendations:
    import capo_compute_optimizer.types.container_recommendation

    out: ContainerRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.container_recommendation.deserialize_cbor(item)
        )
    return out

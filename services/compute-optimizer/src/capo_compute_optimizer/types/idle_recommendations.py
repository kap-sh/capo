"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_recommendation

IdleRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.idle_recommendation.IdleRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendations) -> list:
    import capo_compute_optimizer.types.idle_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleRecommendations:
    import capo_compute_optimizer.types.idle_recommendation

    out: IdleRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.idle_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleRecommendations) -> list:
    import capo_compute_optimizer.types.idle_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_recommendation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> IdleRecommendations:
    import capo_compute_optimizer.types.idle_recommendation

    out: IdleRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.idle_recommendation.deserialize_cbor(item)
        )
    return out

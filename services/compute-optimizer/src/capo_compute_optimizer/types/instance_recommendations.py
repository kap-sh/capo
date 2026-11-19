"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.instance_recommendation

InstanceRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.instance_recommendation.InstanceRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceRecommendations) -> list:
    import capo_compute_optimizer.types.instance_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.instance_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceRecommendations:
    import capo_compute_optimizer.types.instance_recommendation

    out: InstanceRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.instance_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceRecommendations) -> list:
    import capo_compute_optimizer.types.instance_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.instance_recommendation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> InstanceRecommendations:
    import capo_compute_optimizer.types.instance_recommendation

    out: InstanceRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.instance_recommendation.deserialize_cbor(item)
        )
    return out

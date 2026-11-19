"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendationFindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.instance_recommendation_finding_reason_code

InstanceRecommendationFindingReasonCodes: TypeAlias = list[
    "capo_compute_optimizer.types.instance_recommendation_finding_reason_code.InstanceRecommendationFindingReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceRecommendationFindingReasonCodes) -> list:
    import capo_compute_optimizer.types.instance_recommendation_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.instance_recommendation_finding_reason_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceRecommendationFindingReasonCodes:
    import capo_compute_optimizer.types.instance_recommendation_finding_reason_code

    out: InstanceRecommendationFindingReasonCodes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.instance_recommendation_finding_reason_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceRecommendationFindingReasonCodes) -> list:
    import capo_compute_optimizer.types.instance_recommendation_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.instance_recommendation_finding_reason_code.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> InstanceRecommendationFindingReasonCodes:
    import capo_compute_optimizer.types.instance_recommendation_finding_reason_code

    out: InstanceRecommendationFindingReasonCodes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.instance_recommendation_finding_reason_code.deserialize_cbor(
                item
            )
        )
    return out

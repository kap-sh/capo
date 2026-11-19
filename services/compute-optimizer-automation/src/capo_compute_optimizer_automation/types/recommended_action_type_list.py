"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.recommended_action_type

RecommendedActionTypeList: TypeAlias = list[
    "capo_compute_optimizer_automation.types.recommended_action_type.RecommendedActionType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionTypeList) -> list:
    import capo_compute_optimizer_automation.types.recommended_action_type

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.recommended_action_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendedActionTypeList:
    import capo_compute_optimizer_automation.types.recommended_action_type

    out: RecommendedActionTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.recommended_action_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendedActionTypeList) -> list:
    import capo_compute_optimizer_automation.types.recommended_action_type

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.recommended_action_type.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RecommendedActionTypeList:
    import capo_compute_optimizer_automation.types.recommended_action_type

    out: RecommendedActionTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.recommended_action_type.deserialize_cbor(
                item
            )
        )
    return out

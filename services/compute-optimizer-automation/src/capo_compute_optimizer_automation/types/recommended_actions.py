"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.recommended_action

RecommendedActions: TypeAlias = list[
    "capo_compute_optimizer_automation.types.recommended_action.RecommendedAction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActions) -> list:
    import capo_compute_optimizer_automation.types.recommended_action

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.recommended_action.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendedActions:
    import capo_compute_optimizer_automation.types.recommended_action

    out: RecommendedActions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.recommended_action.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendedActions) -> list:
    import capo_compute_optimizer_automation.types.recommended_action

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.recommended_action.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RecommendedActions:
    import capo_compute_optimizer_automation.types.recommended_action

    out: RecommendedActions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.recommended_action.deserialize_cbor(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StringCriteriaConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.string_criteria_condition

StringCriteriaConditionList: TypeAlias = list[
    "capo_compute_optimizer_automation.types.string_criteria_condition.StringCriteriaCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringCriteriaConditionList) -> list:
    import capo_compute_optimizer_automation.types.string_criteria_condition

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.string_criteria_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StringCriteriaConditionList:
    import capo_compute_optimizer_automation.types.string_criteria_condition

    out: StringCriteriaConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.string_criteria_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringCriteriaConditionList) -> list:
    import capo_compute_optimizer_automation.types.string_criteria_condition

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.string_criteria_condition.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> StringCriteriaConditionList:
    import capo_compute_optimizer_automation.types.string_criteria_condition

    out: StringCriteriaConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.string_criteria_condition.deserialize_cbor(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#IntegerCriteriaConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.integer_criteria_condition

IntegerCriteriaConditionList: TypeAlias = list[
    "capo_compute_optimizer_automation.types.integer_criteria_condition.IntegerCriteriaCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IntegerCriteriaConditionList) -> list:
    import capo_compute_optimizer_automation.types.integer_criteria_condition

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.integer_criteria_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IntegerCriteriaConditionList:
    import capo_compute_optimizer_automation.types.integer_criteria_condition

    out: IntegerCriteriaConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.integer_criteria_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegerCriteriaConditionList) -> list:
    import capo_compute_optimizer_automation.types.integer_criteria_condition

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.integer_criteria_condition.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> IntegerCriteriaConditionList:
    import capo_compute_optimizer_automation.types.integer_criteria_condition

    out: IntegerCriteriaConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.integer_criteria_condition.deserialize_cbor(
                item
            )
        )
    return out

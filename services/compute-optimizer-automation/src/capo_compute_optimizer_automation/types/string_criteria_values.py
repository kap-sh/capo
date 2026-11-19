"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StringCriteriaValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.string_criteria_value

StringCriteriaValues: TypeAlias = list[
    "capo_compute_optimizer_automation.types.string_criteria_value.StringCriteriaValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringCriteriaValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringCriteriaValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringCriteriaValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringCriteriaValues:
    return [item for item in data if item is not None]

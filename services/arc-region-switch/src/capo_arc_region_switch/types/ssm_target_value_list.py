"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmTargetValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ssm_target_value

SsmTargetValueList: TypeAlias = list[
    "capo_arc_region_switch.types.ssm_target_value.SsmTargetValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmTargetValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SsmTargetValueList:
    return [item for item in data if item is not None]

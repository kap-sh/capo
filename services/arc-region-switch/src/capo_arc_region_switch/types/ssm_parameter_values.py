"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmParameterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ssm_parameter_value

SsmParameterValues: TypeAlias = list[
    "capo_arc_region_switch.types.ssm_parameter_value.SsmParameterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmParameterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SsmParameterValues:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ssm_target

SsmTargetList: TypeAlias = list["capo_arc_region_switch.types.ssm_target.SsmTarget"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmTargetList) -> list:
    import capo_arc_region_switch.types.ssm_target

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.ssm_target.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SsmTargetList:
    import capo_arc_region_switch.types.ssm_target

    out: SsmTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.ssm_target.deserialize_aws_json_1_0(item)
        )
    return out

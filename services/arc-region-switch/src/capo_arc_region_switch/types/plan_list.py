"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#PlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.abbreviated_plan

PlanList: TypeAlias = list[
    "capo_arc_region_switch.types.abbreviated_plan.AbbreviatedPlan"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlanList) -> list:
    import capo_arc_region_switch.types.abbreviated_plan

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.abbreviated_plan.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PlanList:
    import capo_arc_region_switch.types.abbreviated_plan

    out: PlanList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.abbreviated_plan.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlanList) -> list:
    import capo_arc_region_switch.types.abbreviated_plan

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.abbreviated_plan.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PlanList:
    import capo_arc_region_switch.types.abbreviated_plan

    out: PlanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.abbreviated_plan.deserialize_cbor(item))
    return out

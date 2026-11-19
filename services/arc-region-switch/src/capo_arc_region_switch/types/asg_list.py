"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AsgList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.asg

AsgList: TypeAlias = list["capo_arc_region_switch.types.asg.Asg"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AsgList) -> list:
    import capo_arc_region_switch.types.asg

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.asg.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AsgList:
    import capo_arc_region_switch.types.asg

    out: AsgList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.asg.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AsgList) -> list:
    import capo_arc_region_switch.types.asg

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.asg.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AsgList:
    import capo_arc_region_switch.types.asg

    out: AsgList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.asg.deserialize_cbor(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.trigger

TriggerList: TypeAlias = list["capo_arc_region_switch.types.trigger.Trigger"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerList) -> list:
    import capo_arc_region_switch.types.trigger

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.trigger.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TriggerList:
    import capo_arc_region_switch.types.trigger

    out: TriggerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.trigger.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TriggerList) -> list:
    import capo_arc_region_switch.types.trigger

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.trigger.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TriggerList:
    import capo_arc_region_switch.types.trigger

    out: TriggerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.trigger.deserialize_cbor(item))
    return out

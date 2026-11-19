"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AssociatedAlarmMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.associated_alarm

AssociatedAlarmMap: TypeAlias = dict[
    "str", "capo_arc_region_switch.types.associated_alarm.AssociatedAlarm"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: AssociatedAlarmMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.associated_alarm

        out[key] = capo_arc_region_switch.types.associated_alarm.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociatedAlarmMap:
    out: AssociatedAlarmMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.associated_alarm

        out[key] = (
            capo_arc_region_switch.types.associated_alarm.deserialize_aws_json_1_0(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: AssociatedAlarmMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.associated_alarm

        out[key] = capo_arc_region_switch.types.associated_alarm.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> AssociatedAlarmMap:
    out: AssociatedAlarmMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.associated_alarm

        out[key] = capo_arc_region_switch.types.associated_alarm.deserialize_cbor(value)
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_event

ExecutionEventList: TypeAlias = list[
    "capo_arc_region_switch.types.execution_event.ExecutionEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionEventList) -> list:
    import capo_arc_region_switch.types.execution_event

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.execution_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExecutionEventList:
    import capo_arc_region_switch.types.execution_event

    out: ExecutionEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.execution_event.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionEventList) -> list:
    import capo_arc_region_switch.types.execution_event

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.execution_event.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExecutionEventList:
    import capo_arc_region_switch.types.execution_event

    out: ExecutionEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.execution_event.deserialize_cbor(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.service

ServiceList: TypeAlias = list["capo_arc_region_switch.types.service.Service"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceList) -> list:
    import capo_arc_region_switch.types.service

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.service.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceList:
    import capo_arc_region_switch.types.service

    out: ServiceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.service.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceList) -> list:
    import capo_arc_region_switch.types.service

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.service.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServiceList:
    import capo_arc_region_switch.types.service

    out: ServiceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.service.deserialize_cbor(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region

RegionList: TypeAlias = list["capo_arc_region_switch.types.region.Region"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RegionList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RegionList:
    return [item for item in data if item is not None]

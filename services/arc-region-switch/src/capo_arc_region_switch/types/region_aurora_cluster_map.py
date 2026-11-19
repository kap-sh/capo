"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionAuroraClusterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.aurora_cluster_arn
    import capo_arc_region_switch.types.region

RegionAuroraClusterMap: TypeAlias = dict[
    "capo_arc_region_switch.types.region.Region",
    "capo_arc_region_switch.types.aurora_cluster_arn.AuroraClusterArn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionAuroraClusterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionAuroraClusterMap:
    out: RegionAuroraClusterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: RegionAuroraClusterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> RegionAuroraClusterMap:
    out: RegionAuroraClusterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

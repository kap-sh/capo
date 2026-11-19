"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionNeptuneClusterArnMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.neptune_cluster_arn
    import capo_arc_region_switch.types.region

RegionNeptuneClusterArnMap: TypeAlias = dict[
    "capo_arc_region_switch.types.region.Region",
    "capo_arc_region_switch.types.neptune_cluster_arn.NeptuneClusterArn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionNeptuneClusterArnMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionNeptuneClusterArnMap:
    out: RegionNeptuneClusterArnMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: RegionNeptuneClusterArnMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> RegionNeptuneClusterArnMap:
    out: RegionNeptuneClusterArnMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RdsDbInstanceArnMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.rds_db_instance_arn
    import capo_arc_region_switch.types.region

RdsDbInstanceArnMap: TypeAlias = dict[
    "capo_arc_region_switch.types.region.Region",
    "capo_arc_region_switch.types.rds_db_instance_arn.RdsDbInstanceArn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RdsDbInstanceArnMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsDbInstanceArnMap:
    out: RdsDbInstanceArnMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: RdsDbInstanceArnMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> RdsDbInstanceArnMap:
    out: RdsDbInstanceArnMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

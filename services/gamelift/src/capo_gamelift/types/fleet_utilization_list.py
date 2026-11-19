"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetUtilizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_utilization

FleetUtilizationList: TypeAlias = list[
    "capo_gamelift.types.fleet_utilization.FleetUtilization"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetUtilizationList) -> list:
    import capo_gamelift.types.fleet_utilization

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_utilization.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetUtilizationList:
    import capo_gamelift.types.fleet_utilization

    out: FleetUtilizationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.fleet_utilization.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetUtilizationList) -> list:
    import capo_gamelift.types.fleet_utilization

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_utilization.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FleetUtilizationList:
    import capo_gamelift.types.fleet_utilization

    out: FleetUtilizationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.fleet_utilization.deserialize_cbor(item))
    return out

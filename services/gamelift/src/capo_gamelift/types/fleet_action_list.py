"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_action

FleetActionList: TypeAlias = list["capo_gamelift.types.fleet_action.FleetAction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetActionList) -> list:
    import capo_gamelift.types.fleet_action

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetActionList:
    import capo_gamelift.types.fleet_action

    out: FleetActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.fleet_action.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetActionList) -> list:
    import capo_gamelift.types.fleet_action

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_action.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FleetActionList:
    import capo_gamelift.types.fleet_action

    out: FleetActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.fleet_action.deserialize_cbor(item))
    return out

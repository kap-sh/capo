"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id

FleetIdList: TypeAlias = list["capo_gamelift.types.fleet_id.FleetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FleetIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FleetIdList:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetIdOrArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn

FleetIdOrArnList: TypeAlias = list["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetIdOrArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FleetIdOrArnList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetIdOrArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FleetIdOrArnList:
    return [item for item in data if item is not None]

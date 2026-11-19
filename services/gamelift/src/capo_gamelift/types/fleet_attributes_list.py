"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_attributes

FleetAttributesList: TypeAlias = list[
    "capo_gamelift.types.fleet_attributes.FleetAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAttributesList) -> list:
    import capo_gamelift.types.fleet_attributes

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetAttributesList:
    import capo_gamelift.types.fleet_attributes

    out: FleetAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.fleet_attributes.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetAttributesList) -> list:
    import capo_gamelift.types.fleet_attributes

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.fleet_attributes.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FleetAttributesList:
    import capo_gamelift.types.fleet_attributes

    out: FleetAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.fleet_attributes.deserialize_cbor(item))
    return out

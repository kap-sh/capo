"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetLocationAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_fleet_location_attributes

ContainerFleetLocationAttributesList: TypeAlias = list[
    "capo_gamelift.types.container_fleet_location_attributes.ContainerFleetLocationAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetLocationAttributesList) -> list:
    import capo_gamelift.types.container_fleet_location_attributes

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_fleet_location_attributes.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerFleetLocationAttributesList:
    import capo_gamelift.types.container_fleet_location_attributes

    out: ContainerFleetLocationAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_fleet_location_attributes.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerFleetLocationAttributesList) -> list:
    import capo_gamelift.types.container_fleet_location_attributes

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_fleet_location_attributes.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ContainerFleetLocationAttributesList:
    import capo_gamelift.types.container_fleet_location_attributes

    out: ContainerFleetLocationAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_fleet_location_attributes.deserialize_cbor(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetRemoveAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_fleet_remove_attribute

ContainerFleetRemoveAttributeList: TypeAlias = list[
    "capo_gamelift.types.container_fleet_remove_attribute.ContainerFleetRemoveAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetRemoveAttributeList) -> list:
    import capo_gamelift.types.container_fleet_remove_attribute

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_fleet_remove_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerFleetRemoveAttributeList:
    import capo_gamelift.types.container_fleet_remove_attribute

    out: ContainerFleetRemoveAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_fleet_remove_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerFleetRemoveAttributeList) -> list:
    import capo_gamelift.types.container_fleet_remove_attribute

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_fleet_remove_attribute.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ContainerFleetRemoveAttributeList:
    import capo_gamelift.types.container_fleet_remove_attribute

    out: ContainerFleetRemoveAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_fleet_remove_attribute.deserialize_cbor(item)
        )
    return out

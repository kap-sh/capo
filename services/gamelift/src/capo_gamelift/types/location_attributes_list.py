"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.location_attributes

LocationAttributesList: TypeAlias = list[
    "capo_gamelift.types.location_attributes.LocationAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationAttributesList) -> list:
    import capo_gamelift.types.location_attributes

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationAttributesList:
    import capo_gamelift.types.location_attributes

    out: LocationAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.location_attributes.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationAttributesList) -> list:
    import capo_gamelift.types.location_attributes

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_attributes.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LocationAttributesList:
    import capo_gamelift.types.location_attributes

    out: LocationAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.location_attributes.deserialize_cbor(item))
    return out

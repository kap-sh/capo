"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.location_configuration

LocationConfigurationList: TypeAlias = list[
    "capo_gamelift.types.location_configuration.LocationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationConfigurationList) -> list:
    import capo_gamelift.types.location_configuration

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.location_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LocationConfigurationList:
    import capo_gamelift.types.location_configuration

    out: LocationConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.location_configuration.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationConfigurationList) -> list:
    import capo_gamelift.types.location_configuration

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_configuration.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LocationConfigurationList:
    import capo_gamelift.types.location_configuration

    out: LocationConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.location_configuration.deserialize_cbor(item))
    return out

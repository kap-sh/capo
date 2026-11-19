"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.location_filter

LocationFilterList: TypeAlias = list[
    "capo_gamelift.types.location_filter.LocationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilterList) -> list:
    import capo_gamelift.types.location_filter

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationFilterList:
    import capo_gamelift.types.location_filter

    out: LocationFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.location_filter.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationFilterList) -> list:
    import capo_gamelift.types.location_filter

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LocationFilterList:
    import capo_gamelift.types.location_filter

    out: LocationFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.location_filter.deserialize_cbor(item))
    return out

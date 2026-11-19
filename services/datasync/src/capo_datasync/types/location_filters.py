"""Generated from Smithy shape ``com.amazonaws.datasync#LocationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.location_filter

LocationFilters: TypeAlias = list["capo_datasync.types.location_filter.LocationFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilters) -> list:
    import capo_datasync.types.location_filter

    out: list = []
    for item in value:
        out.append(capo_datasync.types.location_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationFilters:
    import capo_datasync.types.location_filter

    out: LocationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.location_filter.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationFilters) -> list:
    import capo_datasync.types.location_filter

    out: list = []
    for item in value:
        out.append(capo_datasync.types.location_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LocationFilters:
    import capo_datasync.types.location_filter

    out: LocationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.location_filter.deserialize_cbor(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35DeviceRestrictions``."""

from typing import Literal, TypeAlias, cast

"""Corresponds to the device_restrictions parameter in a segmentation_descriptor. If you include one of the "restriction" flags then you must include all four of them."""
Scte35DeviceRestrictions: TypeAlias = Literal[
    "NONE",
    "RESTRICT_GROUP0",
    "RESTRICT_GROUP1",
    "RESTRICT_GROUP2",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35DeviceRestrictions) -> str:
    return value


def deserialize_json(data: str) -> Scte35DeviceRestrictions:
    return cast(Scte35DeviceRestrictions, data)

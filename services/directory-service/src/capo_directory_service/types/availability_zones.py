"""Generated from Smithy shape ``com.amazonaws.directoryservice#AvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.availability_zone

AvailabilityZones: TypeAlias = list[
    "capo_directory_service.types.availability_zone.AvailabilityZone"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZones) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AvailabilityZones:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AvailabilityZones) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AvailabilityZones:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.directoryservice#AdditionalRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.region_name

AdditionalRegions: TypeAlias = list[
    "capo_directory_service.types.region_name.RegionName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalRegions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AdditionalRegions:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdditionalRegions) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AdditionalRegions:
    return [item for item in data if item is not None]

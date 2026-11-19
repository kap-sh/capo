"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackSetRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.region

StackSetRegions: TypeAlias = list["capo_service_catalog.types.region.Region"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackSetRegions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StackSetRegions:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackSetRegions) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StackSetRegions:
    return [item for item in data if item is not None]

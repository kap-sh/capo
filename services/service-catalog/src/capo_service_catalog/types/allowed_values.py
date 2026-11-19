"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AllowedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.string

AllowedValues: TypeAlias = list["capo_service_catalog.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AllowedValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AllowedValues:
    return [item for item in data if item is not None]

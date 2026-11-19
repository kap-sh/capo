"""Generated from Smithy shape ``com.amazonaws.servicecatalog#OutputKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.output_key

OutputKeys: TypeAlias = list["capo_service_catalog.types.output_key.OutputKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OutputKeys:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OutputKeys) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OutputKeys:
    return [item for item in data if item is not None]

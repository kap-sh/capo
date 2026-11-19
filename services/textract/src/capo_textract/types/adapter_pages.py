"""Generated from Smithy shape ``com.amazonaws.textract#AdapterPages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.adapter_page

AdapterPages: TypeAlias = list["capo_textract.types.adapter_page.AdapterPage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterPages) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AdapterPages:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdapterPages) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AdapterPages:
    return [item for item in data if item is not None]

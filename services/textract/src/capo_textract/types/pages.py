"""Generated from Smithy shape ``com.amazonaws.textract#Pages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.u_integer

Pages: TypeAlias = list["capo_textract.types.u_integer.UInteger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Pages) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Pages:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Pages) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Pages:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.textract#PageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.u_integer

PageList: TypeAlias = list["capo_textract.types.u_integer.UInteger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PageList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PageList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PageList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PageList:
    return [item for item in data if item is not None]

"""Generated from Smithy shape ``com.amazonaws.textract#IdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.non_empty_string

IdList: TypeAlias = list["capo_textract.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IdList:
    return [item for item in data if item is not None]

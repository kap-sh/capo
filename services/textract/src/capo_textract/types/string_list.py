"""Generated from Smithy shape ``com.amazonaws.textract#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.string

StringList: TypeAlias = list["capo_textract.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringList:
    return [item for item in data if item is not None]

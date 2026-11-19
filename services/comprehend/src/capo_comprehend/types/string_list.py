"""Generated from Smithy shape ``com.amazonaws.comprehend#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.string

StringList: TypeAlias = list["capo_comprehend.types.string.String"]


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

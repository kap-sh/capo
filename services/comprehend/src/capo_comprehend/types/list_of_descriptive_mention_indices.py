"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDescriptiveMentionIndices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.integer

ListOfDescriptiveMentionIndices: TypeAlias = list[
    "capo_comprehend.types.integer.Integer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDescriptiveMentionIndices) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListOfDescriptiveMentionIndices:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfDescriptiveMentionIndices) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ListOfDescriptiveMentionIndices:
    return [item for item in data if item is not None]

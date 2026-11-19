"""Generated from Smithy shape ``com.amazonaws.comprehend#LabelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.label_list_item

LabelsList: TypeAlias = list["capo_comprehend.types.label_list_item.LabelListItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LabelsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LabelsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> LabelsList:
    return [item for item in data if item is not None]

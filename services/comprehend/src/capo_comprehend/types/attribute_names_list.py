"""Generated from Smithy shape ``com.amazonaws.comprehend#AttributeNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.attribute_names_list_item

AttributeNamesList: TypeAlias = list[
    "capo_comprehend.types.attribute_names_list_item.AttributeNamesListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AttributeNamesList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttributeNamesList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AttributeNamesList:
    return [item for item in data if item is not None]

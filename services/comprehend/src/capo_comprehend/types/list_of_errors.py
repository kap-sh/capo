"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.errors_list_item

ListOfErrors: TypeAlias = list["capo_comprehend.types.errors_list_item.ErrorsListItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfErrors) -> list:
    import capo_comprehend.types.errors_list_item

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.errors_list_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfErrors:
    import capo_comprehend.types.errors_list_item

    out: ListOfErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.errors_list_item.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfErrors) -> list:
    import capo_comprehend.types.errors_list_item

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.errors_list_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfErrors:
    import capo_comprehend.types.errors_list_item

    out: ListOfErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.errors_list_item.deserialize_cbor(item))
    return out

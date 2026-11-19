"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDocumentType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.document_type_list_item

ListOfDocumentType: TypeAlias = list[
    "capo_comprehend.types.document_type_list_item.DocumentTypeListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDocumentType) -> list:
    import capo_comprehend.types.document_type_list_item

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.document_type_list_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDocumentType:
    import capo_comprehend.types.document_type_list_item

    out: ListOfDocumentType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.document_type_list_item.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfDocumentType) -> list:
    import capo_comprehend.types.document_type_list_item

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.document_type_list_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfDocumentType:
    import capo_comprehend.types.document_type_list_item

    out: ListOfDocumentType = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.document_type_list_item.deserialize_cbor(item))
    return out

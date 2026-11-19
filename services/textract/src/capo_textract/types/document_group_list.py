"""Generated from Smithy shape ``com.amazonaws.textract#DocumentGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.document_group

DocumentGroupList: TypeAlias = list["capo_textract.types.document_group.DocumentGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentGroupList) -> list:
    import capo_textract.types.document_group

    out: list = []
    for item in value:
        out.append(capo_textract.types.document_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentGroupList:
    import capo_textract.types.document_group

    out: DocumentGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.document_group.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentGroupList) -> list:
    import capo_textract.types.document_group

    out: list = []
    for item in value:
        out.append(capo_textract.types.document_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DocumentGroupList:
    import capo_textract.types.document_group

    out: DocumentGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.document_group.deserialize_cbor(item))
    return out

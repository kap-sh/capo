"""Generated from Smithy shape ``com.amazonaws.textract#IdentityDocumentFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.identity_document_field

IdentityDocumentFieldList: TypeAlias = list[
    "capo_textract.types.identity_document_field.IdentityDocumentField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDocumentFieldList) -> list:
    import capo_textract.types.identity_document_field

    out: list = []
    for item in value:
        out.append(
            capo_textract.types.identity_document_field.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IdentityDocumentFieldList:
    import capo_textract.types.identity_document_field

    out: IdentityDocumentFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.identity_document_field.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityDocumentFieldList) -> list:
    import capo_textract.types.identity_document_field

    out: list = []
    for item in value:
        out.append(capo_textract.types.identity_document_field.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IdentityDocumentFieldList:
    import capo_textract.types.identity_document_field

    out: IdentityDocumentFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.identity_document_field.deserialize_cbor(item))
    return out

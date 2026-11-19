"""Generated from Smithy shape ``com.amazonaws.textract#IdentityDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.identity_document

IdentityDocumentList: TypeAlias = list[
    "capo_textract.types.identity_document.IdentityDocument"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDocumentList) -> list:
    import capo_textract.types.identity_document

    out: list = []
    for item in value:
        out.append(capo_textract.types.identity_document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IdentityDocumentList:
    import capo_textract.types.identity_document

    out: IdentityDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.identity_document.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityDocumentList) -> list:
    import capo_textract.types.identity_document

    out: list = []
    for item in value:
        out.append(capo_textract.types.identity_document.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IdentityDocumentList:
    import capo_textract.types.identity_document

    out: IdentityDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.identity_document.deserialize_cbor(item))
    return out

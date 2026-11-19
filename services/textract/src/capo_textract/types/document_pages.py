"""Generated from Smithy shape ``com.amazonaws.textract#DocumentPages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.document

DocumentPages: TypeAlias = list["capo_textract.types.document.Document"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentPages) -> list:
    import capo_textract.types.document

    out: list = []
    for item in value:
        out.append(capo_textract.types.document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentPages:
    import capo_textract.types.document

    out: DocumentPages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.document.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentPages) -> list:
    import capo_textract.types.document

    out: list = []
    for item in value:
        out.append(capo_textract.types.document.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DocumentPages:
    import capo_textract.types.document

    out: DocumentPages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.document.deserialize_cbor(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentType``."""

from typing import Literal, TypeAlias, cast

DocumentType: TypeAlias = Literal[
    "NATIVE_PDF",
    "SCANNED_PDF",
    "MS_WORD",
    "IMAGE",
    "PLAIN_TEXT",
    "TEXTRACT_DETECT_DOCUMENT_TEXT_JSON",
    "TEXTRACT_ANALYZE_DOCUMENT_JSON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentType:
    return cast(DocumentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentType) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentType:
    return cast(DocumentType, data)

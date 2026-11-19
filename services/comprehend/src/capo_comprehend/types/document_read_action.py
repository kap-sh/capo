"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReadAction``."""

from typing import Literal, TypeAlias, cast

DocumentReadAction: TypeAlias = Literal[
    "TEXTRACT_DETECT_DOCUMENT_TEXT",
    "TEXTRACT_ANALYZE_DOCUMENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReadAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReadAction:
    return cast(DocumentReadAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentReadAction) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentReadAction:
    return cast(DocumentReadAction, data)

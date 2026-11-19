"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierDocumentTypeFormat``."""

from typing import Literal, TypeAlias, cast

DocumentClassifierDocumentTypeFormat: TypeAlias = Literal[
    "PLAIN_TEXT_DOCUMENT",
    "SEMI_STRUCTURED_DOCUMENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierDocumentTypeFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentClassifierDocumentTypeFormat:
    return cast(DocumentClassifierDocumentTypeFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassifierDocumentTypeFormat) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentClassifierDocumentTypeFormat:
    return cast(DocumentClassifierDocumentTypeFormat, data)

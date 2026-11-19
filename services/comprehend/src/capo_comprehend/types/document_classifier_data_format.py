"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierDataFormat``."""

from typing import Literal, TypeAlias, cast

DocumentClassifierDataFormat: TypeAlias = Literal[
    "COMPREHEND_CSV",
    "AUGMENTED_MANIFEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentClassifierDataFormat:
    return cast(DocumentClassifierDataFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassifierDataFormat) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentClassifierDataFormat:
    return cast(DocumentClassifierDataFormat, data)

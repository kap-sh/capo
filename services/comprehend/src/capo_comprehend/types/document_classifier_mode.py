"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierMode``."""

from typing import Literal, TypeAlias, cast

DocumentClassifierMode: TypeAlias = Literal[
    "MULTI_CLASS",
    "MULTI_LABEL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentClassifierMode:
    return cast(DocumentClassifierMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassifierMode) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentClassifierMode:
    return cast(DocumentClassifierMode, data)

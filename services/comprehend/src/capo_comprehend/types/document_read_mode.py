"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReadMode``."""

from typing import Literal, TypeAlias, cast

DocumentReadMode: TypeAlias = Literal[
    "SERVICE_DEFAULT",
    "FORCE_DOCUMENT_READ_ACTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReadMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReadMode:
    return cast(DocumentReadMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentReadMode) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentReadMode:
    return cast(DocumentReadMode, data)

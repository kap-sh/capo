"""Generated from Smithy shape ``com.amazonaws.comprehend#SemiStructuredDocumentBlob``."""

import base64
from typing import TypeAlias

SemiStructuredDocumentBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SemiStructuredDocumentBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> SemiStructuredDocumentBlob:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SemiStructuredDocumentBlob) -> SemiStructuredDocumentBlob:
    return value


def deserialize_cbor(data: SemiStructuredDocumentBlob) -> SemiStructuredDocumentBlob:
    return data

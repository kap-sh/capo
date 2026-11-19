"""Generated from Smithy shape ``com.amazonaws.translate#TranslatedDocumentContent``."""

import base64
from typing import TypeAlias

TranslatedDocumentContent: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslatedDocumentContent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> TranslatedDocumentContent:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TranslatedDocumentContent) -> TranslatedDocumentContent:
    return value


def deserialize_cbor(data: TranslatedDocumentContent) -> TranslatedDocumentContent:
    return data

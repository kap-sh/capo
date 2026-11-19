"""Generated from Smithy shape ``com.amazonaws.translate#DocumentContent``."""

import base64
from typing import TypeAlias

DocumentContent: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentContent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> DocumentContent:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentContent) -> DocumentContent:
    return value


def deserialize_cbor(data: DocumentContent) -> DocumentContent:
    return data

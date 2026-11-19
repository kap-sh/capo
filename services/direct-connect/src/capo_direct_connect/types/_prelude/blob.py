"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import base64


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> bytes:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: bytes) -> bytes:
    return value


def deserialize_cbor(data: bytes) -> bytes:
    return data

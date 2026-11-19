"""Generated from Smithy shape ``com.amazonaws.acmpca#CsrBlob``."""

import base64
from typing import TypeAlias

CsrBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CsrBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> CsrBlob:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CsrBlob) -> CsrBlob:
    return value


def deserialize_cbor(data: CsrBlob) -> CsrBlob:
    return data

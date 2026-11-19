"""Generated from Smithy shape ``com.amazonaws.gamelift#ZipBlob``."""

import base64
from typing import TypeAlias

ZipBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZipBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ZipBlob:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ZipBlob) -> ZipBlob:
    return value


def deserialize_cbor(data: ZipBlob) -> ZipBlob:
    return data

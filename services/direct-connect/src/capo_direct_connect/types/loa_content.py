"""Generated from Smithy shape ``com.amazonaws.directconnect#LoaContent``."""

import base64
from typing import TypeAlias

LoaContent: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoaContent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> LoaContent:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LoaContent) -> LoaContent:
    return value


def deserialize_cbor(data: LoaContent) -> LoaContent:
    return data

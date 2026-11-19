"""Generated from Smithy shape ``com.amazonaws.workspaces#Ios2XLogo``."""

import base64
from typing import TypeAlias

Ios2XLogo: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ios2XLogo) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> Ios2XLogo:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ios2XLogo) -> Ios2XLogo:
    return value


def deserialize_cbor(data: Ios2XLogo) -> Ios2XLogo:
    return data

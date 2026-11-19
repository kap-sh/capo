"""Generated from Smithy shape ``com.amazonaws.workspaces#DefaultLogo``."""

import base64
from typing import TypeAlias

DefaultLogo: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultLogo) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> DefaultLogo:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DefaultLogo) -> DefaultLogo:
    return value


def deserialize_cbor(data: DefaultLogo) -> DefaultLogo:
    return data

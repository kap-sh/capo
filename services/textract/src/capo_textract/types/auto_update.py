"""Generated from Smithy shape ``com.amazonaws.textract#AutoUpdate``."""

from typing import Literal, TypeAlias, cast

AutoUpdate: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoUpdate) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoUpdate:
    return cast(AutoUpdate, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoUpdate) -> str:
    return value


def deserialize_cbor(data: str) -> AutoUpdate:
    return cast(AutoUpdate, data)

"""Generated from Smithy shape ``com.amazonaws.datasync#OverwriteMode``."""

from typing import Literal, TypeAlias, cast

OverwriteMode: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverwriteMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteMode:
    return cast(OverwriteMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OverwriteMode) -> str:
    return value


def deserialize_cbor(data: str) -> OverwriteMode:
    return cast(OverwriteMode, data)

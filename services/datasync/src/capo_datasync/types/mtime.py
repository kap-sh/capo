"""Generated from Smithy shape ``com.amazonaws.datasync#Mtime``."""

from typing import Literal, TypeAlias, cast

Mtime: TypeAlias = Literal[
    "NONE",
    "PRESERVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mtime) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Mtime:
    return cast(Mtime, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Mtime) -> str:
    return value


def deserialize_cbor(data: str) -> Mtime:
    return cast(Mtime, data)

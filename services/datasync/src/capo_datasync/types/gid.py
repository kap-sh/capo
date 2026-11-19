"""Generated from Smithy shape ``com.amazonaws.datasync#Gid``."""

from typing import Literal, TypeAlias, cast

Gid: TypeAlias = Literal[
    "NONE",
    "INT_VALUE",
    "NAME",
    "BOTH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Gid) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Gid:
    return cast(Gid, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Gid) -> str:
    return value


def deserialize_cbor(data: str) -> Gid:
    return cast(Gid, data)

"""Generated from Smithy shape ``com.amazonaws.datasync#Atime``."""

from typing import Literal, TypeAlias, cast

Atime: TypeAlias = Literal[
    "NONE",
    "BEST_EFFORT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Atime) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Atime:
    return cast(Atime, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Atime) -> str:
    return value


def deserialize_cbor(data: str) -> Atime:
    return cast(Atime, data)

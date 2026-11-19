"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectorySize``."""

from typing import Literal, TypeAlias, cast

DirectorySize: TypeAlias = Literal[
    "Small",
    "Large",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectorySize) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectorySize:
    return cast(DirectorySize, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectorySize) -> str:
    return value


def deserialize_cbor(data: str) -> DirectorySize:
    return cast(DirectorySize, data)

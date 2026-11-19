"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryType``."""

from typing import Literal, TypeAlias, cast

DirectoryType: TypeAlias = Literal[
    "SimpleAD",
    "ADConnector",
    "MicrosoftAD",
    "SharedMicrosoftAD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryType:
    return cast(DirectoryType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryType) -> str:
    return value


def deserialize_cbor(data: str) -> DirectoryType:
    return cast(DirectoryType, data)

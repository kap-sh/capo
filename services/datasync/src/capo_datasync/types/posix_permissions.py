"""Generated from Smithy shape ``com.amazonaws.datasync#PosixPermissions``."""

from typing import Literal, TypeAlias, cast

PosixPermissions: TypeAlias = Literal[
    "NONE",
    "PRESERVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PosixPermissions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PosixPermissions:
    return cast(PosixPermissions, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PosixPermissions) -> str:
    return value


def deserialize_cbor(data: str) -> PosixPermissions:
    return cast(PosixPermissions, data)

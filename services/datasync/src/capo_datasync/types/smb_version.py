"""Generated from Smithy shape ``com.amazonaws.datasync#SmbVersion``."""

from typing import Literal, TypeAlias, cast

SmbVersion: TypeAlias = Literal[
    "AUTOMATIC",
    "SMB2",
    "SMB3",
    "SMB1",
    "SMB2_0",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmbVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SmbVersion:
    return cast(SmbVersion, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SmbVersion) -> str:
    return value


def deserialize_cbor(data: str) -> SmbVersion:
    return cast(SmbVersion, data)

"""Generated from Smithy shape ``com.amazonaws.codebuild#FileSystemType``."""

from typing import Literal, TypeAlias, cast

FileSystemType: TypeAlias = Literal["EFS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemType:
    return cast(FileSystemType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FileSystemType) -> str:
    return value


def deserialize_cbor(data: str) -> FileSystemType:
    return cast(FileSystemType, data)

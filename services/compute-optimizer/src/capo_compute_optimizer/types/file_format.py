"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FileFormat``."""

from typing import Literal, TypeAlias, cast

FileFormat: TypeAlias = Literal["Csv",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FileFormat:
    return cast(FileFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FileFormat) -> str:
    return value


def deserialize_cbor(data: str) -> FileFormat:
    return cast(FileFormat, data)

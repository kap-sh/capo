"""Generated from Smithy shape ``com.amazonaws.codedeploy#FileExistsBehavior``."""

from typing import Literal, TypeAlias, cast

FileExistsBehavior: TypeAlias = Literal[
    "DISALLOW",
    "OVERWRITE",
    "RETAIN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileExistsBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileExistsBehavior:
    return cast(FileExistsBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FileExistsBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> FileExistsBehavior:
    return cast(FileExistsBehavior, data)

"""Generated from Smithy shape ``com.amazonaws.workspaces#LogUploadEnum``."""

from typing import Literal, TypeAlias, cast

LogUploadEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogUploadEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogUploadEnum:
    return cast(LogUploadEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogUploadEnum) -> str:
    return value


def deserialize_cbor(data: str) -> LogUploadEnum:
    return cast(LogUploadEnum, data)

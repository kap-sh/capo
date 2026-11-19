"""Generated from Smithy shape ``com.amazonaws.datasync#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "OFF",
    "BASIC",
    "TRANSFER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogLevel:
    return cast(LogLevel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogLevel) -> str:
    return value


def deserialize_cbor(data: str) -> LogLevel:
    return cast(LogLevel, data)

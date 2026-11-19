"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LogFilter``."""

from typing import Literal, TypeAlias, cast

LogFilter: TypeAlias = Literal[
    "ERROR",
    "WARN",
    "INFO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogFilter:
    return cast(LogFilter, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogFilter) -> str:
    return value


def deserialize_cbor(data: str) -> LogFilter:
    return cast(LogFilter, data)

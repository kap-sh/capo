"""Generated from Smithy shape ``com.amazonaws.gamelift#LogDestination``."""

from typing import Literal, TypeAlias, cast

LogDestination: TypeAlias = Literal[
    "NONE",
    "CLOUDWATCH",
    "S3",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDestination) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogDestination:
    return cast(LogDestination, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogDestination) -> str:
    return value


def deserialize_cbor(data: str) -> LogDestination:
    return cast(LogDestination, data)

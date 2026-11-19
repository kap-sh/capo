"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanOperator``."""

from typing import Literal, TypeAlias, cast

ArchiveBooleanOperator: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveBooleanOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveBooleanOperator:
    return cast(ArchiveBooleanOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveBooleanOperator) -> str:
    return value


def deserialize_cbor(data: str) -> ArchiveBooleanOperator:
    return cast(ArchiveBooleanOperator, data)

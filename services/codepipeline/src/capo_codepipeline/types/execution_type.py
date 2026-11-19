"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionType``."""

from typing import Literal, TypeAlias, cast

ExecutionType: TypeAlias = Literal[
    "STANDARD",
    "ROLLBACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionType:
    return cast(ExecutionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionType) -> str:
    return value


def deserialize_cbor(data: str) -> ExecutionType:
    return cast(ExecutionType, data)

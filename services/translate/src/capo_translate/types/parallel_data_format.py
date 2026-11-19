"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataFormat``."""

from typing import Literal, TypeAlias, cast

ParallelDataFormat: TypeAlias = Literal[
    "TSV",
    "CSV",
    "TMX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParallelDataFormat:
    return cast(ParallelDataFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParallelDataFormat) -> str:
    return value


def deserialize_cbor(data: str) -> ParallelDataFormat:
    return cast(ParallelDataFormat, data)

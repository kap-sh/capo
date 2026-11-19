"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineType``."""

from typing import Literal, TypeAlias, cast

PipelineType: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineType:
    return cast(PipelineType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineType) -> str:
    return value


def deserialize_cbor(data: str) -> PipelineType:
    return cast(PipelineType, data)

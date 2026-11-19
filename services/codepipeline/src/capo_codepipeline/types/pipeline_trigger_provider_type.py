"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineTriggerProviderType``."""

from typing import Literal, TypeAlias, cast

PipelineTriggerProviderType: TypeAlias = Literal["CodeStarSourceConnection",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineTriggerProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineTriggerProviderType:
    return cast(PipelineTriggerProviderType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineTriggerProviderType) -> str:
    return value


def deserialize_cbor(data: str) -> PipelineTriggerProviderType:
    return cast(PipelineTriggerProviderType, data)

"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_variable

PipelineVariableList: TypeAlias = list[
    "capo_codepipeline.types.pipeline_variable.PipelineVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVariableList) -> list:
    import capo_codepipeline.types.pipeline_variable

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_variable.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineVariableList:
    import capo_codepipeline.types.pipeline_variable

    out: PipelineVariableList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.pipeline_variable.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineVariableList) -> list:
    import capo_codepipeline.types.pipeline_variable

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.pipeline_variable.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PipelineVariableList:
    import capo_codepipeline.types.pipeline_variable

    out: PipelineVariableList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.pipeline_variable.deserialize_cbor(item))
    return out

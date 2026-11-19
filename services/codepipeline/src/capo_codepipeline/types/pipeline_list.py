"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_summary

PipelineList: TypeAlias = list[
    "capo_codepipeline.types.pipeline_summary.PipelineSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineList) -> list:
    import capo_codepipeline.types.pipeline_summary

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineList:
    import capo_codepipeline.types.pipeline_summary

    out: PipelineList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.pipeline_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineList) -> list:
    import capo_codepipeline.types.pipeline_summary

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.pipeline_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PipelineList:
    import capo_codepipeline.types.pipeline_summary

    out: PipelineList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.pipeline_summary.deserialize_cbor(item))
    return out

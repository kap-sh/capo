"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_summary

PipelineExecutionSummaryList: TypeAlias = list[
    "capo_codepipeline.types.pipeline_execution_summary.PipelineExecutionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionSummaryList) -> list:
    import capo_codepipeline.types.pipeline_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_execution_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineExecutionSummaryList:
    import capo_codepipeline.types.pipeline_execution_summary

    out: PipelineExecutionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.pipeline_execution_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineExecutionSummaryList) -> list:
    import capo_codepipeline.types.pipeline_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_execution_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PipelineExecutionSummaryList:
    import capo_codepipeline.types.pipeline_execution_summary

    out: PipelineExecutionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.pipeline_execution_summary.deserialize_cbor(item)
        )
    return out

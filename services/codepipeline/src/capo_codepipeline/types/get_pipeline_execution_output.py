"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution


class GetPipelineExecutionOutput(TypedDict, closed=True):
    pipeline_execution: NotRequired[
        "capo_codepipeline.types.pipeline_execution.PipelineExecution"
    ]
    """<p>Represents information about the execution of a pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineExecutionOutput) -> dict:
    out: dict = {}
    if "pipeline_execution" in value:
        import capo_codepipeline.types.pipeline_execution

        out["pipelineExecution"] = (
            capo_codepipeline.types.pipeline_execution.serialize_aws_json_1_1(
                value["pipeline_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineExecutionOutput:
    out: GetPipelineExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecution") is not None:
        import capo_codepipeline.types.pipeline_execution

        out["pipeline_execution"] = (
            capo_codepipeline.types.pipeline_execution.deserialize_aws_json_1_1(
                data["pipelineExecution"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetPipelineExecutionOutput) -> dict:
    out: dict = {}
    if "pipeline_execution" in value:
        import capo_codepipeline.types.pipeline_execution

        out["pipelineExecution"] = (
            capo_codepipeline.types.pipeline_execution.serialize_cbor(
                value["pipeline_execution"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetPipelineExecutionOutput:
    out: GetPipelineExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecution") is not None:
        import capo_codepipeline.types.pipeline_execution

        out["pipeline_execution"] = (
            capo_codepipeline.types.pipeline_execution.deserialize_cbor(
                data["pipelineExecution"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.codepipeline#StartPipelineExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id


class StartPipelineExecutionOutput(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The unique system-generated ID of the pipeline execution that was started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPipelineExecutionOutput) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPipelineExecutionOutput:
    out: StartPipelineExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartPipelineExecutionOutput) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_cbor(data: dict) -> StartPipelineExecutionOutput:
    out: StartPipelineExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_name


class GetPipelineExecutionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline about which you want to get execution details.</p>"""
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution about which you want to get execution details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineExecutionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineExecutionInput:
    out: GetPipelineExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        out["pipeline_execution_id"] = ""
    return out

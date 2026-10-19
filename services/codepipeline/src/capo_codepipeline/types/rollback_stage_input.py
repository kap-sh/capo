"""Generated from Smithy shape ``com.amazonaws.codepipeline#RollbackStageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name


class RollbackStageInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which the stage will be rolled back. </p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage in the pipeline to be rolled back. </p>"""
    target_pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The pipeline execution ID for the stage to be rolled back to. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackStageInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["targetPipelineExecutionId"] = value["target_pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackStageInput:
    out: RollbackStageInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    else:
        out["stage_name"] = ""
    if data.get("targetPipelineExecutionId") is not None:
        out["target_pipeline_execution_id"] = data["targetPipelineExecutionId"]
    else:
        out["target_pipeline_execution_id"] = ""
    return out

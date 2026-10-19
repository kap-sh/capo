"""Generated from Smithy shape ``com.amazonaws.codepipeline#RollbackStageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id


class RollbackStageOutput(TypedDict, closed=True):
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The execution ID of the pipeline execution for the stage that has been rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackStageOutput) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackStageOutput:
    out: RollbackStageOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        out["pipeline_execution_id"] = ""
    return out

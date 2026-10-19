"""Generated from Smithy shape ``com.amazonaws.codepipeline#StopPipelineExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.boolean
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stop_pipeline_execution_reason


class StopPipelineExecutionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to stop.</p>"""
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution to be stopped in the current stage. Use the <code>GetPipelineState</code> action to retrieve the current pipelineExecutionId.</p>"""
    abandon: NotRequired["capo_codepipeline.types.boolean.Boolean"]
    """<p>Use this option to stop the pipeline execution by abandoning, rather than finishing, in-progress actions.</p> <note> <p>This option can lead to failed or out-of-sequence tasks.</p> </note>"""
    reason: NotRequired[
        "capo_codepipeline.types.stop_pipeline_execution_reason.StopPipelineExecutionReason"
    ]
    """<p>Use this option to enter comments, such as the reason the pipeline was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopPipelineExecutionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "abandon" in value:
        out["abandon"] = value["abandon"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopPipelineExecutionInput:
    out: StopPipelineExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("StopPipelineExecutionInput.pipeline_name required")
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError(
            "StopPipelineExecutionInput.pipeline_execution_id required"
        )
    if data.get("abandon") is not None:
        out["abandon"] = data["abandon"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out

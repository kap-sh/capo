"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.execution_type
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.stage_execution_status


class StageExecution(TypedDict, closed=True):
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution associated with the stage.</p>"""
    status: "capo_codepipeline.types.stage_execution_status.StageExecutionStatus"
    """<p>The status of the stage, or for a completed stage, the last status of the stage.</p> <note> <p>A status of cancelled means that the pipeline’s definition was updated before the stage execution could be completed.</p> </note>"""
    type: NotRequired["capo_codepipeline.types.execution_type.ExecutionType"]
    """<p>The type of pipeline execution for the stage, such as a rollback pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageExecution) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import capo_codepipeline.types.stage_execution_status

    out["status"] = (
        capo_codepipeline.types.stage_execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "type" in value:
        import capo_codepipeline.types.execution_type

        out["type"] = capo_codepipeline.types.execution_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StageExecution:
    out: StageExecution = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        out["pipeline_execution_id"] = ""
    if data.get("status") is not None:
        import capo_codepipeline.types.stage_execution_status

        out["status"] = (
            capo_codepipeline.types.stage_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_codepipeline.types.stage_execution_status.StageExecutionStatus", ""
        )
    if data.get("type") is not None:
        import capo_codepipeline.types.execution_type

        out["type"] = capo_codepipeline.types.execution_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out

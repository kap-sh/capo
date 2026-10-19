"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryStageExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.stage_retry_mode


class RetryStageExecutionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline that contains the failed stage.</p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the failed stage to be retried.</p>"""
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution in the failed stage to be retried. Use the <a>GetPipelineState</a> action to retrieve the current pipelineExecutionId of the failed stage</p>"""
    retry_mode: "capo_codepipeline.types.stage_retry_mode.StageRetryMode"
    """<p>The scope of the retry attempt.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryStageExecutionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import capo_codepipeline.types.stage_retry_mode

    out["retryMode"] = capo_codepipeline.types.stage_retry_mode.serialize_aws_json_1_1(
        value["retry_mode"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryStageExecutionInput:
    out: RetryStageExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    else:
        out["stage_name"] = ""
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        out["pipeline_execution_id"] = ""
    if data.get("retryMode") is not None:
        import capo_codepipeline.types.stage_retry_mode

        out["retry_mode"] = (
            capo_codepipeline.types.stage_retry_mode.deserialize_aws_json_1_1(
                data["retryMode"]
            )
        )
    else:
        import typing

        out["retry_mode"] = typing.cast(
            "capo_codepipeline.types.stage_retry_mode.StageRetryMode", ""
        )
    return out

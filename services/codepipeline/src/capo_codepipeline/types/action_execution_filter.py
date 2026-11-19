"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.latest_in_pipeline_execution_filter
    import capo_codepipeline.types.pipeline_execution_id


class ActionExecutionFilter(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The pipeline execution ID used to filter action execution history.</p>"""
    latest_in_pipeline_execution: NotRequired[
        "capo_codepipeline.types.latest_in_pipeline_execution_filter.LatestInPipelineExecutionFilter"
    ]
    """<p>The latest execution in the pipeline.</p> <note> <p>Filtering on the latest execution is available for executions run on or after February 08, 2024.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionFilter) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "latest_in_pipeline_execution" in value:
        import capo_codepipeline.types.latest_in_pipeline_execution_filter

        out["latestInPipelineExecution"] = (
            capo_codepipeline.types.latest_in_pipeline_execution_filter.serialize_aws_json_1_1(
                value["latest_in_pipeline_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecutionFilter:
    out: ActionExecutionFilter = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("latestInPipelineExecution") is not None:
        import capo_codepipeline.types.latest_in_pipeline_execution_filter

        out["latest_in_pipeline_execution"] = (
            capo_codepipeline.types.latest_in_pipeline_execution_filter.deserialize_aws_json_1_1(
                data["latestInPipelineExecution"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionExecutionFilter) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "latest_in_pipeline_execution" in value:
        import capo_codepipeline.types.latest_in_pipeline_execution_filter

        out["latestInPipelineExecution"] = (
            capo_codepipeline.types.latest_in_pipeline_execution_filter.serialize_cbor(
                value["latest_in_pipeline_execution"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ActionExecutionFilter:
    out: ActionExecutionFilter = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("latestInPipelineExecution") is not None:
        import capo_codepipeline.types.latest_in_pipeline_execution_filter

        out["latest_in_pipeline_execution"] = (
            capo_codepipeline.types.latest_in_pipeline_execution_filter.deserialize_cbor(
                data["latestInPipelineExecution"]
            )
        )
    return out

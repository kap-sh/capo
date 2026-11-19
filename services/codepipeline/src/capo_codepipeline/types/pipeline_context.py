"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_context
    import capo_codepipeline.types.pipeline_arn
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_context


class PipelineContext(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.</p>"""
    stage: NotRequired["capo_codepipeline.types.stage_context.StageContext"]
    """<p>The stage of the pipeline.</p>"""
    action: NotRequired["capo_codepipeline.types.action_context.ActionContext"]
    """<p>The context of an action to a job worker in the stage of a pipeline.</p>"""
    pipeline_arn: NotRequired["capo_codepipeline.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The execution ID of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineContext) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "stage" in value:
        import capo_codepipeline.types.stage_context

        out["stage"] = capo_codepipeline.types.stage_context.serialize_aws_json_1_1(
            value["stage"]
        )
    if "action" in value:
        import capo_codepipeline.types.action_context

        out["action"] = capo_codepipeline.types.action_context.serialize_aws_json_1_1(
            value["action"]
        )
    if "pipeline_arn" in value:
        out["pipelineArn"] = value["pipeline_arn"]
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineContext:
    out: PipelineContext = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    if data.get("stage") is not None:
        import capo_codepipeline.types.stage_context

        out["stage"] = capo_codepipeline.types.stage_context.deserialize_aws_json_1_1(
            data["stage"]
        )
    if data.get("action") is not None:
        import capo_codepipeline.types.action_context

        out["action"] = capo_codepipeline.types.action_context.deserialize_aws_json_1_1(
            data["action"]
        )
    if data.get("pipelineArn") is not None:
        out["pipeline_arn"] = data["pipelineArn"]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineContext) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "stage" in value:
        import capo_codepipeline.types.stage_context

        out["stage"] = capo_codepipeline.types.stage_context.serialize_cbor(
            value["stage"]
        )
    if "action" in value:
        import capo_codepipeline.types.action_context

        out["action"] = capo_codepipeline.types.action_context.serialize_cbor(
            value["action"]
        )
    if "pipeline_arn" in value:
        out["pipelineArn"] = value["pipeline_arn"]
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_cbor(data: dict) -> PipelineContext:
    out: PipelineContext = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    if data.get("stage") is not None:
        import capo_codepipeline.types.stage_context

        out["stage"] = capo_codepipeline.types.stage_context.deserialize_cbor(
            data["stage"]
        )
    if data.get("action") is not None:
        import capo_codepipeline.types.action_context

        out["action"] = capo_codepipeline.types.action_context.deserialize_cbor(
            data["action"]
        )
    if data.get("pipelineArn") is not None:
        out["pipeline_arn"] = data["pipelineArn"]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out

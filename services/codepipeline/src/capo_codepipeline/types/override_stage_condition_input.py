"""Generated from Smithy shape ``com.amazonaws.codepipeline#OverrideStageConditionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_type
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name


class OverrideStageConditionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline with the stage that will override the condition.</p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage for the override.</p>"""
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution for the override.</p>"""
    condition_type: "capo_codepipeline.types.condition_type.ConditionType"
    """<p>The type of condition to override for the stage, such as entry conditions, failure conditions, or success conditions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverrideStageConditionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import capo_codepipeline.types.condition_type

    out["conditionType"] = (
        capo_codepipeline.types.condition_type.serialize_aws_json_1_1(
            value["condition_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OverrideStageConditionInput:
    out: OverrideStageConditionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("conditionType") is not None:
        import capo_codepipeline.types.condition_type

        out["condition_type"] = (
            capo_codepipeline.types.condition_type.deserialize_aws_json_1_1(
                data["conditionType"]
            )
        )
    else:
        import typing

        out["condition_type"] = typing.cast(
            "capo_codepipeline.types.condition_type.ConditionType", ""
        )
    return out

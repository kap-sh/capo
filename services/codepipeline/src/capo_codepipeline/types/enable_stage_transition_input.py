"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnableStageTransitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.stage_transition_type


class EnableStageTransitionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.</p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).</p>"""
    transition_type: "capo_codepipeline.types.stage_transition_type.StageTransitionType"
    """<p>Specifies whether artifacts are allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already processed artifacts are allowed to transition to the next stage (outbound).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableStageTransitionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    import capo_codepipeline.types.stage_transition_type

    out["transitionType"] = (
        capo_codepipeline.types.stage_transition_type.serialize_aws_json_1_1(
            value["transition_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableStageTransitionInput:
    out: EnableStageTransitionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    else:
        out["stage_name"] = ""
    if data.get("transitionType") is not None:
        import capo_codepipeline.types.stage_transition_type

        out["transition_type"] = (
            capo_codepipeline.types.stage_transition_type.deserialize_aws_json_1_1(
                data["transitionType"]
            )
        )
    else:
        import typing

        out["transition_type"] = typing.cast(
            "capo_codepipeline.types.stage_transition_type.StageTransitionType", ""
        )
    return out

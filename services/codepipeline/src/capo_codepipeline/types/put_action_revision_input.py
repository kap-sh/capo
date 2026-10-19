"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutActionRevisionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.action_revision
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name


class PutActionRevisionInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline that starts processing the revision to the source.</p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage that contains the action that acts on the revision.</p>"""
    action_name: "capo_codepipeline.types.action_name.ActionName"
    """<p>The name of the action that processes the revision.</p>"""
    action_revision: "capo_codepipeline.types.action_revision.ActionRevision"
    """<p>Represents information about the version (or revision) of an action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutActionRevisionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["actionName"] = value["action_name"]
    import capo_codepipeline.types.action_revision

    out["actionRevision"] = (
        capo_codepipeline.types.action_revision.serialize_aws_json_1_1(
            value["action_revision"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutActionRevisionInput:
    out: PutActionRevisionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    else:
        out["stage_name"] = ""
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("actionRevision") is not None:
        import capo_codepipeline.types.action_revision

        out["action_revision"] = (
            capo_codepipeline.types.action_revision.deserialize_aws_json_1_1(
                data["actionRevision"]
            )
        )
    else:
        raise DeserializationError("PutActionRevisionInput.action_revision required")
    return out

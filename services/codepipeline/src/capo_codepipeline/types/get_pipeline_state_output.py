"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineStateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.stage_state_list
    import capo_codepipeline.types.timestamp


class GetPipelineStateOutput(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline for which you want to get the state.</p>"""
    pipeline_version: NotRequired[
        "capo_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version number of the pipeline.</p> <note> <p>A newly created pipeline is always assigned a version number of <code>1</code>.</p> </note>"""
    stage_states: NotRequired["capo_codepipeline.types.stage_state_list.StageStateList"]
    """<p>A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data.</p>"""
    created: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was created, in timestamp format.</p>"""
    updated: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was last updated, in timestamp format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineStateOutput) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_states" in value:
        import capo_codepipeline.types.stage_state_list

        out["stageStates"] = (
            capo_codepipeline.types.stage_state_list.serialize_aws_json_1_1(
                value["stage_states"]
            )
        )
    if "created" in value:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "updated" in value:
        import capo_codepipeline.types.timestamp

        out["updated"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["updated"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineStateOutput:
    out: GetPipelineStateOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    if data.get("stageStates") is not None:
        import capo_codepipeline.types.stage_state_list

        out["stage_states"] = (
            capo_codepipeline.types.stage_state_list.deserialize_aws_json_1_1(
                data["stageStates"]
            )
        )
    if data.get("created") is not None:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("updated") is not None:
        import capo_codepipeline.types.timestamp

        out["updated"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["updated"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetPipelineStateOutput) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_states" in value:
        import capo_codepipeline.types.stage_state_list

        out["stageStates"] = capo_codepipeline.types.stage_state_list.serialize_cbor(
            value["stage_states"]
        )
    if "created" in value:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["created"]
        )
    if "updated" in value:
        import capo_codepipeline.types.timestamp

        out["updated"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["updated"]
        )
    return out


def deserialize_cbor(data: dict) -> GetPipelineStateOutput:
    out: GetPipelineStateOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    if data.get("stageStates") is not None:
        import capo_codepipeline.types.stage_state_list

        out["stage_states"] = capo_codepipeline.types.stage_state_list.deserialize_cbor(
            data["stageStates"]
        )
    if data.get("created") is not None:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["created"]
        )
    if data.get("updated") is not None:
        import capo_codepipeline.types.timestamp

        out["updated"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["updated"]
        )
    return out

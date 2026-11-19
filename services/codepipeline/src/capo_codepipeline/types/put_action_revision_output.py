"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutActionRevisionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.boolean
    import capo_codepipeline.types.pipeline_execution_id


class PutActionRevisionOutput(TypedDict, closed=True):
    new_revision: "capo_codepipeline.types.boolean.Boolean"
    """<p>Indicates whether the artifact revision was previously used in an execution of the specified pipeline.</p>"""
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the current workflow state of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutActionRevisionOutput) -> dict:
    out: dict = {}
    out["newRevision"] = value.get("new_revision", False)
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutActionRevisionOutput:
    out: PutActionRevisionOutput = {}  # type: ignore[typeddict-item]
    if data.get("newRevision") is not None:
        out["new_revision"] = data["newRevision"]
    else:
        out["new_revision"] = False
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutActionRevisionOutput) -> dict:
    out: dict = {}
    out["newRevision"] = value.get("new_revision", False)
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_cbor(data: dict) -> PutActionRevisionOutput:
    out: PutActionRevisionOutput = {}  # type: ignore[typeddict-item]
    if data.get("newRevision") is not None:
        out["new_revision"] = data["newRevision"]
    else:
        out["new_revision"] = False
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out

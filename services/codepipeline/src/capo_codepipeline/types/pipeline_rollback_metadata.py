"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineRollbackMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id


class PipelineRollbackMetadata(TypedDict, closed=True):
    rollback_target_pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The pipeline execution ID to which the stage will be rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineRollbackMetadata) -> dict:
    out: dict = {}
    if "rollback_target_pipeline_execution_id" in value:
        out["rollbackTargetPipelineExecutionId"] = value[
            "rollback_target_pipeline_execution_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineRollbackMetadata:
    out: PipelineRollbackMetadata = {}  # type: ignore[typeddict-item]
    if data.get("rollbackTargetPipelineExecutionId") is not None:
        out["rollback_target_pipeline_execution_id"] = data[
            "rollbackTargetPipelineExecutionId"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineRollbackMetadata) -> dict:
    out: dict = {}
    if "rollback_target_pipeline_execution_id" in value:
        out["rollbackTargetPipelineExecutionId"] = value[
            "rollback_target_pipeline_execution_id"
        ]
    return out


def deserialize_cbor(data: dict) -> PipelineRollbackMetadata:
    out: PipelineRollbackMetadata = {}  # type: ignore[typeddict-item]
    if data.get("rollbackTargetPipelineExecutionId") is not None:
        out["rollback_target_pipeline_execution_id"] = data[
            "rollbackTargetPipelineExecutionId"
        ]
    return out

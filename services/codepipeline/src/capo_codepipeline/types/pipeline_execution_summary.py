"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.execution_mode
    import capo_codepipeline.types.execution_trigger
    import capo_codepipeline.types.execution_type
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_execution_status
    import capo_codepipeline.types.pipeline_execution_status_summary
    import capo_codepipeline.types.pipeline_rollback_metadata
    import capo_codepipeline.types.source_revision_list
    import capo_codepipeline.types.stop_execution_trigger
    import capo_codepipeline.types.timestamp


class PipelineExecutionSummary(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the pipeline execution.</p>"""
    status: NotRequired[
        "capo_codepipeline.types.pipeline_execution_status.PipelineExecutionStatus"
    ]
    """<p>The status of the pipeline execution.</p> <ul> <li> <p>InProgress: The pipeline execution is currently running.</p> </li> <li> <p>Stopped: The pipeline execution was manually stopped. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped">Stopped Executions</a>.</p> </li> <li> <p>Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped">Stopped Executions</a>.</p> </li> <li> <p>Succeeded: The pipeline execution was completed successfully. </p> </li> <li> <p>Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-superseded">Superseded Executions</a>.</p> </li> <li> <p>Failed: The pipeline execution was not completed successfully.</p> </li> </ul>"""
    status_summary: NotRequired[
        "capo_codepipeline.types.pipeline_execution_status_summary.PipelineExecutionStatusSummary"
    ]
    """<p>Status summary for the pipeline.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time when the pipeline execution began, in timestamp format.</p>"""
    last_update_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time of the last change to the pipeline execution, in timestamp format.</p>"""
    source_revisions: NotRequired[
        "capo_codepipeline.types.source_revision_list.SourceRevisionList"
    ]
    """<p>A list of the source artifact revisions that initiated a pipeline execution.</p>"""
    trigger: NotRequired["capo_codepipeline.types.execution_trigger.ExecutionTrigger"]
    """<p>The interaction or event that started a pipeline execution, such as automated change detection or a <code>StartPipelineExecution</code> API call.</p>"""
    stop_trigger: NotRequired[
        "capo_codepipeline.types.stop_execution_trigger.StopExecutionTrigger"
    ]
    """<p>The interaction that stopped a pipeline execution.</p>"""
    execution_mode: NotRequired["capo_codepipeline.types.execution_mode.ExecutionMode"]
    """<p>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</p>"""
    execution_type: NotRequired["capo_codepipeline.types.execution_type.ExecutionType"]
    """<p>Type of the pipeline execution.</p>"""
    rollback_metadata: NotRequired[
        "capo_codepipeline.types.pipeline_rollback_metadata.PipelineRollbackMetadata"
    ]
    """<p>The metadata for the stage execution to be rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionSummary) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "status" in value:
        import capo_codepipeline.types.pipeline_execution_status

        out["status"] = (
            capo_codepipeline.types.pipeline_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_summary" in value:
        out["statusSummary"] = value["status_summary"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "last_update_time" in value:
        import capo_codepipeline.types.timestamp

        out["lastUpdateTime"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "source_revisions" in value:
        import capo_codepipeline.types.source_revision_list

        out["sourceRevisions"] = (
            capo_codepipeline.types.source_revision_list.serialize_aws_json_1_1(
                value["source_revisions"]
            )
        )
    if "trigger" in value:
        import capo_codepipeline.types.execution_trigger

        out["trigger"] = (
            capo_codepipeline.types.execution_trigger.serialize_aws_json_1_1(
                value["trigger"]
            )
        )
    if "stop_trigger" in value:
        import capo_codepipeline.types.stop_execution_trigger

        out["stopTrigger"] = (
            capo_codepipeline.types.stop_execution_trigger.serialize_aws_json_1_1(
                value["stop_trigger"]
            )
        )
    if "execution_mode" in value:
        import capo_codepipeline.types.execution_mode

        out["executionMode"] = (
            capo_codepipeline.types.execution_mode.serialize_aws_json_1_1(
                value["execution_mode"]
            )
        )
    if "execution_type" in value:
        import capo_codepipeline.types.execution_type

        out["executionType"] = (
            capo_codepipeline.types.execution_type.serialize_aws_json_1_1(
                value["execution_type"]
            )
        )
    if "rollback_metadata" in value:
        import capo_codepipeline.types.pipeline_rollback_metadata

        out["rollbackMetadata"] = (
            capo_codepipeline.types.pipeline_rollback_metadata.serialize_aws_json_1_1(
                value["rollback_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionSummary:
    out: PipelineExecutionSummary = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("status") is not None:
        import capo_codepipeline.types.pipeline_execution_status

        out["status"] = (
            capo_codepipeline.types.pipeline_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("statusSummary") is not None:
        out["status_summary"] = data["statusSummary"]
    if data.get("startTime") is not None:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("lastUpdateTime") is not None:
        import capo_codepipeline.types.timestamp

        out["last_update_time"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdateTime"]
            )
        )
    if data.get("sourceRevisions") is not None:
        import capo_codepipeline.types.source_revision_list

        out["source_revisions"] = (
            capo_codepipeline.types.source_revision_list.deserialize_aws_json_1_1(
                data["sourceRevisions"]
            )
        )
    if data.get("trigger") is not None:
        import capo_codepipeline.types.execution_trigger

        out["trigger"] = (
            capo_codepipeline.types.execution_trigger.deserialize_aws_json_1_1(
                data["trigger"]
            )
        )
    if data.get("stopTrigger") is not None:
        import capo_codepipeline.types.stop_execution_trigger

        out["stop_trigger"] = (
            capo_codepipeline.types.stop_execution_trigger.deserialize_aws_json_1_1(
                data["stopTrigger"]
            )
        )
    if data.get("executionMode") is not None:
        import capo_codepipeline.types.execution_mode

        out["execution_mode"] = (
            capo_codepipeline.types.execution_mode.deserialize_aws_json_1_1(
                data["executionMode"]
            )
        )
    if data.get("executionType") is not None:
        import capo_codepipeline.types.execution_type

        out["execution_type"] = (
            capo_codepipeline.types.execution_type.deserialize_aws_json_1_1(
                data["executionType"]
            )
        )
    if data.get("rollbackMetadata") is not None:
        import capo_codepipeline.types.pipeline_rollback_metadata

        out["rollback_metadata"] = (
            capo_codepipeline.types.pipeline_rollback_metadata.deserialize_aws_json_1_1(
                data["rollbackMetadata"]
            )
        )
    return out

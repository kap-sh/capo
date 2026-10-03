"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_revision_list
    import capo_codepipeline.types.execution_mode
    import capo_codepipeline.types.execution_trigger
    import capo_codepipeline.types.execution_type
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_execution_status
    import capo_codepipeline.types.pipeline_execution_status_summary
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.pipeline_rollback_metadata
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.resolved_pipeline_variable_list


class PipelineExecution(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline with the specified pipeline execution.</p>"""
    pipeline_version: NotRequired[
        "capo_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version number of the pipeline with the specified pipeline execution.</p>"""
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the pipeline execution.</p>"""
    status: NotRequired[
        "capo_codepipeline.types.pipeline_execution_status.PipelineExecutionStatus"
    ]
    """<p>The status of the pipeline execution.</p> <ul> <li> <p>Cancelled: The pipeline’s definition was updated before the pipeline execution could be completed.</p> </li> <li> <p>InProgress: The pipeline execution is currently running.</p> </li> <li> <p>Stopped: The pipeline execution was manually stopped. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped">Stopped Executions</a>.</p> </li> <li> <p>Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped">Stopped Executions</a>.</p> </li> <li> <p>Succeeded: The pipeline execution was completed successfully. </p> </li> <li> <p>Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-superseded">Superseded Executions</a>.</p> </li> <li> <p>Failed: The pipeline execution was not completed successfully.</p> </li> </ul>"""
    status_summary: NotRequired[
        "capo_codepipeline.types.pipeline_execution_status_summary.PipelineExecutionStatusSummary"
    ]
    """<p>A summary that contains a description of the pipeline execution status.</p>"""
    artifact_revisions: NotRequired[
        "capo_codepipeline.types.artifact_revision_list.ArtifactRevisionList"
    ]
    """<p>A list of <code>ArtifactRevision</code> objects included in a pipeline execution.</p>"""
    variables: NotRequired[
        "capo_codepipeline.types.resolved_pipeline_variable_list.ResolvedPipelineVariableList"
    ]
    """<p>A list of pipeline variables used for the pipeline execution.</p>"""
    trigger: NotRequired["capo_codepipeline.types.execution_trigger.ExecutionTrigger"]
    execution_mode: NotRequired["capo_codepipeline.types.execution_mode.ExecutionMode"]
    """<p>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</p>"""
    execution_type: NotRequired["capo_codepipeline.types.execution_type.ExecutionType"]
    """<p>The type of the pipeline execution.</p>"""
    rollback_metadata: NotRequired[
        "capo_codepipeline.types.pipeline_rollback_metadata.PipelineRollbackMetadata"
    ]
    """<p>The metadata about the execution pertaining to stage rollback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecution) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
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
    if "artifact_revisions" in value:
        import capo_codepipeline.types.artifact_revision_list

        out["artifactRevisions"] = (
            capo_codepipeline.types.artifact_revision_list.serialize_aws_json_1_1(
                value["artifact_revisions"]
            )
        )
    if "variables" in value:
        import capo_codepipeline.types.resolved_pipeline_variable_list

        out["variables"] = (
            capo_codepipeline.types.resolved_pipeline_variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "trigger" in value:
        import capo_codepipeline.types.execution_trigger

        out["trigger"] = (
            capo_codepipeline.types.execution_trigger.serialize_aws_json_1_1(
                value["trigger"]
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


def deserialize_aws_json_1_1(data: dict) -> PipelineExecution:
    out: PipelineExecution = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
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
    if data.get("artifactRevisions") is not None:
        import capo_codepipeline.types.artifact_revision_list

        out["artifact_revisions"] = (
            capo_codepipeline.types.artifact_revision_list.deserialize_aws_json_1_1(
                data["artifactRevisions"]
            )
        )
    if data.get("variables") is not None:
        import capo_codepipeline.types.resolved_pipeline_variable_list

        out["variables"] = (
            capo_codepipeline.types.resolved_pipeline_variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if data.get("trigger") is not None:
        import capo_codepipeline.types.execution_trigger

        out["trigger"] = (
            capo_codepipeline.types.execution_trigger.deserialize_aws_json_1_1(
                data["trigger"]
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

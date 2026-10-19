"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetTaskInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.generic_map
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.task_instance_status
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn


class GetTaskInstanceResponse(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this task instance.</p>"""
    run_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run that contains this task instance.</p>"""
    task_instance_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of this task instance.</p>"""
    workflow_version: NotRequired["capo_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow that contains this task instance.</p>"""
    status: NotRequired[
        "capo_mwaa_serverless.types.task_instance_status.TaskInstanceStatus"
    ]
    """<p>The current status of the task instance.</p>"""
    duration_in_seconds: NotRequired["int"]
    """<p>The duration of the task instance execution in seconds. This value is null if the task is not complete.</p>"""
    operator_name: NotRequired[
        "capo_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The name of the Apache Airflow operator used for this task instance.</p>"""
    modified_at: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the task instance was last modified, in ISO 8601 date-time format.</p>"""
    ended_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the task instance completed execution, in ISO 8601 date-time format. This value is null if the task is not complete.</p>"""
    started_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the task instance started execution, in ISO 8601 date-time format. This value is null if the task has not started.</p>"""
    attempt_number: NotRequired["int"]
    """<p>The attempt number for this task instance.</p>"""
    error_message: NotRequired[
        "capo_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The error message if the task instance failed. This value is null if the task completed successfully.</p>"""
    task_id: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the task definition within the workflow.</p>"""
    log_stream: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The CloudWatch log stream name for this task instance execution.</p>"""
    xcom: NotRequired["capo_mwaa_serverless.types.generic_map.GenericMap"]
    """<p>Cross-communication data exchanged between tasks in the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTaskInstanceResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    out["RunId"] = value["run_id"]
    out["TaskInstanceId"] = value["task_instance_id"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "status" in value:
        import capo_mwaa_serverless.types.task_instance_status

        out["Status"] = (
            capo_mwaa_serverless.types.task_instance_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    if "operator_name" in value:
        out["OperatorName"] = value["operator_name"]
    if "modified_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["ModifiedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "ended_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["EndedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["ended_at"]
            )
        )
    if "started_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["StartedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["started_at"]
            )
        )
    if "attempt_number" in value:
        out["AttemptNumber"] = value["attempt_number"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "log_stream" in value:
        out["LogStream"] = value["log_stream"]
    if "xcom" in value:
        import capo_mwaa_serverless.types.generic_map

        out["Xcom"] = capo_mwaa_serverless.types.generic_map.serialize_aws_json_1_0(
            value["xcom"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTaskInstanceResponse:
    out: GetTaskInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    if data.get("TaskInstanceId") is not None:
        out["task_instance_id"] = data["TaskInstanceId"]
    else:
        out["task_instance_id"] = ""
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    if data.get("Status") is not None:
        import capo_mwaa_serverless.types.task_instance_status

        out["status"] = (
            capo_mwaa_serverless.types.task_instance_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    if data.get("OperatorName") is not None:
        out["operator_name"] = data["OperatorName"]
    if data.get("ModifiedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["modified_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if data.get("EndedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["ended_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["EndedAt"]
            )
        )
    if data.get("StartedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["started_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    if data.get("AttemptNumber") is not None:
        out["attempt_number"] = data["AttemptNumber"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("LogStream") is not None:
        out["log_stream"] = data["LogStream"]
    if data.get("Xcom") is not None:
        import capo_mwaa_serverless.types.generic_map

        out["xcom"] = capo_mwaa_serverless.types.generic_map.deserialize_aws_json_1_0(
            data["Xcom"]
        )
    return out

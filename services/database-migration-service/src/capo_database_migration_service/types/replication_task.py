"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.replication_task_stats
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class ReplicationTask(TypedDict, closed=True):
    replication_task_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The user-assigned replication task identifier or name.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    source_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the endpoint.</p>"""
    target_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN that uniquely identifies the endpoint.</p>"""
    replication_instance_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the replication instance.</p>"""
    migration_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The type of migration.</p>"""
    table_mappings: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Table mappings specified in the task.</p>"""
    replication_task_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The settings for the replication task.</p>"""
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The status of the replication task. This response parameter can return one of the following values:</p> <ul> <li> <p> <code>"moving"</code> – The task is being moved in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html"> <code>MoveReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"creating"</code> – The task is being created in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html"> <code>CreateReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"deleting"</code> – The task is being deleted in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask.html"> <code>DeleteReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"failed"</code> – The task failed to successfully complete the database migration in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html"> <code>StartReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"failed-move"</code> – The task failed to move in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html"> <code>MoveReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"modifying"</code> – The task definition is being modified in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html"> <code>ModifyReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"ready"</code> – The task is in a <code>ready</code> state where it can respond to other task operations, such as <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html"> <code>StartReplicationTask</code> </a> or <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask.html"> <code>DeleteReplicationTask</code> </a>. </p> </li> <li> <p> <code>"running"</code> – The task is performing a database migration in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html"> <code>StartReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"starting"</code> – The task is preparing to perform a database migration in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html"> <code>StartReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"stopped"</code> – The task has stopped in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask.html"> <code>StopReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"stopping"</code> – The task is preparing to stop in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask.html"> <code>StopReplicationTask</code> </a> operation.</p> </li> <li> <p> <code>"testing"</code> – The database migration specified for this task is being tested in response to running either the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html"> <code>StartReplicationTaskAssessmentRun</code> </a> or the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html"> <code>StartReplicationTaskAssessment</code> </a> operation.</p> <note> <p> <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html"> <code>StartReplicationTaskAssessmentRun</code> </a> is an improved premigration task assessment operation. The <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html"> <code>StartReplicationTaskAssessment</code> </a> operation assesses data type compatibility only between the source and target database of a given migration task. In contrast, <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html"> <code>StartReplicationTaskAssessmentRun</code> </a> enables you to specify a variety of premigration task assessments in addition to data type compatibility. These assessments include ones for the validity of primary key definitions and likely issues with database migration performance, among others.</p> </note> </li> </ul>"""
    last_failure_message: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The last error (failure) message generated for the replication task.</p>"""
    stop_reason: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The reason the replication task was stopped. This response parameter can return one of the following values:</p> <ul> <li> <p> <code>"Stop Reason NORMAL"</code> – The task completed successfully with no additional information returned.</p> </li> <li> <p> <code>"Stop Reason RECOVERABLE_ERROR"</code> </p> </li> <li> <p> <code>"Stop Reason FATAL_ERROR"</code> </p> </li> <li> <p> <code>"Stop Reason FULL_LOAD_ONLY_FINISHED"</code> – The task completed the full load phase. DMS applied cached changes if you set <code>StopTaskCachedChangesApplied</code> to <code>true</code>.</p> </li> <li> <p> <code>"Stop Reason STOPPED_AFTER_FULL_LOAD"</code> – Full load completed, with cached changes not applied</p> </li> <li> <p> <code>"Stop Reason STOPPED_AFTER_CACHED_EVENTS"</code> – Full load completed, with cached changes applied</p> </li> <li> <p> <code>"Stop Reason EXPRESS_LICENSE_LIMITS_REACHED"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_AFTER_DDL_APPLY"</code> – User-defined stop task after DDL applied</p> </li> <li> <p> <code>"Stop Reason STOPPED_DUE_TO_LOW_MEMORY"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_DUE_TO_LOW_DISK"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_AT_SERVER_TIME"</code> – User-defined server time for stopping task</p> </li> <li> <p> <code>"Stop Reason STOPPED_AT_COMMIT_TIME"</code> – User-defined commit time for stopping task</p> </li> <li> <p> <code>"Stop Reason RECONFIGURATION_RESTART"</code> </p> </li> <li> <p> <code>"Stop Reason RECYCLE_TASK"</code> </p> </li> </ul>"""
    replication_task_creation_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task was created.</p>"""
    replication_task_start_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task is scheduled to start.</p>"""
    cdc_start_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to start. Use either <code>CdcStartPosition</code> or <code>CdcStartTime</code> to specify when you want the CDC operation to start. Specifying both values results in an error.</p> <p>The value can be in date, checkpoint, or LSN/SCN format.</p> <p>Date Example: --cdc-start-position “2018-03-08T12:12:12”</p> <p>Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"</p> <p>LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”</p>"""
    cdc_stop_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p> <p>Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”</p> <p>Commit time example: --cdc-stop-position “commit_time:2018-02-09T12:12:12“</p>"""
    recovery_checkpoint: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the <code>CdcStartPosition</code> parameter to start a CDC operation that begins at that checkpoint.</p>"""
    replication_task_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication task.</p>"""
    replication_task_stats: NotRequired[
        "capo_database_migration_service.types.replication_task_stats.ReplicationTaskStats"
    ]
    """<p>The statistics for the task, including elapsed time, tables loaded, and table errors.</p>"""
    task_data: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html">Specifying Supplemental Data for Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    target_replication_instance_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the replication instance to which this task is moved in response to running the <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html"> <code>MoveReplicationTask</code> </a> operation. Otherwise, this response parameter isn't a member of the <code>ReplicationTask</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTask) -> dict:
    out: dict = {}
    if "replication_task_identifier" in value:
        out["ReplicationTaskIdentifier"] = value["replication_task_identifier"]
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "migration_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["MigrationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["migration_type"]
            )
        )
    if "table_mappings" in value:
        out["TableMappings"] = value["table_mappings"]
    if "replication_task_settings" in value:
        out["ReplicationTaskSettings"] = value["replication_task_settings"]
    if "status" in value:
        out["Status"] = value["status"]
    if "last_failure_message" in value:
        out["LastFailureMessage"] = value["last_failure_message"]
    if "stop_reason" in value:
        out["StopReason"] = value["stop_reason"]
    if "replication_task_creation_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationTaskCreationDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_task_creation_date"]
            )
        )
    if "replication_task_start_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationTaskStartDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_task_start_date"]
            )
        )
    if "cdc_start_position" in value:
        out["CdcStartPosition"] = value["cdc_start_position"]
    if "cdc_stop_position" in value:
        out["CdcStopPosition"] = value["cdc_stop_position"]
    if "recovery_checkpoint" in value:
        out["RecoveryCheckpoint"] = value["recovery_checkpoint"]
    if "replication_task_arn" in value:
        out["ReplicationTaskArn"] = value["replication_task_arn"]
    if "replication_task_stats" in value:
        import capo_database_migration_service.types.replication_task_stats

        out["ReplicationTaskStats"] = (
            capo_database_migration_service.types.replication_task_stats.serialize_aws_json_1_1(
                value["replication_task_stats"]
            )
        )
    if "task_data" in value:
        out["TaskData"] = value["task_data"]
    if "target_replication_instance_arn" in value:
        out["TargetReplicationInstanceArn"] = value["target_replication_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTask:
    out: ReplicationTask = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskIdentifier") is not None:
        out["replication_task_identifier"] = data["ReplicationTaskIdentifier"]
    if data.get("SourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if data.get("TargetEndpointArn") is not None:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if data.get("MigrationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["migration_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["MigrationType"]
            )
        )
    if data.get("TableMappings") is not None:
        out["table_mappings"] = data["TableMappings"]
    if data.get("ReplicationTaskSettings") is not None:
        out["replication_task_settings"] = data["ReplicationTaskSettings"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("LastFailureMessage") is not None:
        out["last_failure_message"] = data["LastFailureMessage"]
    if data.get("StopReason") is not None:
        out["stop_reason"] = data["StopReason"]
    if data.get("ReplicationTaskCreationDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["replication_task_creation_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationTaskCreationDate"]
            )
        )
    if data.get("ReplicationTaskStartDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["replication_task_start_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationTaskStartDate"]
            )
        )
    if data.get("CdcStartPosition") is not None:
        out["cdc_start_position"] = data["CdcStartPosition"]
    if data.get("CdcStopPosition") is not None:
        out["cdc_stop_position"] = data["CdcStopPosition"]
    if data.get("RecoveryCheckpoint") is not None:
        out["recovery_checkpoint"] = data["RecoveryCheckpoint"]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    if data.get("ReplicationTaskStats") is not None:
        import capo_database_migration_service.types.replication_task_stats

        out["replication_task_stats"] = (
            capo_database_migration_service.types.replication_task_stats.deserialize_aws_json_1_1(
                data["ReplicationTaskStats"]
            )
        )
    if data.get("TaskData") is not None:
        out["task_data"] = data["TaskData"]
    if data.get("TargetReplicationInstanceArn") is not None:
        out["target_replication_instance_arn"] = data["TargetReplicationInstanceArn"]
    return out

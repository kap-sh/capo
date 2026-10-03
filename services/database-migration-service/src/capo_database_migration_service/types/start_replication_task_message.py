"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.start_replication_task_type_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class StartReplicationTaskMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication task to be started.</p>"""
    start_replication_task_type: "capo_database_migration_service.types.start_replication_task_type_value.StartReplicationTaskTypeValue"
    """<p>The type of replication task to start.</p> <p> <code>start-replication</code> is the only valid action that can be used for the first time a task with the migration type of <code>full-load</code>full-load, <code>full-load-and-cdc</code> or <code>cdc</code> is run. Any other action used for the first time on a given task, such as <code>resume-processing</code> and reload-target will result in data errors.</p> <p>You can also use <a>ReloadTables</a> to reload specific tables that failed during migration instead of restarting the task.</p> <p>For a <code>full-load</code> task, the resume-processing option will reload any tables that were partially loaded or not yet loaded during the full load phase.</p> <p>For a <code>full-load-and-cdc</code> task, DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use <code>reload-target</code>. Otherwise use <code>resume-processing</code>, to replicate the changes from the last stop position.</p> <p>For a <code>cdc</code> only task, to start from a specific position, you must use start-replication and also specify the start position. Check the source endpoint DMS documentation for any limitations. For example, not all sources support starting from a time.</p> <note> <p> <code>resume-processing</code> is only available for previously executed tasks.</p> </note>"""
    cdc_start_time: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p>Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p>Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”</p>"""
    cdc_start_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p> The value can be in date, checkpoint, or LSN/SCN format.</p> <p>Date Example: --cdc-start-position “2018-03-08T12:12:12”</p> <p>Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"</p> <p>LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”</p> <note> <p>When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the <code>slotName</code> extra connection attribute to the name of this logical replication slot. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra Connection Attributes When Using PostgreSQL as a Source for DMS</a>.</p> </note>"""
    cdc_stop_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p> <p>Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”</p> <p>Commit time example: --cdc-stop-position “commit_time:2018-02-09T12:12:12“</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    import capo_database_migration_service.types.start_replication_task_type_value

    out["StartReplicationTaskType"] = (
        capo_database_migration_service.types.start_replication_task_type_value.serialize_aws_json_1_1(
            value["start_replication_task_type"]
        )
    )
    if "cdc_start_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["CdcStartTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["cdc_start_time"]
            )
        )
    if "cdc_start_position" in value:
        out["CdcStartPosition"] = value["cdc_start_position"]
    if "cdc_stop_position" in value:
        out["CdcStopPosition"] = value["cdc_stop_position"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationTaskMessage:
    out: StartReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        raise DeserializationError(
            "StartReplicationTaskMessage.replication_task_arn required"
        )
    if data.get("StartReplicationTaskType") is not None:
        import capo_database_migration_service.types.start_replication_task_type_value

        out["start_replication_task_type"] = (
            capo_database_migration_service.types.start_replication_task_type_value.deserialize_aws_json_1_1(
                data["StartReplicationTaskType"]
            )
        )
    else:
        raise DeserializationError(
            "StartReplicationTaskMessage.start_replication_task_type required"
        )
    if data.get("CdcStartTime") is not None:
        import capo_database_migration_service.types.t_stamp

        out["cdc_start_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["CdcStartTime"]
            )
        )
    if data.get("CdcStartPosition") is not None:
        out["cdc_start_position"] = data["CdcStartPosition"]
    if data.get("CdcStopPosition") is not None:
        out["cdc_stop_position"] = data["CdcStopPosition"]
    return out

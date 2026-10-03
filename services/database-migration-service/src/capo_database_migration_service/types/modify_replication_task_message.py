"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationTaskMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class ModifyReplicationTaskMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication task.</p>"""
    replication_task_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The replication task identifier.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    migration_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The migration type. Valid values: <code>full-load</code> | <code>cdc</code> | <code>full-load-and-cdc</code> </p>"""
    table_mappings: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>When using the CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with <code>file://</code>. For example, <code>--table-mappings file://mappingfile.json</code>. When working with the DMS API, provide the JSON as the parameter value. </p>"""
    replication_task_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>JSON file that contains settings for the task, such as task metadata settings.</p>"""
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
    task_data: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html">Specifying Supplemental Data for Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    if "replication_task_identifier" in value:
        out["ReplicationTaskIdentifier"] = value["replication_task_identifier"]
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
    if "task_data" in value:
        out["TaskData"] = value["task_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationTaskMessage:
    out: ModifyReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        raise DeserializationError(
            "ModifyReplicationTaskMessage.replication_task_arn required"
        )
    if data.get("ReplicationTaskIdentifier") is not None:
        out["replication_task_identifier"] = data["ReplicationTaskIdentifier"]
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
    if data.get("TaskData") is not None:
        out["task_data"] = data["TaskData"]
    return out

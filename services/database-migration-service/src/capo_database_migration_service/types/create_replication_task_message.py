"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationTaskMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp
    import capo_database_migration_service.types.tag_list


class CreateReplicationTaskMessage(TypedDict, closed=True):
    replication_task_identifier: "capo_database_migration_service.types.string.String"
    """<p>An identifier for the replication task.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    source_endpoint_arn: "capo_database_migration_service.types.string.String"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.</p>"""
    target_endpoint_arn: "capo_database_migration_service.types.string.String"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.</p>"""
    replication_instance_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of a replication instance.</p>"""
    migration_type: (
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    )
    """<p>The migration type. Valid values: <code>full-load</code> | <code>cdc</code> | <code>full-load-and-cdc</code> </p>"""
    table_mappings: "capo_database_migration_service.types.string.String"
    """<p>The table mappings for the task, in JSON format. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">Using Table Mapping to Specify Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    replication_task_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Overall settings for the task, in JSON format. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">Specifying Task Settings for Database Migration Service Tasks</a> in the <i>Database Migration Service User Guide.</i> </p>"""
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
    tags: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the replication task.</p>"""
    task_data: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html">Specifying Supplemental Data for Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    resource_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A friendly name for the resource identifier at the end of the <code>EndpointArn</code> response parameter that is returned in the created <code>Endpoint</code> object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as <code>Example-App-ARN1</code>. For example, this value might result in the <code>EndpointArn</code> value <code>arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1</code>. If you don't specify a <code>ResourceIdentifier</code> value, DMS generates a default identifier value for the end of <code>EndpointArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskIdentifier"] = value["replication_task_identifier"]
    out["SourceEndpointArn"] = value["source_endpoint_arn"]
    out["TargetEndpointArn"] = value["target_endpoint_arn"]
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    import capo_database_migration_service.types.migration_type_value

    out["MigrationType"] = (
        capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
            value["migration_type"]
        )
    )
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
    if "tags" in value:
        import capo_database_migration_service.types.tag_list

        out["Tags"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "task_data" in value:
        out["TaskData"] = value["task_data"]
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationTaskMessage:
    out: CreateReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskIdentifier") is not None:
        out["replication_task_identifier"] = data["ReplicationTaskIdentifier"]
    else:
        raise DeserializationError(
            "CreateReplicationTaskMessage.replication_task_identifier required"
        )
    if data.get("SourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    else:
        raise DeserializationError(
            "CreateReplicationTaskMessage.source_endpoint_arn required"
        )
    if data.get("TargetEndpointArn") is not None:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    else:
        raise DeserializationError(
            "CreateReplicationTaskMessage.target_endpoint_arn required"
        )
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "CreateReplicationTaskMessage.replication_instance_arn required"
        )
    if data.get("MigrationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["migration_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["MigrationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReplicationTaskMessage.migration_type required"
        )
    if data.get("TableMappings") is not None:
        out["table_mappings"] = data["TableMappings"]
    else:
        raise DeserializationError(
            "CreateReplicationTaskMessage.table_mappings required"
        )
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
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if data.get("TaskData") is not None:
        out["task_data"] = data["TaskData"]
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    return out

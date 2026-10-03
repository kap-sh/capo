"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Replication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.premigration_assessment_status_list
    import capo_database_migration_service.types.provision_data
    import capo_database_migration_service.types.replication_stats
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.string_list
    import capo_database_migration_service.types.t_stamp


class Replication(TypedDict, closed=True):
    replication_config_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier for the <code>ReplicationConfig</code> associated with the replication.</p>"""
    replication_config_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name for the <code>ReplicationConfig</code> associated with the replication.</p>"""
    source_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name for an existing <code>Endpoint</code> the serverless replication uses for its data source.</p>"""
    target_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name for an existing <code>Endpoint</code> the serverless replication uses for its data target.</p>"""
    replication_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The type of the serverless replication.</p>"""
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The current status of the serverless replication.</p>"""
    provision_data: NotRequired[
        "capo_database_migration_service.types.provision_data.ProvisionData"
    ]
    """<p>Information about provisioning resources for an DMS serverless replication.</p>"""
    premigration_assessment_statuses: NotRequired[
        "capo_database_migration_service.types.premigration_assessment_status_list.PremigrationAssessmentStatusList"
    ]
    """<p>The status output of premigration assessment in describe-replications.</p>"""
    stop_reason: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The reason the replication task was stopped. This response parameter can return one of the following values:</p> <ul> <li> <p> <code>"Stop Reason NORMAL"</code> </p> </li> <li> <p> <code>"Stop Reason RECOVERABLE_ERROR"</code> </p> </li> <li> <p> <code>"Stop Reason FATAL_ERROR"</code> </p> </li> <li> <p> <code>"Stop Reason FULL_LOAD_ONLY_FINISHED"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_AFTER_FULL_LOAD"</code> – Full load completed, with cached changes not applied</p> </li> <li> <p> <code>"Stop Reason STOPPED_AFTER_CACHED_EVENTS"</code> – Full load completed, with cached changes applied</p> </li> <li> <p> <code>"Stop Reason EXPRESS_LICENSE_LIMITS_REACHED"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_AFTER_DDL_APPLY"</code> – User-defined stop task after DDL applied</p> </li> <li> <p> <code>"Stop Reason STOPPED_DUE_TO_LOW_MEMORY"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_DUE_TO_LOW_DISK"</code> </p> </li> <li> <p> <code>"Stop Reason STOPPED_AT_SERVER_TIME"</code> – User-defined server time for stopping task</p> </li> <li> <p> <code>"Stop Reason STOPPED_AT_COMMIT_TIME"</code> – User-defined commit time for stopping task</p> </li> <li> <p> <code>"Stop Reason RECONFIGURATION_RESTART"</code> </p> </li> <li> <p> <code>"Stop Reason RECYCLE_TASK"</code> </p> </li> </ul>"""
    failure_messages: NotRequired[
        "capo_database_migration_service.types.string_list.StringList"
    ]
    """<p>Error and other information about why a serverless replication failed.</p>"""
    replication_stats: NotRequired[
        "capo_database_migration_service.types.replication_stats.ReplicationStats"
    ]
    """<p>This object provides a collection of statistics about a serverless replication.</p>"""
    start_replication_type: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The type of replication to start.</p>"""
    cdc_start_time: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p>Indicates the start time for a change data capture (CDC) operation. Use either <code>CdcStartTime</code> or <code>CdcStartPosition</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p>"""
    cdc_start_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates the start time for a change data capture (CDC) operation. Use either <code>CdcStartTime</code> or <code>CdcStartPosition</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p>"""
    cdc_stop_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p>"""
    recovery_checkpoint: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the <code>CdcStartPosition</code> parameter to start a CDC operation that begins at that checkpoint.</p>"""
    replication_create_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the serverless replication was created.</p>"""
    replication_update_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the serverless replication was updated.</p>"""
    replication_last_stop_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The timestamp when replication was last stopped.</p>"""
    replication_deprovision_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The timestamp when DMS will deprovision the replication.</p>"""
    is_read_only: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the serverless replication is read-only. When set to <code>true</code>, this replication is managed by DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only replications through their associated zero-ETL integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Replication) -> dict:
    out: dict = {}
    if "replication_config_identifier" in value:
        out["ReplicationConfigIdentifier"] = value["replication_config_identifier"]
    if "replication_config_arn" in value:
        out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    if "replication_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["ReplicationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["replication_type"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "provision_data" in value:
        import capo_database_migration_service.types.provision_data

        out["ProvisionData"] = (
            capo_database_migration_service.types.provision_data.serialize_aws_json_1_1(
                value["provision_data"]
            )
        )
    if "premigration_assessment_statuses" in value:
        import capo_database_migration_service.types.premigration_assessment_status_list

        out["PremigrationAssessmentStatuses"] = (
            capo_database_migration_service.types.premigration_assessment_status_list.serialize_aws_json_1_1(
                value["premigration_assessment_statuses"]
            )
        )
    if "stop_reason" in value:
        out["StopReason"] = value["stop_reason"]
    if "failure_messages" in value:
        import capo_database_migration_service.types.string_list

        out["FailureMessages"] = (
            capo_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["failure_messages"]
            )
        )
    if "replication_stats" in value:
        import capo_database_migration_service.types.replication_stats

        out["ReplicationStats"] = (
            capo_database_migration_service.types.replication_stats.serialize_aws_json_1_1(
                value["replication_stats"]
            )
        )
    if "start_replication_type" in value:
        out["StartReplicationType"] = value["start_replication_type"]
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
    if "recovery_checkpoint" in value:
        out["RecoveryCheckpoint"] = value["recovery_checkpoint"]
    if "replication_create_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationCreateTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_create_time"]
            )
        )
    if "replication_update_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationUpdateTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_update_time"]
            )
        )
    if "replication_last_stop_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationLastStopTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_last_stop_time"]
            )
        )
    if "replication_deprovision_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationDeprovisionTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_deprovision_time"]
            )
        )
    if "is_read_only" in value:
        out["IsReadOnly"] = value["is_read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Replication:
    out: Replication = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigIdentifier") is not None:
        out["replication_config_identifier"] = data["ReplicationConfigIdentifier"]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    if data.get("SourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if data.get("TargetEndpointArn") is not None:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    if data.get("ReplicationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["replication_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["ReplicationType"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("ProvisionData") is not None:
        import capo_database_migration_service.types.provision_data

        out["provision_data"] = (
            capo_database_migration_service.types.provision_data.deserialize_aws_json_1_1(
                data["ProvisionData"]
            )
        )
    if data.get("PremigrationAssessmentStatuses") is not None:
        import capo_database_migration_service.types.premigration_assessment_status_list

        out["premigration_assessment_statuses"] = (
            capo_database_migration_service.types.premigration_assessment_status_list.deserialize_aws_json_1_1(
                data["PremigrationAssessmentStatuses"]
            )
        )
    if data.get("StopReason") is not None:
        out["stop_reason"] = data["StopReason"]
    if data.get("FailureMessages") is not None:
        import capo_database_migration_service.types.string_list

        out["failure_messages"] = (
            capo_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["FailureMessages"]
            )
        )
    if data.get("ReplicationStats") is not None:
        import capo_database_migration_service.types.replication_stats

        out["replication_stats"] = (
            capo_database_migration_service.types.replication_stats.deserialize_aws_json_1_1(
                data["ReplicationStats"]
            )
        )
    if data.get("StartReplicationType") is not None:
        out["start_replication_type"] = data["StartReplicationType"]
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
    if data.get("RecoveryCheckpoint") is not None:
        out["recovery_checkpoint"] = data["RecoveryCheckpoint"]
    if data.get("ReplicationCreateTime") is not None:
        import capo_database_migration_service.types.t_stamp

        out["replication_create_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationCreateTime"]
            )
        )
    if data.get("ReplicationUpdateTime") is not None:
        import capo_database_migration_service.types.t_stamp

        out["replication_update_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationUpdateTime"]
            )
        )
    if data.get("ReplicationLastStopTime") is not None:
        import capo_database_migration_service.types.t_stamp

        out["replication_last_stop_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationLastStopTime"]
            )
        )
    if data.get("ReplicationDeprovisionTime") is not None:
        import capo_database_migration_service.types.t_stamp

        out["replication_deprovision_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationDeprovisionTime"]
            )
        )
    if data.get("IsReadOnly") is not None:
        out["is_read_only"] = data["IsReadOnly"]
    return out

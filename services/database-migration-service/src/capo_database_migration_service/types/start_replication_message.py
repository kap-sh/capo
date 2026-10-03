"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class StartReplicationMessage(TypedDict, closed=True):
    replication_config_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name of the replication for which to start replication.</p>"""
    start_replication_type: "capo_database_migration_service.types.string.String"
    """<p>The replication type.</p> <p>When the replication type is <code>full-load</code> or <code>full-load-and-cdc</code>, the only valid value for the first run of the replication is <code>start-replication</code>. This option will start the replication.</p> <p>You can also use <a>ReloadTables</a> to reload specific tables that failed during replication instead of restarting the replication.</p> <p>The <code>resume-processing</code> option isn't applicable for a full-load replication, because you can't resume partially loaded tables during the full load phase.</p> <p>For a <code>full-load-and-cdc</code> replication, DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use <code>reload-target</code>. Otherwise use <code>resume-processing</code>, to replicate the changes from the last stop position.</p>"""
    premigration_assessment_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>User-defined settings for the premigration assessment. The possible values are:</p> <ul> <li> <p> <code>ResultLocationFolder</code>: The folder within an Amazon S3 bucket where you want DMS to store the results of this assessment run.</p> </li> <li> <p> <code>ResultEncryptionMode</code>: The supported values are <code>SSE_KMS</code> and <code>SSE_S3</code>. If these values are not provided, then the files are not encrypted at rest. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.KMSKeys">Creating Amazon Web Services KMS keys to encrypt Amazon S3 target objects</a>.</p> </li> <li> <p> <code>ResultKmsKeyArn</code>: The ARN of a customer KMS encryption key that you specify when you set <code>ResultEncryptionMode</code> to <code>SSE_KMS</code>.</p> </li> <li> <p> <code>IncludeOnly</code>: A space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that Database Migration Service supports for the associated migration.</p> </li> <li> <p> <code>Exclude</code>: A space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that Database Migration Service supports for the associated migration.</p> </li> <li> <p> <code>FailOnAssessmentFailure</code>: A configurable setting you can set to <code>true</code> (the default setting) or <code>false</code>. Use this setting to to stop the replication from starting automatically if the assessment fails. This can help you evaluate the issue that is preventing the replication from running successfully.</p> </li> </ul>"""
    cdc_start_time: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p>Indicates the start time for a change data capture (CDC) operation. Use either <code>CdcStartTime</code> or <code>CdcStartPosition</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p>"""
    cdc_start_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to start. Use either <code>CdcStartPosition</code> or <code>CdcStartTime</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p>The value can be in date, checkpoint, or LSN/SCN format.</p>"""
    cdc_stop_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    out["StartReplicationType"] = value["start_replication_type"]
    if "premigration_assessment_settings" in value:
        out["PremigrationAssessmentSettings"] = value[
            "premigration_assessment_settings"
        ]
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


def deserialize_aws_json_1_1(data: dict) -> StartReplicationMessage:
    out: StartReplicationMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        raise DeserializationError(
            "StartReplicationMessage.replication_config_arn required"
        )
    if data.get("StartReplicationType") is not None:
        out["start_replication_type"] = data["StartReplicationType"]
    else:
        raise DeserializationError(
            "StartReplicationMessage.start_replication_type required"
        )
    if data.get("PremigrationAssessmentSettings") is not None:
        out["premigration_assessment_settings"] = data["PremigrationAssessmentSettings"]
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

"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterAutomatedBackup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zones
    import capo_rds.types.boolean
    import capo_rds.types.integer
    import capo_rds.types.integer_optional
    import capo_rds.types.restore_window
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class DBClusterAutomatedBackup(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine for this automated backup.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>The VPC ID associated with the DB cluster.</p>"""
    db_cluster_automated_backups_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the automated backups.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the source DB cluster, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""
    restore_window: NotRequired["capo_rds.types.restore_window.RestoreWindow"]
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master user name of the automated backup.</p>"""
    db_cluster_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The resource ID for the source DB cluster, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""
    region: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region associated with the automated backup.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model information for this DB cluster automated backup.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>A list of status information for an automated backup:</p> <ul> <li> <p> <code>retained</code> - Automated backups for deleted clusters.</p> </li> </ul>"""
    iam_database_authentication_enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    cluster_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the DB cluster was created, in Universal Coordinated Time (UTC).</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the source DB cluster is encrypted.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the automated backup. Possible values:</p> <ul> <li> <p> <code>none</code> - The automated backup is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The automated backup is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The automated backup is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    allocated_storage: NotRequired["capo_rds.types.integer.Integer"]
    """<p>For all database engines except Amazon Aurora, <code>AllocatedStorage</code> specifies the allocated storage size in gibibytes (GiB). For Aurora, <code>AllocatedStorage</code> always returns 1, because Aurora DB cluster storage size isn't fixed, but instead automatically adjusts as needed.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine for the automated backup.</p>"""
    db_cluster_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the source DB cluster.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The retention period for the automated backups.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    engine_mode: NotRequired["capo_rds.types.string.String"]
    """<p>The engine mode of the database engine for the automated backup.</p>"""
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>The Availability Zones where instances in the DB cluster can be created. For information on Amazon Web Services Regions and Availability Zones, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html">Regions and Availability Zones</a>.</p>"""
    port: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The port number that the automated backup used for connections.</p> <p>Default: Inherits from the source DB cluster</p> <p>Valid Values: <code>1150-65535</code> </p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key ID for an automated backup.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type associated with the DB cluster.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The IOPS (I/O operations per second) value for the automated backup.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput for the automated backup. The throughput is automatically set based on the IOPS that you provision, and is not configurable.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    aws_backup_recovery_point_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterAutomatedBackup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "db_cluster_automated_backups_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterAutomatedBackupsArn",
                str(value["db_cluster_automated_backups_arn"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "restore_window" in value:
        import capo_rds.types.restore_window

        capo_rds.types.restore_window.serialize_query(
            value["restore_window"], pairs, f"{key_prefix}RestoreWindow"
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "db_cluster_resource_id" in value:
        pairs.append(
            (f"{key_prefix}DbClusterResourceId", str(value["db_cluster_resource_id"]))
        )
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "cluster_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "storage_encryption_type" in value:
        import capo_rds.types.storage_encryption_type

        capo_rds.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "db_cluster_arn" in value:
        pairs.append((f"{key_prefix}DBClusterArn", str(value["db_cluster_arn"])))
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "engine_mode" in value:
        pairs.append((f"{key_prefix}EngineMode", str(value["engine_mode"])))
    if "availability_zones" in value:
        import capo_rds.types.availability_zones

        capo_rds.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "aws_backup_recovery_point_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AwsBackupRecoveryPointArn",
                str(value["aws_backup_recovery_point_arn"]),
            )
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )


def deserialize_query(el: Element) -> DBClusterAutomatedBackup:
    out: DBClusterAutomatedBackup = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_db_cluster_automated_backups_arn = el.find("DBClusterAutomatedBackupsArn")
    if child_db_cluster_automated_backups_arn is not None:
        out["db_cluster_automated_backups_arn"] = str(
            child_db_cluster_automated_backups_arn.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_restore_window = el.find("RestoreWindow")
    if child_restore_window is not None:
        import capo_rds.types.restore_window

        out["restore_window"] = capo_rds.types.restore_window.deserialize_query(
            child_restore_window
        )
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_db_cluster_resource_id = el.find("DbClusterResourceId")
    if child_db_cluster_resource_id is not None:
        out["db_cluster_resource_id"] = str(child_db_cluster_resource_id.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_cluster_create_time = el.find("ClusterCreateTime")
    if child_cluster_create_time is not None:
        import capo_rds.types.t_stamp

        out["cluster_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_rds.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_rds.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_cluster_arn = el.find("DBClusterArn")
    if child_db_cluster_arn is not None:
        out["db_cluster_arn"] = str(child_db_cluster_arn.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_engine_mode = el.find("EngineMode")
    if child_engine_mode is not None:
        out["engine_mode"] = str(child_engine_mode.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_rds.types.availability_zones

        out["availability_zones"] = capo_rds.types.availability_zones.deserialize_query(
            child_availability_zones
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_aws_backup_recovery_point_arn = el.find("AwsBackupRecoveryPointArn")
    if child_aws_backup_recovery_point_arn is not None:
        out["aws_backup_recovery_point_arn"] = str(
            child_aws_backup_recovery_point_arn.text or ""
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    return out

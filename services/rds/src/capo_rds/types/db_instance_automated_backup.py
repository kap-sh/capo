"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.db_instance_automated_backups_replication_list
    import capo_rds.types.integer
    import capo_rds.types.integer_optional
    import capo_rds.types.restore_window
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class DBInstanceAutomatedBackup(TypedDict, closed=True):
    db_instance_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the automated backups.</p>"""
    dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The resource ID for the source DB instance, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""
    region: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region associated with the automated backup.</p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the source DB instance, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""
    restore_window: NotRequired["capo_rds.types.restore_window.RestoreWindow"]
    """<p>The earliest and latest time a DB instance can be restored to.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The allocated storage size for the automated backup in gibibytes (GiB).</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>A list of status information for an automated backup:</p> <ul> <li> <p> <code>active</code> - Automated backups for current instances.</p> </li> <li> <p> <code>retained</code> - Automated backups for deleted instances.</p> </li> <li> <p> <code>creating</code> - Automated backups that are waiting for the first automated snapshot to be available.</p> </li> </ul>"""
    port: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The port number that the automated backup used for connections.</p> <p>Default: Inherits from the source DB instance</p> <p>Valid Values: <code>1150-65535</code> </p>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The Availability Zone that the automated backup was created in. For information on Amazon Web Services Regions and Availability Zones, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html">Regions and Availability Zones</a>.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>The VPC ID associated with the DB instance.</p>"""
    instance_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the DB instance was created.</p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master user name of an automated backup.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine for this automated backup.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine for the automated backup.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model information for the automated backup.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The IOPS (I/O operations per second) value for the automated backup.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput for the automated backup.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group the automated backup is associated with. If omitted, the default option group for the engine specified is used.</p>"""
    tde_credential_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN from the key store with which the automated backup is associated for TDE encryption.</p>"""
    encrypted: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the automated backup is encrypted.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the automated backup. Possible values:</p> <ul> <li> <p> <code>none</code> - The automated backup is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The automated backup is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The automated backup is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type associated with the automated backup.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key ID for an automated backup.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    timezone: NotRequired["capo_rds.types.string.String"]
    """<p>The time zone of the automated backup. In most cases, the <code>Timezone</code> element is empty. <code>Timezone</code> content appears only for Microsoft SQL Server DB instances that were created with a time zone specified.</p>"""
    iam_database_authentication_enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>True if mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The retention period for the automated backups.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    db_instance_automated_backups_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the replicated automated backups.</p>"""
    db_instance_automated_backups_replications: NotRequired[
        "capo_rds.types.db_instance_automated_backups_replication_list.DBInstanceAutomatedBackupsReplicationList"
    ]
    """<p>The list of replications to different Amazon Web Services Regions associated with the automated backup.</p>"""
    backup_target: NotRequired["capo_rds.types.string.String"]
    """<p>The location where automated backups are stored: Dedicated Local Zones, Amazon Web Services Outposts or the Amazon Web Services Region.</p>"""
    multi_tenant: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the automatic backup is for a DB instance in the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE). </p>"""
    aws_backup_recovery_point_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>The additional storage volumes associated with the automated backup.</p> <p>Valid Values: <code>GP3 | IO2</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceAutomatedBackup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_arn" in value:
        pairs.append((f"{key_prefix}DBInstanceArn", str(value["db_instance_arn"])))
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "restore_window" in value:
        import capo_rds.types.restore_window

        capo_rds.types.restore_window.serialize_query(
            value["restore_window"], pairs, f"{key_prefix}RestoreWindow"
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "instance_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["instance_create_time"], pairs, f"{key_prefix}InstanceCreateTime"
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "tde_credential_arn" in value:
        pairs.append(
            (f"{key_prefix}TdeCredentialArn", str(value["tde_credential_arn"]))
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "storage_encryption_type" in value:
        import capo_rds.types.storage_encryption_type

        capo_rds.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
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
    if "db_instance_automated_backups_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DBInstanceAutomatedBackupsArn",
                str(value["db_instance_automated_backups_arn"]),
            )
        )
    if "db_instance_automated_backups_replications" in value:
        import capo_rds.types.db_instance_automated_backups_replication_list

        capo_rds.types.db_instance_automated_backups_replication_list.serialize_query(
            value["db_instance_automated_backups_replications"],
            pairs,
            f"{key_prefix}DBInstanceAutomatedBackupsReplications",
        )
    if "backup_target" in value:
        pairs.append((f"{key_prefix}BackupTarget", str(value["backup_target"])))
    if "multi_tenant" in value:
        pairs.append(
            (f"{key_prefix}MultiTenant", "true" if value["multi_tenant"] else "false")
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
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "additional_storage_volumes" in value:
        import capo_rds.types.additional_storage_volumes_list

        capo_rds.types.additional_storage_volumes_list.serialize_query(
            value["additional_storage_volumes"],
            pairs,
            f"{key_prefix}AdditionalStorageVolumes",
        )


def deserialize_query(el: Element) -> DBInstanceAutomatedBackup:
    out: DBInstanceAutomatedBackup = {}  # type: ignore[typeddict-item]
    child_db_instance_arn = el.find("DBInstanceArn")
    if child_db_instance_arn is not None:
        out["db_instance_arn"] = str(child_db_instance_arn.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_restore_window = el.find("RestoreWindow")
    if child_restore_window is not None:
        import capo_rds.types.restore_window

        out["restore_window"] = capo_rds.types.restore_window.deserialize_query(
            child_restore_window
        )
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_instance_create_time = el.find("InstanceCreateTime")
    if child_instance_create_time is not None:
        import capo_rds.types.t_stamp

        out["instance_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_instance_create_time
        )
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_rds.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_rds.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_db_instance_automated_backups_arn = el.find("DBInstanceAutomatedBackupsArn")
    if child_db_instance_automated_backups_arn is not None:
        out["db_instance_automated_backups_arn"] = str(
            child_db_instance_automated_backups_arn.text or ""
        )
    child_db_instance_automated_backups_replications = el.find(
        "DBInstanceAutomatedBackupsReplications"
    )
    if child_db_instance_automated_backups_replications is not None:
        import capo_rds.types.db_instance_automated_backups_replication_list

        out["db_instance_automated_backups_replications"] = (
            capo_rds.types.db_instance_automated_backups_replication_list.deserialize_query(
                child_db_instance_automated_backups_replications
            )
        )
    child_backup_target = el.find("BackupTarget")
    if child_backup_target is not None:
        out["backup_target"] = str(child_backup_target.text or "")
    child_multi_tenant = el.find("MultiTenant")
    if child_multi_tenant is not None:
        out["multi_tenant"] = (child_multi_tenant.text or "").lower() == "true"
    child_aws_backup_recovery_point_arn = el.find("AwsBackupRecoveryPointArn")
    if child_aws_backup_recovery_point_arn is not None:
        out["aws_backup_recovery_point_arn"] = str(
            child_aws_backup_recovery_point_arn.text or ""
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.additional_storage_volumes_list

        out["additional_storage_volumes"] = (
            capo_rds.types.additional_storage_volumes_list.deserialize_query(
                child_additional_storage_volumes
            )
        )
    return out

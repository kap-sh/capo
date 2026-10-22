"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zones
    import capo_rds.types.boolean
    import capo_rds.types.integer
    import capo_rds.types.integer_optional
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class DBClusterSnapshot(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>The list of Availability Zones (AZs) where instances in the DB cluster snapshot can be restored.</p>"""
    db_cluster_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the DB cluster snapshot.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.</p>"""
    snapshot_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the snapshot was taken, in Universal Coordinated Time (UTC).</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine for this DB cluster snapshot.</p>"""
    engine_mode: NotRequired["capo_rds.types.string.String"]
    """<p>The engine mode of the database engine for this DB cluster snapshot.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The allocated storage size of the DB cluster snapshot in gibibytes (GiB).</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of this DB cluster snapshot. Valid statuses are the following:</p> <ul> <li> <p> <code>available</code> </p> </li> <li> <p> <code>copying</code> </p> </li> <li> <p> <code>creating</code> </p> </li> </ul>"""
    port: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The port that the DB cluster was listening on at the time of the snapshot.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>The VPC ID associated with the DB cluster snapshot.</p>"""
    cluster_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the DB cluster was created, in Universal Coordinated Time (UTC).</p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master username for this DB cluster snapshot.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine for this DB cluster snapshot.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model information for this DB cluster snapshot.</p>"""
    snapshot_type: NotRequired["capo_rds.types.string.String"]
    """<p>The type of the DB cluster snapshot.</p>"""
    percent_progress: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The percentage of the estimated data that has been transferred.</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether the DB cluster snapshot is encrypted with an Amazon Web Services managed key or a customer managed key.</p> <p>If the DB cluster snapshot is encrypted with an Amazon Web Services owned key, this value is <code>false</code> and <code>StorageEncryptionType</code> is <code>sse-rds</code>. In that case, the data at rest is still encrypted. To determine how the data at rest is protected, use <code>StorageEncryptionType</code>.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the DB cluster snapshot. Possible values:</p> <ul> <li> <p> <code>none</code> - The DB cluster snapshot is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The DB cluster snapshot is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The DB cluster snapshot is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automatic DB snapshots are retained.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>If <code>StorageEncrypted</code> is true, the Amazon Web Services KMS key identifier for the encrypted DB cluster snapshot.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    db_cluster_snapshot_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB cluster snapshot.</p>"""
    source_db_cluster_snapshot_arn: NotRequired["capo_rds.types.string.String"]
    """<p>If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.</p>"""
    iam_database_authentication_enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type associated with the DB cluster snapshot.</p> <p>This setting is only for Aurora DB clusters.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput for the DB cluster snapshot. The throughput is automatically set based on the IOPS that you provision, and is not configurable.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    db_cluster_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The resource ID of the DB cluster that this DB cluster snapshot was created from.</p>"""
    db_system_id: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshot, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_rds.types.availability_zones

        capo_rds.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "snapshot_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["snapshot_create_time"], pairs, f"{key_prefix}SnapshotCreateTime"
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_mode" in value:
        pairs.append((f"{key_prefix}EngineMode", str(value["engine_mode"])))
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "cluster_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "percent_progress" in value:
        pairs.append((f"{key_prefix}PercentProgress", str(value["percent_progress"])))
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
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "db_cluster_snapshot_arn" in value:
        pairs.append(
            (f"{key_prefix}DBClusterSnapshotArn", str(value["db_cluster_snapshot_arn"]))
        )
    if "source_db_cluster_snapshot_arn" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterSnapshotArn",
                str(value["source_db_cluster_snapshot_arn"]),
            )
        )
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "db_cluster_resource_id" in value:
        pairs.append(
            (f"{key_prefix}DbClusterResourceId", str(value["db_cluster_resource_id"]))
        )
    if "db_system_id" in value:
        pairs.append((f"{key_prefix}DBSystemId", str(value["db_system_id"])))


def deserialize_query(el: Element) -> DBClusterSnapshot:
    out: DBClusterSnapshot = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_rds.types.availability_zones

        out["availability_zones"] = capo_rds.types.availability_zones.deserialize_query(
            child_availability_zones
        )
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_snapshot_create_time = el.find("SnapshotCreateTime")
    if child_snapshot_create_time is not None:
        import capo_rds.types.t_stamp

        out["snapshot_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_snapshot_create_time
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_mode = el.find("EngineMode")
    if child_engine_mode is not None:
        out["engine_mode"] = str(child_engine_mode.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_cluster_create_time = el.find("ClusterCreateTime")
    if child_cluster_create_time is not None:
        import capo_rds.types.t_stamp

        out["cluster_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_percent_progress = el.find("PercentProgress")
    if child_percent_progress is not None:
        out["percent_progress"] = int(child_percent_progress.text or "")
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
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_db_cluster_snapshot_arn = el.find("DBClusterSnapshotArn")
    if child_db_cluster_snapshot_arn is not None:
        out["db_cluster_snapshot_arn"] = str(child_db_cluster_snapshot_arn.text or "")
    child_source_db_cluster_snapshot_arn = el.find("SourceDBClusterSnapshotArn")
    if child_source_db_cluster_snapshot_arn is not None:
        out["source_db_cluster_snapshot_arn"] = str(
            child_source_db_cluster_snapshot_arn.text or ""
        )
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_db_cluster_resource_id = el.find("DbClusterResourceId")
    if child_db_cluster_resource_id is not None:
        out["db_cluster_resource_id"] = str(child_db_cluster_resource_id.text or "")
    child_db_system_id = el.find("DBSystemId")
    if child_db_system_id is not None:
        out["db_system_id"] = str(child_db_system_id.text or "")
    return out

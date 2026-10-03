"""Generated from Smithy shape ``com.amazonaws.redshift#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.accounts_with_restore_access_list
    import capo_redshift.types.boolean
    import capo_redshift.types.double
    import capo_redshift.types.integer
    import capo_redshift.types.integer_optional
    import capo_redshift.types.long
    import capo_redshift.types.restorable_node_type_list
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.tag_list


class Snapshot(TypedDict, closed=True):
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The snapshot identifier that is provided in the request.</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster for which the snapshot was taken.</p>"""
    snapshot_create_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.</p>"""
    status: NotRequired["capo_redshift.types.string.String"]
    """<p>The snapshot status. The value of the status depends on the API operation used: </p> <ul> <li> <p> <a>CreateClusterSnapshot</a> and <a>CopyClusterSnapshot</a> returns status as "creating". </p> </li> <li> <p> <a>DescribeClusterSnapshots</a> returns status as "creating", "available", "final snapshot", or "failed".</p> </li> <li> <p> <a>DeleteClusterSnapshot</a> returns status as "deleted".</p> </li> </ul>"""
    port: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The port that the cluster is listening on.</p>"""
    availability_zone: NotRequired["capo_redshift.types.string.String"]
    """<p>The Availability Zone in which the cluster was created.</p>"""
    cluster_create_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time (UTC) when the cluster was originally created.</p>"""
    master_username: NotRequired["capo_redshift.types.string.String"]
    """<p>The admin user name for the cluster.</p>"""
    cluster_version: NotRequired["capo_redshift.types.string.String"]
    """<p>The version ID of the Amazon Redshift engine that is running on the cluster.</p>"""
    engine_full_version: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster version of the cluster used to create the snapshot. For example, 1.0.15503. </p>"""
    snapshot_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The snapshot type. Snapshots created using <a>CreateClusterSnapshot</a> and <a>CopyClusterSnapshot</a> are of type "manual". </p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type of the nodes in the cluster.</p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The number of nodes in the cluster.</p>"""
    db_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the database that was created when the cluster was created.</p>"""
    vpc_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.</p>"""
    encrypted: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>If <code>true</code>, the data in the snapshot is encrypted at rest.</p>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.</p>"""
    encrypted_with_hsm: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. <code>true</code> indicates that the data is encrypted using HSM keys.</p>"""
    accounts_with_restore_access: NotRequired[
        "capo_redshift.types.accounts_with_restore_access_list.AccountsWithRestoreAccessList"
    ]
    """<p>A list of the Amazon Web Services accounts authorized to restore the snapshot. Returns <code>null</code> if no accounts are authorized. Visible only to the snapshot owner. </p>"""
    owner_account: NotRequired["capo_redshift.types.string.String"]
    """<p>For manual snapshots, the Amazon Web Services account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.</p>"""
    total_backup_size_in_mega_bytes: NotRequired["capo_redshift.types.double.Double"]
    """<p>The size of the complete set of backup data that would be used to restore the cluster.</p>"""
    actual_incremental_backup_size_in_mega_bytes: NotRequired[
        "capo_redshift.types.double.Double"
    ]
    """<p>The size of the incremental backup.</p>"""
    backup_progress_in_mega_bytes: NotRequired["capo_redshift.types.double.Double"]
    """<p>The number of megabytes that have been transferred to the snapshot backup.</p>"""
    current_backup_rate_in_mega_bytes_per_second: NotRequired[
        "capo_redshift.types.double.Double"
    ]
    """<p>The number of megabytes per second being transferred to the snapshot backup. Returns <code>0</code> for a completed backup. </p>"""
    estimated_seconds_to_completion: NotRequired["capo_redshift.types.long.Long"]
    """<p>The estimate of the time remaining before the snapshot backup will complete. Returns <code>0</code> for a completed backup. </p>"""
    elapsed_time_in_seconds: NotRequired["capo_redshift.types.long.Long"]
    """<p>The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.</p>"""
    source_region: NotRequired["capo_redshift.types.string.String"]
    """<p>The source region from which the snapshot was copied.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the cluster snapshot.</p>"""
    restorable_node_types: NotRequired[
        "capo_redshift.types.restorable_node_type_list.RestorableNodeTypeList"
    ]
    """<p>The list of node types that this cluster snapshot is able to restore into.</p>"""
    enhanced_vpc_routing: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>"""
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the maintenance track for the snapshot.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""
    manual_snapshot_remaining_days: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days until a manual snapshot will pass its retention period.</p>"""
    snapshot_retention_start_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>A timestamp representing the start of the retention period for the snapshot.</p>"""
    master_password_secret_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the cluster's admin user credentials secret.</p>"""
    master_password_secret_kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret.</p>"""
    snapshot_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Snapshot, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "snapshot_create_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["snapshot_create_time"], pairs, f"{key_prefix}SnapshotCreateTime"
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "cluster_create_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "cluster_version" in value:
        pairs.append((f"{key_prefix}ClusterVersion", str(value["cluster_version"])))
    if "engine_full_version" in value:
        pairs.append(
            (f"{key_prefix}EngineFullVersion", str(value["engine_full_version"]))
        )
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "number_of_nodes" in value:
        pairs.append((f"{key_prefix}NumberOfNodes", str(value["number_of_nodes"])))
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "encrypted_with_hsm" in value:
        pairs.append(
            (
                f"{key_prefix}EncryptedWithHSM",
                "true" if value["encrypted_with_hsm"] else "false",
            )
        )
    if "accounts_with_restore_access" in value:
        import capo_redshift.types.accounts_with_restore_access_list

        capo_redshift.types.accounts_with_restore_access_list.serialize_query(
            value["accounts_with_restore_access"],
            pairs,
            f"{key_prefix}AccountsWithRestoreAccess",
        )
    if "owner_account" in value:
        pairs.append((f"{key_prefix}OwnerAccount", str(value["owner_account"])))
    if "total_backup_size_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}TotalBackupSizeInMegaBytes",
                (
                    "NaN"
                    if value["total_backup_size_in_mega_bytes"]
                    != value["total_backup_size_in_mega_bytes"]
                    else "Infinity"
                    if value["total_backup_size_in_mega_bytes"] == float("inf")
                    else "-Infinity"
                    if value["total_backup_size_in_mega_bytes"] == float("-inf")
                    else str(value["total_backup_size_in_mega_bytes"])
                ),
            )
        )
    if "actual_incremental_backup_size_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}ActualIncrementalBackupSizeInMegaBytes",
                (
                    "NaN"
                    if value["actual_incremental_backup_size_in_mega_bytes"]
                    != value["actual_incremental_backup_size_in_mega_bytes"]
                    else "Infinity"
                    if value["actual_incremental_backup_size_in_mega_bytes"]
                    == float("inf")
                    else "-Infinity"
                    if value["actual_incremental_backup_size_in_mega_bytes"]
                    == float("-inf")
                    else str(value["actual_incremental_backup_size_in_mega_bytes"])
                ),
            )
        )
    if "backup_progress_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}BackupProgressInMegaBytes",
                (
                    "NaN"
                    if value["backup_progress_in_mega_bytes"]
                    != value["backup_progress_in_mega_bytes"]
                    else "Infinity"
                    if value["backup_progress_in_mega_bytes"] == float("inf")
                    else "-Infinity"
                    if value["backup_progress_in_mega_bytes"] == float("-inf")
                    else str(value["backup_progress_in_mega_bytes"])
                ),
            )
        )
    if "current_backup_rate_in_mega_bytes_per_second" in value:
        pairs.append(
            (
                f"{key_prefix}CurrentBackupRateInMegaBytesPerSecond",
                (
                    "NaN"
                    if value["current_backup_rate_in_mega_bytes_per_second"]
                    != value["current_backup_rate_in_mega_bytes_per_second"]
                    else "Infinity"
                    if value["current_backup_rate_in_mega_bytes_per_second"]
                    == float("inf")
                    else "-Infinity"
                    if value["current_backup_rate_in_mega_bytes_per_second"]
                    == float("-inf")
                    else str(value["current_backup_rate_in_mega_bytes_per_second"])
                ),
            )
        )
    if "estimated_seconds_to_completion" in value:
        pairs.append(
            (
                f"{key_prefix}EstimatedSecondsToCompletion",
                str(value["estimated_seconds_to_completion"]),
            )
        )
    if "elapsed_time_in_seconds" in value:
        pairs.append(
            (f"{key_prefix}ElapsedTimeInSeconds", str(value["elapsed_time_in_seconds"]))
        )
    if "source_region" in value:
        pairs.append((f"{key_prefix}SourceRegion", str(value["source_region"])))
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "restorable_node_types" in value:
        import capo_redshift.types.restorable_node_type_list

        capo_redshift.types.restorable_node_type_list.serialize_query(
            value["restorable_node_types"], pairs, f"{key_prefix}RestorableNodeTypes"
        )
    if "enhanced_vpc_routing" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedVpcRouting",
                "true" if value["enhanced_vpc_routing"] else "false",
            )
        )
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{key_prefix}MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )
    if "manual_snapshot_remaining_days" in value:
        pairs.append(
            (
                f"{key_prefix}ManualSnapshotRemainingDays",
                str(value["manual_snapshot_remaining_days"]),
            )
        )
    if "snapshot_retention_start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["snapshot_retention_start_time"],
            pairs,
            f"{key_prefix}SnapshotRetentionStartTime",
        )
    if "master_password_secret_arn" in value:
        pairs.append(
            (
                f"{key_prefix}MasterPasswordSecretArn",
                str(value["master_password_secret_arn"]),
            )
        )
    if "master_password_secret_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}MasterPasswordSecretKmsKeyId",
                str(value["master_password_secret_kms_key_id"]),
            )
        )
    if "snapshot_arn" in value:
        pairs.append((f"{key_prefix}SnapshotArn", str(value["snapshot_arn"])))


def deserialize_query(el: Element) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_snapshot_create_time = el.find("SnapshotCreateTime")
    if child_snapshot_create_time is not None:
        import capo_redshift.types.t_stamp

        out["snapshot_create_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_snapshot_create_time
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_cluster_create_time = el.find("ClusterCreateTime")
    if child_cluster_create_time is not None:
        import capo_redshift.types.t_stamp

        out["cluster_create_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_engine_full_version = el.find("EngineFullVersion")
    if child_engine_full_version is not None:
        out["engine_full_version"] = str(child_engine_full_version.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_encrypted_with_hsm = el.find("EncryptedWithHSM")
    if child_encrypted_with_hsm is not None:
        out["encrypted_with_hsm"] = (
            child_encrypted_with_hsm.text or ""
        ).lower() == "true"
    child_accounts_with_restore_access = el.find("AccountsWithRestoreAccess")
    if child_accounts_with_restore_access is not None:
        import capo_redshift.types.accounts_with_restore_access_list

        out["accounts_with_restore_access"] = (
            capo_redshift.types.accounts_with_restore_access_list.deserialize_query(
                child_accounts_with_restore_access
            )
        )
    child_owner_account = el.find("OwnerAccount")
    if child_owner_account is not None:
        out["owner_account"] = str(child_owner_account.text or "")
    child_total_backup_size_in_mega_bytes = el.find("TotalBackupSizeInMegaBytes")
    if child_total_backup_size_in_mega_bytes is not None:
        out["total_backup_size_in_mega_bytes"] = float(
            child_total_backup_size_in_mega_bytes.text or ""
        )
    child_actual_incremental_backup_size_in_mega_bytes = el.find(
        "ActualIncrementalBackupSizeInMegaBytes"
    )
    if child_actual_incremental_backup_size_in_mega_bytes is not None:
        out["actual_incremental_backup_size_in_mega_bytes"] = float(
            child_actual_incremental_backup_size_in_mega_bytes.text or ""
        )
    child_backup_progress_in_mega_bytes = el.find("BackupProgressInMegaBytes")
    if child_backup_progress_in_mega_bytes is not None:
        out["backup_progress_in_mega_bytes"] = float(
            child_backup_progress_in_mega_bytes.text or ""
        )
    child_current_backup_rate_in_mega_bytes_per_second = el.find(
        "CurrentBackupRateInMegaBytesPerSecond"
    )
    if child_current_backup_rate_in_mega_bytes_per_second is not None:
        out["current_backup_rate_in_mega_bytes_per_second"] = float(
            child_current_backup_rate_in_mega_bytes_per_second.text or ""
        )
    child_estimated_seconds_to_completion = el.find("EstimatedSecondsToCompletion")
    if child_estimated_seconds_to_completion is not None:
        out["estimated_seconds_to_completion"] = int(
            child_estimated_seconds_to_completion.text or ""
        )
    child_elapsed_time_in_seconds = el.find("ElapsedTimeInSeconds")
    if child_elapsed_time_in_seconds is not None:
        out["elapsed_time_in_seconds"] = int(child_elapsed_time_in_seconds.text or "")
    child_source_region = el.find("SourceRegion")
    if child_source_region is not None:
        out["source_region"] = str(child_source_region.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    child_restorable_node_types = el.find("RestorableNodeTypes")
    if child_restorable_node_types is not None:
        import capo_redshift.types.restorable_node_type_list

        out["restorable_node_types"] = (
            capo_redshift.types.restorable_node_type_list.deserialize_query(
                child_restorable_node_types
            )
        )
    child_enhanced_vpc_routing = el.find("EnhancedVpcRouting")
    if child_enhanced_vpc_routing is not None:
        out["enhanced_vpc_routing"] = (
            child_enhanced_vpc_routing.text or ""
        ).lower() == "true"
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    child_manual_snapshot_remaining_days = el.find("ManualSnapshotRemainingDays")
    if child_manual_snapshot_remaining_days is not None:
        out["manual_snapshot_remaining_days"] = int(
            child_manual_snapshot_remaining_days.text or ""
        )
    child_snapshot_retention_start_time = el.find("SnapshotRetentionStartTime")
    if child_snapshot_retention_start_time is not None:
        import capo_redshift.types.t_stamp

        out["snapshot_retention_start_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_snapshot_retention_start_time
            )
        )
    child_master_password_secret_arn = el.find("MasterPasswordSecretArn")
    if child_master_password_secret_arn is not None:
        out["master_password_secret_arn"] = str(
            child_master_password_secret_arn.text or ""
        )
    child_master_password_secret_kms_key_id = el.find("MasterPasswordSecretKmsKeyId")
    if child_master_password_secret_kms_key_id is not None:
        out["master_password_secret_kms_key_id"] = str(
            child_master_password_secret_kms_key_id.text or ""
        )
    child_snapshot_arn = el.find("SnapshotArn")
    if child_snapshot_arn is not None:
        out["snapshot_arn"] = str(child_snapshot_arn.text or "")
    return out

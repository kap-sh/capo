"""Generated from Smithy shape ``com.amazonaws.neptune#DBCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.availability_zones
    import capo_neptune.types.boolean
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.cluster_pending_modified_values
    import capo_neptune.types.db_cluster_member_list
    import capo_neptune.types.db_cluster_option_group_memberships
    import capo_neptune.types.db_cluster_roles
    import capo_neptune.types.global_cluster_identifier
    import capo_neptune.types.integer_optional
    import capo_neptune.types.log_type_list
    import capo_neptune.types.read_replica_identifier_list
    import capo_neptune.types.serverless_v2_scaling_configuration_info
    import capo_neptune.types.string
    import capo_neptune.types.t_stamp
    import capo_neptune.types.vpc_security_group_membership_list


class DBCluster(TypedDict, closed=True):
    allocated_storage: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p> <code>AllocatedStorage</code> always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.</p>"""
    availability_zones: NotRequired[
        "capo_neptune.types.availability_zones.AvailabilityZones"
    ]
    """<p>Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.</p>"""
    backup_retention_period: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the number of days for which automatic DB snapshots are retained.</p>"""
    character_set_name: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    database_name: NotRequired["capo_neptune.types.string.String"]
    """<p>Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.</p>"""
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.</p>"""
    db_cluster_parameter_group: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the name of the DB cluster parameter group for the DB cluster.</p>"""
    db_subnet_group: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.</p>"""
    status: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the current state of this DB cluster.</p>"""
    percent_progress: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the progress of the operation as a percentage.</p>"""
    earliest_restorable_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p>Specifies the earliest time to which a database can be restored with point-in-time restore.</p>"""
    endpoint: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the connection endpoint for the primary instance of the DB cluster.</p>"""
    reader_endpoint: NotRequired["capo_neptune.types.string.String"]
    """<p>The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.</p> <p>If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.</p>"""
    multi_az: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Specifies whether the DB cluster has instances in multiple Availability Zones.</p>"""
    engine: NotRequired["capo_neptune.types.string.String"]
    """<p>Provides the name of the database engine to be used for this DB cluster.</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>Indicates the database engine version.</p>"""
    latest_restorable_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p>Specifies the latest time to which a database can be restored with point-in-time restore.</p>"""
    port: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>Specifies the port that the database engine is listening on.</p>"""
    master_username: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    db_cluster_option_group_memberships: NotRequired[
        "capo_neptune.types.db_cluster_option_group_memberships.DBClusterOptionGroupMemberships"
    ]
    """<p>Not supported by Neptune.</p>"""
    preferred_backup_window: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    preferred_maintenance_window: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>"""
    replication_source_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    read_replica_identifiers: NotRequired[
        "capo_neptune.types.read_replica_identifier_list.ReadReplicaIdentifierList"
    ]
    """<p>Contains one or more identifiers of the Read Replicas associated with this DB cluster.</p>"""
    db_cluster_members: NotRequired[
        "capo_neptune.types.db_cluster_member_list.DBClusterMemberList"
    ]
    """<p>Provides the list of instances that make up the DB cluster.</p>"""
    vpc_security_groups: NotRequired[
        "capo_neptune.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>Provides a list of VPC security groups that the DB cluster belongs to.</p>"""
    hosted_zone_id: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.</p>"""
    storage_encrypted: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Specifies whether the DB cluster is encrypted.</p>"""
    kms_key_id: NotRequired["capo_neptune.types.string.String"]
    """<p>If <code>StorageEncrypted</code> is true, the Amazon KMS key identifier for the encrypted DB cluster.</p>"""
    db_cluster_resource_id: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Region-unique, immutable identifier for the DB cluster. This identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS key for the DB cluster is accessed.</p>"""
    db_cluster_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB cluster.</p>"""
    associated_roles: NotRequired["capo_neptune.types.db_cluster_roles.DBClusterRoles"]
    """<p>Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_neptune.types.boolean.Boolean"
    ]
    """<p>True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.</p>"""
    clone_group_id: NotRequired["capo_neptune.types.string.String"]
    """<p>Identifies the clone group to which the DB cluster is associated.</p>"""
    cluster_create_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p>Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p> <i>If set to <code>true</code>, tags are copied to any snapshot of the DB cluster that is created.</i> </p>"""
    enabled_cloudwatch_logs_exports: NotRequired[
        "capo_neptune.types.log_type_list.LogTypeList"
    ]
    """<p>A list of the log types that this DB cluster is configured to export to CloudWatch Logs. Valid log types are: <code>audit</code> (to publish audit logs to CloudWatch) and slowquery (to publish slow-query logs to CloudWatch). See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html">Publishing Neptune logs to Amazon CloudWatch logs</a>.</p>"""
    pending_modified_values: NotRequired[
        "capo_neptune.types.cluster_pending_modified_values.ClusterPendingModifiedValues"
    ]
    """<p>This data type is used as a response element in the <code>ModifyDBCluster</code> operation and contains changes that will be applied during the next maintenance window.</p>"""
    deletion_protection: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether or not the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.</p>"""
    cross_account_clone: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>If set to <code>true</code>, the DB cluster can be cloned across accounts.</p>"""
    automatic_restart_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p>Time at which the DB cluster will be automatically restarted.</p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_neptune.types.serverless_v2_scaling_configuration_info.ServerlessV2ScalingConfigurationInfo"
    ]
    """<p>Shows the scaling configuration for a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>"""
    global_cluster_identifier: NotRequired[
        "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.</p>"""
    io_optimized_next_allowed_modification_time: NotRequired[
        "capo_neptune.types.t_stamp.TStamp"
    ]
    """<p>The next time you can modify the DB cluster to use the <code>iopt1</code> storage type.</p>"""
    storage_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The storage type used by the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>standard</code> </b> – ( <i>the default</i> ) Provides cost-effective database storage for applications with moderate to small I/O usage.</p> </li> <li> <p> <b> <code>iopt1</code> </b> – Enables <a href="https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage">I/O-Optimized storage</a> that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.</p> <p>Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.</p> </li> </ul>"""
    network_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBCluster, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "availability_zones" in value:
        import capo_neptune.types.availability_zones

        capo_neptune.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "character_set_name" in value:
        pairs.append(
            (f"{key_prefix}CharacterSetName", str(value["character_set_name"]))
        )
    if "database_name" in value:
        pairs.append((f"{key_prefix}DatabaseName", str(value["database_name"])))
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "db_cluster_parameter_group" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroup",
                str(value["db_cluster_parameter_group"]),
            )
        )
    if "db_subnet_group" in value:
        pairs.append((f"{key_prefix}DBSubnetGroup", str(value["db_subnet_group"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "percent_progress" in value:
        pairs.append((f"{key_prefix}PercentProgress", str(value["percent_progress"])))
    if "earliest_restorable_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["earliest_restorable_time"],
            pairs,
            f"{key_prefix}EarliestRestorableTime",
        )
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "reader_endpoint" in value:
        pairs.append((f"{key_prefix}ReaderEndpoint", str(value["reader_endpoint"])))
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "latest_restorable_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["latest_restorable_time"], pairs, f"{key_prefix}LatestRestorableTime"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "db_cluster_option_group_memberships" in value:
        import capo_neptune.types.db_cluster_option_group_memberships

        capo_neptune.types.db_cluster_option_group_memberships.serialize_query(
            value["db_cluster_option_group_memberships"],
            pairs,
            f"{key_prefix}DBClusterOptionGroupMemberships",
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "replication_source_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}ReplicationSourceIdentifier",
                str(value["replication_source_identifier"]),
            )
        )
    if "read_replica_identifiers" in value:
        import capo_neptune.types.read_replica_identifier_list

        capo_neptune.types.read_replica_identifier_list.serialize_query(
            value["read_replica_identifiers"],
            pairs,
            f"{key_prefix}ReadReplicaIdentifiers",
        )
    if "db_cluster_members" in value:
        import capo_neptune.types.db_cluster_member_list

        capo_neptune.types.db_cluster_member_list.serialize_query(
            value["db_cluster_members"], pairs, f"{key_prefix}DBClusterMembers"
        )
    if "vpc_security_groups" in value:
        import capo_neptune.types.vpc_security_group_membership_list

        capo_neptune.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_groups"], pairs, f"{key_prefix}VpcSecurityGroups"
        )
    if "hosted_zone_id" in value:
        pairs.append((f"{key_prefix}HostedZoneId", str(value["hosted_zone_id"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "db_cluster_resource_id" in value:
        pairs.append(
            (f"{key_prefix}DbClusterResourceId", str(value["db_cluster_resource_id"]))
        )
    if "db_cluster_arn" in value:
        pairs.append((f"{key_prefix}DBClusterArn", str(value["db_cluster_arn"])))
    if "associated_roles" in value:
        import capo_neptune.types.db_cluster_roles

        capo_neptune.types.db_cluster_roles.serialize_query(
            value["associated_roles"], pairs, f"{key_prefix}AssociatedRoles"
        )
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "clone_group_id" in value:
        pairs.append((f"{key_prefix}CloneGroupId", str(value["clone_group_id"])))
    if "cluster_create_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "enabled_cloudwatch_logs_exports" in value:
        import capo_neptune.types.log_type_list

        capo_neptune.types.log_type_list.serialize_query(
            value["enabled_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnabledCloudwatchLogsExports",
        )
    if "pending_modified_values" in value:
        import capo_neptune.types.cluster_pending_modified_values

        capo_neptune.types.cluster_pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "cross_account_clone" in value:
        pairs.append(
            (
                f"{key_prefix}CrossAccountClone",
                "true" if value["cross_account_clone"] else "false",
            )
        )
    if "automatic_restart_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["automatic_restart_time"], pairs, f"{key_prefix}AutomaticRestartTime"
        )
    if "serverless_v2_scaling_configuration" in value:
        import capo_neptune.types.serverless_v2_scaling_configuration_info

        capo_neptune.types.serverless_v2_scaling_configuration_info.serialize_query(
            value["serverless_v2_scaling_configuration"],
            pairs,
            f"{key_prefix}ServerlessV2ScalingConfiguration",
        )
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "io_optimized_next_allowed_modification_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["io_optimized_next_allowed_modification_time"],
            pairs,
            f"{key_prefix}IOOptimizedNextAllowedModificationTime",
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))


def deserialize_query(el: Element) -> DBCluster:
    out: DBCluster = {}  # type: ignore[typeddict-item]
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_neptune.types.availability_zones

        out["availability_zones"] = (
            capo_neptune.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_db_cluster_parameter_group = el.find("DBClusterParameterGroup")
    if child_db_cluster_parameter_group is not None:
        out["db_cluster_parameter_group"] = str(
            child_db_cluster_parameter_group.text or ""
        )
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        out["db_subnet_group"] = str(child_db_subnet_group.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_percent_progress = el.find("PercentProgress")
    if child_percent_progress is not None:
        out["percent_progress"] = str(child_percent_progress.text or "")
    child_earliest_restorable_time = el.find("EarliestRestorableTime")
    if child_earliest_restorable_time is not None:
        import capo_neptune.types.t_stamp

        out["earliest_restorable_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_earliest_restorable_time
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_reader_endpoint = el.find("ReaderEndpoint")
    if child_reader_endpoint is not None:
        out["reader_endpoint"] = str(child_reader_endpoint.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_latest_restorable_time = el.find("LatestRestorableTime")
    if child_latest_restorable_time is not None:
        import capo_neptune.types.t_stamp

        out["latest_restorable_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_latest_restorable_time
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_db_cluster_option_group_memberships = el.find(
        "DBClusterOptionGroupMemberships"
    )
    if child_db_cluster_option_group_memberships is not None:
        import capo_neptune.types.db_cluster_option_group_memberships

        out["db_cluster_option_group_memberships"] = (
            capo_neptune.types.db_cluster_option_group_memberships.deserialize_query(
                child_db_cluster_option_group_memberships
            )
        )
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_replication_source_identifier = el.find("ReplicationSourceIdentifier")
    if child_replication_source_identifier is not None:
        out["replication_source_identifier"] = str(
            child_replication_source_identifier.text or ""
        )
    child_read_replica_identifiers = el.find("ReadReplicaIdentifiers")
    if child_read_replica_identifiers is not None:
        import capo_neptune.types.read_replica_identifier_list

        out["read_replica_identifiers"] = (
            capo_neptune.types.read_replica_identifier_list.deserialize_query(
                child_read_replica_identifiers
            )
        )
    child_db_cluster_members = el.find("DBClusterMembers")
    if child_db_cluster_members is not None:
        import capo_neptune.types.db_cluster_member_list

        out["db_cluster_members"] = (
            capo_neptune.types.db_cluster_member_list.deserialize_query(
                child_db_cluster_members
            )
        )
    child_vpc_security_groups = el.find("VpcSecurityGroups")
    if child_vpc_security_groups is not None:
        import capo_neptune.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            capo_neptune.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_groups
            )
        )
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_db_cluster_resource_id = el.find("DbClusterResourceId")
    if child_db_cluster_resource_id is not None:
        out["db_cluster_resource_id"] = str(child_db_cluster_resource_id.text or "")
    child_db_cluster_arn = el.find("DBClusterArn")
    if child_db_cluster_arn is not None:
        out["db_cluster_arn"] = str(child_db_cluster_arn.text or "")
    child_associated_roles = el.find("AssociatedRoles")
    if child_associated_roles is not None:
        import capo_neptune.types.db_cluster_roles

        out["associated_roles"] = capo_neptune.types.db_cluster_roles.deserialize_query(
            child_associated_roles
        )
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_clone_group_id = el.find("CloneGroupId")
    if child_clone_group_id is not None:
        out["clone_group_id"] = str(child_clone_group_id.text or "")
    child_cluster_create_time = el.find("ClusterCreateTime")
    if child_cluster_create_time is not None:
        import capo_neptune.types.t_stamp

        out["cluster_create_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_enabled_cloudwatch_logs_exports = el.find("EnabledCloudwatchLogsExports")
    if child_enabled_cloudwatch_logs_exports is not None:
        import capo_neptune.types.log_type_list

        out["enabled_cloudwatch_logs_exports"] = (
            capo_neptune.types.log_type_list.deserialize_query(
                child_enabled_cloudwatch_logs_exports
            )
        )
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_neptune.types.cluster_pending_modified_values

        out["pending_modified_values"] = (
            capo_neptune.types.cluster_pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_cross_account_clone = el.find("CrossAccountClone")
    if child_cross_account_clone is not None:
        out["cross_account_clone"] = (
            child_cross_account_clone.text or ""
        ).lower() == "true"
    child_automatic_restart_time = el.find("AutomaticRestartTime")
    if child_automatic_restart_time is not None:
        import capo_neptune.types.t_stamp

        out["automatic_restart_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_automatic_restart_time
        )
    child_serverless_v2_scaling_configuration = el.find(
        "ServerlessV2ScalingConfiguration"
    )
    if child_serverless_v2_scaling_configuration is not None:
        import capo_neptune.types.serverless_v2_scaling_configuration_info

        out["serverless_v2_scaling_configuration"] = (
            capo_neptune.types.serverless_v2_scaling_configuration_info.deserialize_query(
                child_serverless_v2_scaling_configuration
            )
        )
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_io_optimized_next_allowed_modification_time = el.find(
        "IOOptimizedNextAllowedModificationTime"
    )
    if child_io_optimized_next_allowed_modification_time is not None:
        import capo_neptune.types.t_stamp

        out["io_optimized_next_allowed_modification_time"] = (
            capo_neptune.types.t_stamp.deserialize_query(
                child_io_optimized_next_allowed_modification_time
            )
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    return out

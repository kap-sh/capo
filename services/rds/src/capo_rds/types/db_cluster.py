"""Generated from Smithy shape ``com.amazonaws.rds#DBCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.activity_stream_mode
    import capo_rds.types.activity_stream_status
    import capo_rds.types.availability_zones
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.certificate_details
    import capo_rds.types.cluster_pending_modified_values
    import capo_rds.types.cluster_scalability_type
    import capo_rds.types.database_insights_mode
    import capo_rds.types.db_cluster_member_list
    import capo_rds.types.db_cluster_option_group_memberships
    import capo_rds.types.db_cluster_roles
    import capo_rds.types.db_cluster_status_info_list
    import capo_rds.types.domain_membership_list
    import capo_rds.types.global_cluster_identifier
    import capo_rds.types.integer_optional
    import capo_rds.types.limitless_database
    import capo_rds.types.local_write_forwarding_status
    import capo_rds.types.log_type_list
    import capo_rds.types.long_optional
    import capo_rds.types.master_user_secret
    import capo_rds.types.rds_custom_cluster_configuration
    import capo_rds.types.read_replica_identifier_list
    import capo_rds.types.scaling_configuration_info
    import capo_rds.types.serverless_v2_scaling_configuration_info
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list
    import capo_rds.types.upgrade_rollout_order
    import capo_rds.types.vpc_security_group_membership_list
    import capo_rds.types.write_forwarding_status


class DBCluster(TypedDict, closed=True):
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p> <code>AllocatedStorage</code> specifies the allocated storage size in gibibytes (GiB). For Aurora, <code>AllocatedStorage</code> can vary because Aurora DB cluster storage size adjusts as needed.</p>"""
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>The list of Availability Zones (AZs) where instances in the DB cluster can be created.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automatic DB snapshots are retained.</p>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>If present, specifies the name of the character set that this cluster is associated with.</p>"""
    database_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the initial database that was specified for the DB cluster when it was created, if one was provided. This same name is returned for the life of the DB cluster.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied identifier for the DB cluster. This identifier is the unique key that identifies a DB cluster.</p>"""
    db_cluster_parameter_group: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group for the DB cluster.</p>"""
    db_subnet_group: NotRequired["capo_rds.types.string.String"]
    """<p>Information about the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The current state of this DB cluster.</p>"""
    percent_progress: NotRequired["capo_rds.types.string.String"]
    """<p>The progress of the operation as a percentage.</p>"""
    earliest_restorable_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The earliest time to which a database can be restored with point-in-time restore.</p>"""
    endpoint: NotRequired["capo_rds.types.string.String"]
    """<p>The connection endpoint for the primary instance of the DB cluster.</p>"""
    reader_endpoint: NotRequired["capo_rds.types.string.String"]
    """<p>The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Aurora Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Aurora distributes the connection requests among the Aurora Replicas in the DB cluster. This functionality can help balance your read workload across multiple Aurora Replicas in your DB cluster.</p> <p>If a failover occurs, and the Aurora Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Aurora Replicas in the cluster, you can then reconnect to the reader endpoint.</p>"""
    custom_endpoints: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The custom endpoints associated with the DB cluster.</p>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB cluster has instances in multiple Availability Zones.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine used for this DB cluster.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine.</p>"""
    latest_restorable_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The latest time to which a database can be restored with point-in-time restore.</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port that the database engine is listening on.</p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master username for the DB cluster.</p>"""
    db_cluster_option_group_memberships: NotRequired[
        "capo_rds.types.db_cluster_option_group_memberships.DBClusterOptionGroupMemberships"
    ]
    """<p>The list of option group memberships for this DB cluster.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>"""
    upgrade_rollout_order: NotRequired[
        "capo_rds.types.upgrade_rollout_order.UpgradeRolloutOrder"
    ]
    """<p>This data type represents the order in which the clusters are upgraded.</p> <ul> <li> <p>[first] - Typically used for development or testing environments.</p> </li> <li> <p>[second] - Default order for resources not specifically configured.</p> </li> <li> <p>[last] - Usually reserved for production environments.</p> </li> </ul>"""
    replication_source_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the source DB cluster if this DB cluster is a read replica.</p>"""
    read_replica_identifiers: NotRequired[
        "capo_rds.types.read_replica_identifier_list.ReadReplicaIdentifierList"
    ]
    """<p>Contains one or more identifiers of the read replicas associated with this DB cluster.</p>"""
    status_infos: NotRequired[
        "capo_rds.types.db_cluster_status_info_list.DBClusterStatusInfoList"
    ]
    """<p>Reserved for future use.</p>"""
    db_cluster_members: NotRequired[
        "capo_rds.types.db_cluster_member_list.DBClusterMemberList"
    ]
    """<p>The list of DB instances that make up the DB cluster.</p>"""
    vpc_security_groups: NotRequired[
        "capo_rds.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>The list of VPC security groups that the DB cluster belongs to.</p>"""
    hosted_zone_id: NotRequired["capo_rds.types.string.String"]
    """<p>The ID that Amazon Route 53 assigns when you create a hosted zone.</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB cluster is encrypted.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the DB cluster. Possible values:</p> <ul> <li> <p> <code>none</code> - The DB cluster is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The DB cluster is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The DB cluster is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>If <code>StorageEncrypted</code> is enabled, the Amazon Web Services KMS key identifier for the encrypted DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    db_cluster_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the DB cluster. This identifier is found in Amazon Web Services CloudTrail log entries whenever the KMS key for the DB cluster is accessed.</p>"""
    db_cluster_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB cluster.</p>"""
    associated_roles: NotRequired["capo_rds.types.db_cluster_roles.DBClusterRoles"]
    """<p>A list of the Amazon Web Services Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon Web Services on your behalf.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    clone_group_id: NotRequired["capo_rds.types.string.String"]
    """<p>The ID of the clone group with which the DB cluster is associated. For newly created clusters, the ID is typically null. </p> <p>If you clone a DB cluster when the ID is null, the operation populates the ID value for the source cluster and the clone because both clusters become part of the same clone group. Even if you delete the clone cluster, the clone group ID remains for the lifetime of the source cluster to show that it was used in a cloning operation.</p> <p>For PITR, the clone group ID is inherited from the source cluster. For snapshot restore operations, the clone group ID isn't inherited from the source cluster.</p>"""
    cluster_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when the DB cluster was created, in Universal Coordinated Time (UTC).</p>"""
    earliest_backtrack_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The earliest time to which a DB cluster can be backtracked.</p>"""
    backtrack_window: NotRequired["capo_rds.types.long_optional.LongOptional"]
    """<p>The target backtrack window, in seconds. If this value is set to <code>0</code>, backtracking is disabled for the DB cluster. Otherwise, backtracking is enabled.</p>"""
    backtrack_consumed_change_records: NotRequired[
        "capo_rds.types.long_optional.LongOptional"
    ]
    """<p>The number of change records stored for Backtrack.</p>"""
    enabled_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>A list of log types that this DB cluster is configured to export to CloudWatch Logs.</p> <p>Log types vary by DB engine. For information about the log types for each DB engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html">Amazon RDS Database Log Files</a> in the <i>Amazon Aurora User Guide.</i> </p>"""
    capacity: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The current capacity of an Aurora Serverless v1 DB cluster. The capacity is <code>0</code> (zero) when the cluster is paused.</p> <p>For more information about Aurora Serverless v1, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html">Using Amazon Aurora Serverless v1</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    pending_modified_values: NotRequired[
        "capo_rds.types.cluster_pending_modified_values.ClusterPendingModifiedValues"
    ]
    """<p>Information about pending changes to the DB cluster. This information is returned only when there are pending changes. Specific changes are identified by subelements.</p>"""
    engine_mode: NotRequired["capo_rds.types.string.String"]
    """<p>The DB engine mode of the DB cluster, either <code>provisioned</code> or <code>serverless</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html"> CreateDBCluster</a>.</p>"""
    scaling_configuration_info: NotRequired[
        "capo_rds.types.scaling_configuration_info.ScalingConfigurationInfo"
    ]
    rds_custom_cluster_configuration: NotRequired[
        "capo_rds.types.rds_custom_cluster_configuration.RdsCustomClusterConfiguration"
    ]
    """<p>Reserved for future use.</p>"""
    db_cluster_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the compute and memory capacity class of the DB instance.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type associated with the DB cluster.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The Provisioned IOPS (I/O operations per second) value.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput for the DB cluster. The throughput is automatically set based on the IOPS that you provision, and is not configurable.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    io_optimized_next_allowed_modification_time: NotRequired[
        "capo_rds.types.t_stamp.TStamp"
    ]
    """<p>The next time you can modify the DB cluster to use the <code>aurora-iopt1</code> storage type.</p> <p>This setting is only for Aurora DB clusters.</p>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB cluster is publicly accessible.</p> <p>When the DB cluster is publicly accessible and you connect from outside of the DB cluster's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB cluster, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.</p> <p>For more information, see <a>CreateDBCluster</a>.</p> <p>This setting is only for non-Aurora Multi-AZ DB clusters.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether minor version patches are applied automatically.</p> <p>This setting is for Aurora DB clusters and Multi-AZ DB clusters.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.</p>"""
    http_endpoint_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the HTTP endpoint is enabled for an Aurora DB cluster.</p> <p>When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the DB cluster. You can also query your database from inside the RDS console with the RDS query editor.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html">Using RDS Data API</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    activity_stream_mode: NotRequired[
        "capo_rds.types.activity_stream_mode.ActivityStreamMode"
    ]
    """<p>The mode of the database activity stream. Database events such as a change or access generate an activity stream event. The database session can handle these events either synchronously or asynchronously.</p>"""
    activity_stream_status: NotRequired[
        "capo_rds.types.activity_stream_status.ActivityStreamStatus"
    ]
    """<p>The status of the database activity stream.</p>"""
    activity_stream_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier used for encrypting messages in the database activity stream.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    activity_stream_kinesis_stream_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Amazon Kinesis data stream used for the database activity stream.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether tags are copied from the DB cluster to snapshots of the DB cluster.</p>"""
    cross_account_clone: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB cluster is a clone of a DB cluster owned by a different Amazon Web Services account.</p>"""
    domain_memberships: NotRequired[
        "capo_rds.types.domain_membership_list.DomainMembershipList"
    ]
    """<p>The Active Directory Domain membership records associated with the DB cluster.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    global_cluster_identifier: NotRequired[
        "capo_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database cluster.</p>"""
    global_write_forwarding_status: NotRequired[
        "capo_rds.types.write_forwarding_status.WriteForwardingStatus"
    ]
    """<p>The status of write forwarding for a secondary cluster in an Aurora global database.</p>"""
    global_write_forwarding_requested: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether write forwarding is enabled for a secondary cluster in an Aurora global database. Because write forwarding takes time to enable, check the value of <code>GlobalWriteForwardingStatus</code> to confirm that the request has completed before using the write forwarding feature for this cluster.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>This setting is only for Aurora DB clusters.</p> <p>Valid Values: <code>IPV4 | DUAL</code> </p>"""
    automatic_restart_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when a stopped DB cluster is restarted automatically.</p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_rds.types.serverless_v2_scaling_configuration_info.ServerlessV2ScalingConfigurationInfo"
    ]
    serverless_v2_platform_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the Aurora Serverless V2 platform used by the DB cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html">Using Aurora Serverless v2</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster.</p> <p>This setting is only for -Aurora DB clusters and Multi-AZ DB clusters.</p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.</p> <p>This setting is only for Aurora DB clusters and Multi-AZ DB clusters.</p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>The mode of Database Insights that is enabled for the DB cluster.</p>"""
    performance_insights_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether Performance Insights is enabled for the DB cluster.</p> <p>This setting is only for Aurora DB clusters and Multi-AZ DB clusters.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>This setting is only for Aurora DB clusters and Multi-AZ DB clusters.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>This setting is only for Aurora DB clusters and Multi-AZ DB clusters.</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p>"""
    db_system_id: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""
    master_user_secret: NotRequired[
        "capo_rds.types.master_user_secret.MasterUserSecret"
    ]
    """<p>The secret managed by RDS in Amazon Web Services Secrets Manager for the master user password.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon Aurora User Guide.</i> </p>"""
    local_write_forwarding_status: NotRequired[
        "capo_rds.types.local_write_forwarding_status.LocalWriteForwardingStatus"
    ]
    """<p>Indicates whether an Aurora DB cluster has in-cluster write forwarding enabled, not enabled, requested, or is in the process of enabling it.</p>"""
    aws_backup_recovery_point_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.</p>"""
    limitless_database: NotRequired[
        "capo_rds.types.limitless_database.LimitlessDatabase"
    ]
    """<p>The details for Aurora Limitless Database.</p>"""
    cluster_scalability_type: NotRequired[
        "capo_rds.types.cluster_scalability_type.ClusterScalabilityType"
    ]
    """<p>The scalability mode of the Aurora DB cluster. When set to <code>limitless</code>, the cluster operates as an Aurora Limitless Database. When set to <code>standard</code> (the default), the cluster uses normal DB instance creation.</p>"""
    certificate_details: NotRequired[
        "capo_rds.types.certificate_details.CertificateDetails"
    ]
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for the DB cluster.</p> <p>For more information, see CreateDBCluster.</p>"""
    vpc_networking_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the DB cluster uses VPC-based networking.</p> <p>This setting is applicable only for Aurora PostgreSQL clusters created through express configuration.</p>"""
    internet_access_gateway_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the DB cluster has internet-based connectivity enabled through an internet access gateway.</p> <p>This setting is applicable only for Aurora PostgreSQL clusters created through express configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBCluster, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "availability_zones" in value:
        import capo_rds.types.availability_zones

        capo_rds.types.availability_zones.serialize_query(
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
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["earliest_restorable_time"],
            pairs,
            f"{key_prefix}EarliestRestorableTime",
        )
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "reader_endpoint" in value:
        pairs.append((f"{key_prefix}ReaderEndpoint", str(value["reader_endpoint"])))
    if "custom_endpoints" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["custom_endpoints"], pairs, f"{key_prefix}CustomEndpoints"
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "latest_restorable_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["latest_restorable_time"], pairs, f"{key_prefix}LatestRestorableTime"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "db_cluster_option_group_memberships" in value:
        import capo_rds.types.db_cluster_option_group_memberships

        capo_rds.types.db_cluster_option_group_memberships.serialize_query(
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
    if "upgrade_rollout_order" in value:
        import capo_rds.types.upgrade_rollout_order

        capo_rds.types.upgrade_rollout_order.serialize_query(
            value["upgrade_rollout_order"], pairs, f"{key_prefix}UpgradeRolloutOrder"
        )
    if "replication_source_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}ReplicationSourceIdentifier",
                str(value["replication_source_identifier"]),
            )
        )
    if "read_replica_identifiers" in value:
        import capo_rds.types.read_replica_identifier_list

        capo_rds.types.read_replica_identifier_list.serialize_query(
            value["read_replica_identifiers"],
            pairs,
            f"{key_prefix}ReadReplicaIdentifiers",
        )
    if "status_infos" in value:
        import capo_rds.types.db_cluster_status_info_list

        capo_rds.types.db_cluster_status_info_list.serialize_query(
            value["status_infos"], pairs, f"{key_prefix}StatusInfos"
        )
    if "db_cluster_members" in value:
        import capo_rds.types.db_cluster_member_list

        capo_rds.types.db_cluster_member_list.serialize_query(
            value["db_cluster_members"], pairs, f"{key_prefix}DBClusterMembers"
        )
    if "vpc_security_groups" in value:
        import capo_rds.types.vpc_security_group_membership_list

        capo_rds.types.vpc_security_group_membership_list.serialize_query(
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
    if "storage_encryption_type" in value:
        import capo_rds.types.storage_encryption_type

        capo_rds.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
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
        import capo_rds.types.db_cluster_roles

        capo_rds.types.db_cluster_roles.serialize_query(
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
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "earliest_backtrack_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["earliest_backtrack_time"],
            pairs,
            f"{key_prefix}EarliestBacktrackTime",
        )
    if "backtrack_window" in value:
        pairs.append((f"{key_prefix}BacktrackWindow", str(value["backtrack_window"])))
    if "backtrack_consumed_change_records" in value:
        pairs.append(
            (
                f"{key_prefix}BacktrackConsumedChangeRecords",
                str(value["backtrack_consumed_change_records"]),
            )
        )
    if "enabled_cloudwatch_logs_exports" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["enabled_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnabledCloudwatchLogsExports",
        )
    if "capacity" in value:
        pairs.append((f"{key_prefix}Capacity", str(value["capacity"])))
    if "pending_modified_values" in value:
        import capo_rds.types.cluster_pending_modified_values

        capo_rds.types.cluster_pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "engine_mode" in value:
        pairs.append((f"{key_prefix}EngineMode", str(value["engine_mode"])))
    if "scaling_configuration_info" in value:
        import capo_rds.types.scaling_configuration_info

        capo_rds.types.scaling_configuration_info.serialize_query(
            value["scaling_configuration_info"],
            pairs,
            f"{key_prefix}ScalingConfigurationInfo",
        )
    if "rds_custom_cluster_configuration" in value:
        import capo_rds.types.rds_custom_cluster_configuration

        capo_rds.types.rds_custom_cluster_configuration.serialize_query(
            value["rds_custom_cluster_configuration"],
            pairs,
            f"{key_prefix}RdsCustomClusterConfiguration",
        )
    if "db_cluster_instance_class" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterInstanceClass",
                str(value["db_cluster_instance_class"]),
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "io_optimized_next_allowed_modification_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["io_optimized_next_allowed_modification_time"],
            pairs,
            f"{key_prefix}IOOptimizedNextAllowedModificationTime",
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "http_endpoint_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}HttpEndpointEnabled",
                "true" if value["http_endpoint_enabled"] else "false",
            )
        )
    if "activity_stream_mode" in value:
        import capo_rds.types.activity_stream_mode

        capo_rds.types.activity_stream_mode.serialize_query(
            value["activity_stream_mode"], pairs, f"{key_prefix}ActivityStreamMode"
        )
    if "activity_stream_status" in value:
        import capo_rds.types.activity_stream_status

        capo_rds.types.activity_stream_status.serialize_query(
            value["activity_stream_status"], pairs, f"{key_prefix}ActivityStreamStatus"
        )
    if "activity_stream_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}ActivityStreamKmsKeyId",
                str(value["activity_stream_kms_key_id"]),
            )
        )
    if "activity_stream_kinesis_stream_name" in value:
        pairs.append(
            (
                f"{key_prefix}ActivityStreamKinesisStreamName",
                str(value["activity_stream_kinesis_stream_name"]),
            )
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "cross_account_clone" in value:
        pairs.append(
            (
                f"{key_prefix}CrossAccountClone",
                "true" if value["cross_account_clone"] else "false",
            )
        )
    if "domain_memberships" in value:
        import capo_rds.types.domain_membership_list

        capo_rds.types.domain_membership_list.serialize_query(
            value["domain_memberships"], pairs, f"{key_prefix}DomainMemberships"
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "global_write_forwarding_status" in value:
        import capo_rds.types.write_forwarding_status

        capo_rds.types.write_forwarding_status.serialize_query(
            value["global_write_forwarding_status"],
            pairs,
            f"{key_prefix}GlobalWriteForwardingStatus",
        )
    if "global_write_forwarding_requested" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalWriteForwardingRequested",
                "true" if value["global_write_forwarding_requested"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "automatic_restart_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["automatic_restart_time"], pairs, f"{key_prefix}AutomaticRestartTime"
        )
    if "serverless_v2_scaling_configuration" in value:
        import capo_rds.types.serverless_v2_scaling_configuration_info

        capo_rds.types.serverless_v2_scaling_configuration_info.serialize_query(
            value["serverless_v2_scaling_configuration"],
            pairs,
            f"{key_prefix}ServerlessV2ScalingConfiguration",
        )
    if "serverless_v2_platform_version" in value:
        pairs.append(
            (
                f"{key_prefix}ServerlessV2PlatformVersion",
                str(value["serverless_v2_platform_version"]),
            )
        )
    if "monitoring_interval" in value:
        pairs.append(
            (f"{key_prefix}MonitoringInterval", str(value["monitoring_interval"]))
        )
    if "monitoring_role_arn" in value:
        pairs.append(
            (f"{key_prefix}MonitoringRoleArn", str(value["monitoring_role_arn"]))
        )
    if "database_insights_mode" in value:
        import capo_rds.types.database_insights_mode

        capo_rds.types.database_insights_mode.serialize_query(
            value["database_insights_mode"], pairs, f"{key_prefix}DatabaseInsightsMode"
        )
    if "performance_insights_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsEnabled",
                "true" if value["performance_insights_enabled"] else "false",
            )
        )
    if "performance_insights_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsKMSKeyId",
                str(value["performance_insights_kms_key_id"]),
            )
        )
    if "performance_insights_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsRetentionPeriod",
                str(value["performance_insights_retention_period"]),
            )
        )
    if "db_system_id" in value:
        pairs.append((f"{key_prefix}DBSystemId", str(value["db_system_id"])))
    if "master_user_secret" in value:
        import capo_rds.types.master_user_secret

        capo_rds.types.master_user_secret.serialize_query(
            value["master_user_secret"], pairs, f"{key_prefix}MasterUserSecret"
        )
    if "local_write_forwarding_status" in value:
        import capo_rds.types.local_write_forwarding_status

        capo_rds.types.local_write_forwarding_status.serialize_query(
            value["local_write_forwarding_status"],
            pairs,
            f"{key_prefix}LocalWriteForwardingStatus",
        )
    if "aws_backup_recovery_point_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AwsBackupRecoveryPointArn",
                str(value["aws_backup_recovery_point_arn"]),
            )
        )
    if "limitless_database" in value:
        import capo_rds.types.limitless_database

        capo_rds.types.limitless_database.serialize_query(
            value["limitless_database"], pairs, f"{key_prefix}LimitlessDatabase"
        )
    if "cluster_scalability_type" in value:
        import capo_rds.types.cluster_scalability_type

        capo_rds.types.cluster_scalability_type.serialize_query(
            value["cluster_scalability_type"],
            pairs,
            f"{key_prefix}ClusterScalabilityType",
        )
    if "certificate_details" in value:
        import capo_rds.types.certificate_details

        capo_rds.types.certificate_details.serialize_query(
            value["certificate_details"], pairs, f"{key_prefix}CertificateDetails"
        )
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )
    if "vpc_networking_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}VPCNetworkingEnabled",
                "true" if value["vpc_networking_enabled"] else "false",
            )
        )
    if "internet_access_gateway_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}InternetAccessGatewayEnabled",
                "true" if value["internet_access_gateway_enabled"] else "false",
            )
        )


def deserialize_query(el: Element) -> DBCluster:
    out: DBCluster = {}  # type: ignore[typeddict-item]
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_rds.types.availability_zones

        out["availability_zones"] = capo_rds.types.availability_zones.deserialize_query(
            child_availability_zones
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
        import capo_rds.types.t_stamp

        out["earliest_restorable_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_earliest_restorable_time
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_reader_endpoint = el.find("ReaderEndpoint")
    if child_reader_endpoint is not None:
        out["reader_endpoint"] = str(child_reader_endpoint.text or "")
    child_custom_endpoints = el.find("CustomEndpoints")
    if child_custom_endpoints is not None:
        import capo_rds.types.string_list

        out["custom_endpoints"] = capo_rds.types.string_list.deserialize_query(
            child_custom_endpoints
        )
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
        import capo_rds.types.t_stamp

        out["latest_restorable_time"] = capo_rds.types.t_stamp.deserialize_query(
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
        import capo_rds.types.db_cluster_option_group_memberships

        out["db_cluster_option_group_memberships"] = (
            capo_rds.types.db_cluster_option_group_memberships.deserialize_query(
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
    child_upgrade_rollout_order = el.find("UpgradeRolloutOrder")
    if child_upgrade_rollout_order is not None:
        import capo_rds.types.upgrade_rollout_order

        out["upgrade_rollout_order"] = (
            capo_rds.types.upgrade_rollout_order.deserialize_query(
                child_upgrade_rollout_order
            )
        )
    child_replication_source_identifier = el.find("ReplicationSourceIdentifier")
    if child_replication_source_identifier is not None:
        out["replication_source_identifier"] = str(
            child_replication_source_identifier.text or ""
        )
    child_read_replica_identifiers = el.find("ReadReplicaIdentifiers")
    if child_read_replica_identifiers is not None:
        import capo_rds.types.read_replica_identifier_list

        out["read_replica_identifiers"] = (
            capo_rds.types.read_replica_identifier_list.deserialize_query(
                child_read_replica_identifiers
            )
        )
    child_status_infos = el.find("StatusInfos")
    if child_status_infos is not None:
        import capo_rds.types.db_cluster_status_info_list

        out["status_infos"] = (
            capo_rds.types.db_cluster_status_info_list.deserialize_query(
                child_status_infos
            )
        )
    child_db_cluster_members = el.find("DBClusterMembers")
    if child_db_cluster_members is not None:
        import capo_rds.types.db_cluster_member_list

        out["db_cluster_members"] = (
            capo_rds.types.db_cluster_member_list.deserialize_query(
                child_db_cluster_members
            )
        )
    child_vpc_security_groups = el.find("VpcSecurityGroups")
    if child_vpc_security_groups is not None:
        import capo_rds.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            capo_rds.types.vpc_security_group_membership_list.deserialize_query(
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
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_rds.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_rds.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
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
        import capo_rds.types.db_cluster_roles

        out["associated_roles"] = capo_rds.types.db_cluster_roles.deserialize_query(
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
        import capo_rds.types.t_stamp

        out["cluster_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_earliest_backtrack_time = el.find("EarliestBacktrackTime")
    if child_earliest_backtrack_time is not None:
        import capo_rds.types.t_stamp

        out["earliest_backtrack_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_earliest_backtrack_time
        )
    child_backtrack_window = el.find("BacktrackWindow")
    if child_backtrack_window is not None:
        out["backtrack_window"] = int(child_backtrack_window.text or "")
    child_backtrack_consumed_change_records = el.find("BacktrackConsumedChangeRecords")
    if child_backtrack_consumed_change_records is not None:
        out["backtrack_consumed_change_records"] = int(
            child_backtrack_consumed_change_records.text or ""
        )
    child_enabled_cloudwatch_logs_exports = el.find("EnabledCloudwatchLogsExports")
    if child_enabled_cloudwatch_logs_exports is not None:
        import capo_rds.types.log_type_list

        out["enabled_cloudwatch_logs_exports"] = (
            capo_rds.types.log_type_list.deserialize_query(
                child_enabled_cloudwatch_logs_exports
            )
        )
    child_capacity = el.find("Capacity")
    if child_capacity is not None:
        out["capacity"] = int(child_capacity.text or "")
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_rds.types.cluster_pending_modified_values

        out["pending_modified_values"] = (
            capo_rds.types.cluster_pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_engine_mode = el.find("EngineMode")
    if child_engine_mode is not None:
        out["engine_mode"] = str(child_engine_mode.text or "")
    child_scaling_configuration_info = el.find("ScalingConfigurationInfo")
    if child_scaling_configuration_info is not None:
        import capo_rds.types.scaling_configuration_info

        out["scaling_configuration_info"] = (
            capo_rds.types.scaling_configuration_info.deserialize_query(
                child_scaling_configuration_info
            )
        )
    child_rds_custom_cluster_configuration = el.find("RdsCustomClusterConfiguration")
    if child_rds_custom_cluster_configuration is not None:
        import capo_rds.types.rds_custom_cluster_configuration

        out["rds_custom_cluster_configuration"] = (
            capo_rds.types.rds_custom_cluster_configuration.deserialize_query(
                child_rds_custom_cluster_configuration
            )
        )
    child_db_cluster_instance_class = el.find("DBClusterInstanceClass")
    if child_db_cluster_instance_class is not None:
        out["db_cluster_instance_class"] = str(
            child_db_cluster_instance_class.text or ""
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_io_optimized_next_allowed_modification_time = el.find(
        "IOOptimizedNextAllowedModificationTime"
    )
    if child_io_optimized_next_allowed_modification_time is not None:
        import capo_rds.types.t_stamp

        out["io_optimized_next_allowed_modification_time"] = (
            capo_rds.types.t_stamp.deserialize_query(
                child_io_optimized_next_allowed_modification_time
            )
        )
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_http_endpoint_enabled = el.find("HttpEndpointEnabled")
    if child_http_endpoint_enabled is not None:
        out["http_endpoint_enabled"] = (
            child_http_endpoint_enabled.text or ""
        ).lower() == "true"
    child_activity_stream_mode = el.find("ActivityStreamMode")
    if child_activity_stream_mode is not None:
        import capo_rds.types.activity_stream_mode

        out["activity_stream_mode"] = (
            capo_rds.types.activity_stream_mode.deserialize_query(
                child_activity_stream_mode
            )
        )
    child_activity_stream_status = el.find("ActivityStreamStatus")
    if child_activity_stream_status is not None:
        import capo_rds.types.activity_stream_status

        out["activity_stream_status"] = (
            capo_rds.types.activity_stream_status.deserialize_query(
                child_activity_stream_status
            )
        )
    child_activity_stream_kms_key_id = el.find("ActivityStreamKmsKeyId")
    if child_activity_stream_kms_key_id is not None:
        out["activity_stream_kms_key_id"] = str(
            child_activity_stream_kms_key_id.text or ""
        )
    child_activity_stream_kinesis_stream_name = el.find(
        "ActivityStreamKinesisStreamName"
    )
    if child_activity_stream_kinesis_stream_name is not None:
        out["activity_stream_kinesis_stream_name"] = str(
            child_activity_stream_kinesis_stream_name.text or ""
        )
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_cross_account_clone = el.find("CrossAccountClone")
    if child_cross_account_clone is not None:
        out["cross_account_clone"] = (
            child_cross_account_clone.text or ""
        ).lower() == "true"
    child_domain_memberships = el.find("DomainMemberships")
    if child_domain_memberships is not None:
        import capo_rds.types.domain_membership_list

        out["domain_memberships"] = (
            capo_rds.types.domain_membership_list.deserialize_query(
                child_domain_memberships
            )
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_global_write_forwarding_status = el.find("GlobalWriteForwardingStatus")
    if child_global_write_forwarding_status is not None:
        import capo_rds.types.write_forwarding_status

        out["global_write_forwarding_status"] = (
            capo_rds.types.write_forwarding_status.deserialize_query(
                child_global_write_forwarding_status
            )
        )
    child_global_write_forwarding_requested = el.find("GlobalWriteForwardingRequested")
    if child_global_write_forwarding_requested is not None:
        out["global_write_forwarding_requested"] = (
            child_global_write_forwarding_requested.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_automatic_restart_time = el.find("AutomaticRestartTime")
    if child_automatic_restart_time is not None:
        import capo_rds.types.t_stamp

        out["automatic_restart_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_automatic_restart_time
        )
    child_serverless_v2_scaling_configuration = el.find(
        "ServerlessV2ScalingConfiguration"
    )
    if child_serverless_v2_scaling_configuration is not None:
        import capo_rds.types.serverless_v2_scaling_configuration_info

        out["serverless_v2_scaling_configuration"] = (
            capo_rds.types.serverless_v2_scaling_configuration_info.deserialize_query(
                child_serverless_v2_scaling_configuration
            )
        )
    child_serverless_v2_platform_version = el.find("ServerlessV2PlatformVersion")
    if child_serverless_v2_platform_version is not None:
        out["serverless_v2_platform_version"] = str(
            child_serverless_v2_platform_version.text or ""
        )
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
    child_database_insights_mode = el.find("DatabaseInsightsMode")
    if child_database_insights_mode is not None:
        import capo_rds.types.database_insights_mode

        out["database_insights_mode"] = (
            capo_rds.types.database_insights_mode.deserialize_query(
                child_database_insights_mode
            )
        )
    child_performance_insights_enabled = el.find("PerformanceInsightsEnabled")
    if child_performance_insights_enabled is not None:
        out["performance_insights_enabled"] = (
            child_performance_insights_enabled.text or ""
        ).lower() == "true"
    child_performance_insights_kms_key_id = el.find("PerformanceInsightsKMSKeyId")
    if child_performance_insights_kms_key_id is not None:
        out["performance_insights_kms_key_id"] = str(
            child_performance_insights_kms_key_id.text or ""
        )
    child_performance_insights_retention_period = el.find(
        "PerformanceInsightsRetentionPeriod"
    )
    if child_performance_insights_retention_period is not None:
        out["performance_insights_retention_period"] = int(
            child_performance_insights_retention_period.text or ""
        )
    child_db_system_id = el.find("DBSystemId")
    if child_db_system_id is not None:
        out["db_system_id"] = str(child_db_system_id.text or "")
    child_master_user_secret = el.find("MasterUserSecret")
    if child_master_user_secret is not None:
        import capo_rds.types.master_user_secret

        out["master_user_secret"] = capo_rds.types.master_user_secret.deserialize_query(
            child_master_user_secret
        )
    child_local_write_forwarding_status = el.find("LocalWriteForwardingStatus")
    if child_local_write_forwarding_status is not None:
        import capo_rds.types.local_write_forwarding_status

        out["local_write_forwarding_status"] = (
            capo_rds.types.local_write_forwarding_status.deserialize_query(
                child_local_write_forwarding_status
            )
        )
    child_aws_backup_recovery_point_arn = el.find("AwsBackupRecoveryPointArn")
    if child_aws_backup_recovery_point_arn is not None:
        out["aws_backup_recovery_point_arn"] = str(
            child_aws_backup_recovery_point_arn.text or ""
        )
    child_limitless_database = el.find("LimitlessDatabase")
    if child_limitless_database is not None:
        import capo_rds.types.limitless_database

        out["limitless_database"] = capo_rds.types.limitless_database.deserialize_query(
            child_limitless_database
        )
    child_cluster_scalability_type = el.find("ClusterScalabilityType")
    if child_cluster_scalability_type is not None:
        import capo_rds.types.cluster_scalability_type

        out["cluster_scalability_type"] = (
            capo_rds.types.cluster_scalability_type.deserialize_query(
                child_cluster_scalability_type
            )
        )
    child_certificate_details = el.find("CertificateDetails")
    if child_certificate_details is not None:
        import capo_rds.types.certificate_details

        out["certificate_details"] = (
            capo_rds.types.certificate_details.deserialize_query(
                child_certificate_details
            )
        )
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_vpc_networking_enabled = el.find("VPCNetworkingEnabled")
    if child_vpc_networking_enabled is not None:
        out["vpc_networking_enabled"] = (
            child_vpc_networking_enabled.text or ""
        ).lower() == "true"
    child_internet_access_gateway_enabled = el.find("InternetAccessGatewayEnabled")
    if child_internet_access_gateway_enabled is not None:
        out["internet_access_gateway_enabled"] = (
            child_internet_access_gateway_enabled.text or ""
        ).lower() == "true"
    return out

"""Generated from Smithy shape ``com.amazonaws.rds#DBInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.activity_stream_mode
    import capo_rds.types.activity_stream_policy_status
    import capo_rds.types.activity_stream_status
    import capo_rds.types.additional_storage_volumes_output_list
    import capo_rds.types.automation_mode
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.certificate_details
    import capo_rds.types.database_insights_mode
    import capo_rds.types.db_instance_automated_backups_replication_list
    import capo_rds.types.db_instance_roles
    import capo_rds.types.db_instance_status_info_list
    import capo_rds.types.db_parameter_group_status_list
    import capo_rds.types.db_security_group_membership_list
    import capo_rds.types.db_subnet_group
    import capo_rds.types.domain_membership_list
    import capo_rds.types.endpoint
    import capo_rds.types.integer
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.master_user_secret
    import capo_rds.types.option_group_membership_list
    import capo_rds.types.pending_modified_values
    import capo_rds.types.processor_feature_list
    import capo_rds.types.read_replica_db_cluster_identifier_list
    import capo_rds.types.read_replica_db_instance_identifier_list
    import capo_rds.types.replica_mode
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list
    import capo_rds.types.upgrade_rollout_order
    import capo_rds.types.vpc_security_group_membership_list


class DBInstance(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied database identifier. This identifier is the unique key that identifies a DB instance.</p>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the compute and memory capacity class of the DB instance.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine used for this DB instance.</p>"""
    db_instance_status: NotRequired["capo_rds.types.string.String"]
    """<p>The current state of this database.</p> <p>For information about DB instance statuses, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/accessing-monitoring.html#Overview.DBInstance.Status">Viewing DB instance status</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master username for the DB instance.</p>"""
    db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The initial database name that you provided (if required) when you created the DB instance. This name is returned for the life of your DB instance. For an RDS for Oracle CDB instance, the name identifies the PDB rather than the CDB.</p>"""
    endpoint: NotRequired["capo_rds.types.endpoint.Endpoint"]
    """<p>The connection endpoint for the DB instance.</p> <note> <p>The endpoint might not be shown for instances with the status of <code>creating</code>.</p> </note>"""
    allocated_storage: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The amount of storage in gibibytes (GiB) allocated for the DB instance.</p>"""
    instance_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the DB instance was created.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    backup_retention_period: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The number of days for which automatic DB snapshots are retained.</p>"""
    db_security_groups: NotRequired[
        "capo_rds.types.db_security_group_membership_list.DBSecurityGroupMembershipList"
    ]
    """<p>A list of DB security group elements containing <code>DBSecurityGroup.Name</code> and <code>DBSecurityGroup.Status</code> subelements.</p>"""
    vpc_security_groups: NotRequired[
        "capo_rds.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>The list of Amazon EC2 VPC security groups that the DB instance belongs to.</p>"""
    db_parameter_groups: NotRequired[
        "capo_rds.types.db_parameter_group_status_list.DBParameterGroupStatusList"
    ]
    """<p>The list of DB parameter groups applied to this DB instance.</p>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Availability Zone where the DB instance is located.</p>"""
    db_subnet_group: NotRequired["capo_rds.types.db_subnet_group.DBSubnetGroup"]
    """<p>Information about the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.</p>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>"""
    upgrade_rollout_order: NotRequired[
        "capo_rds.types.upgrade_rollout_order.UpgradeRolloutOrder"
    ]
    """<p>This data type represents the order in which the instances are upgraded.</p> <ul> <li> <p>[first] - Typically used for development or testing environments.</p> </li> <li> <p>[second] - Default order for resources not specifically configured.</p> </li> <li> <p>[last] - Usually reserved for production environments.</p> </li> </ul>"""
    pending_modified_values: NotRequired[
        "capo_rds.types.pending_modified_values.PendingModifiedValues"
    ]
    """<p>Information about pending changes to the DB instance. This information is returned only when there are pending changes. Specific changes are identified by subelements.</p>"""
    latest_restorable_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The latest time to which a database in this DB instance can be restored with point-in-time restore.</p>"""
    multi_az: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance is a Multi-AZ deployment. This setting doesn't apply to RDS Custom DB instances.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether minor version patches are applied automatically.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    read_replica_source_db_instance_identifier: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>The identifier of the source DB instance if this DB instance is a read replica.</p>"""
    read_replica_db_instance_identifiers: NotRequired[
        "capo_rds.types.read_replica_db_instance_identifier_list.ReadReplicaDBInstanceIdentifierList"
    ]
    """<p>The identifiers of the read replicas associated with this DB instance.</p>"""
    read_replica_db_cluster_identifiers: NotRequired[
        "capo_rds.types.read_replica_db_cluster_identifier_list.ReadReplicaDBClusterIdentifierList"
    ]
    """<p>The identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a read replica. For example, when you create an Aurora read replica of an RDS for MySQL DB instance, the Aurora MySQL DB cluster for the Aurora read replica is shown. This output doesn't contain information about cross-Region Aurora read replicas.</p> <note> <p>Currently, each RDS DB instance can have only one Aurora read replica.</p> </note>"""
    replica_mode: NotRequired["capo_rds.types.replica_mode.ReplicaMode"]
    """<p>The open mode of a Db2 or an Oracle read replica. The default is <code>open-read-only</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replication.html">Working with replicas for Amazon RDS for Db2</a> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html">Working with read replicas for Amazon RDS for Oracle</a> in the <i>Amazon RDS User Guide</i>. </p> <note> <p>This attribute is only supported in RDS for Db2, RDS for Oracle, and RDS Custom for Oracle.</p> </note>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model information for this DB instance. This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The Provisioned IOPS (I/O operations per second) value for the DB instance.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput for the DB instance.</p> <p>This setting applies only to the <code>gp3</code> storage type.</p>"""
    option_group_memberships: NotRequired[
        "capo_rds.types.option_group_membership_list.OptionGroupMembershipList"
    ]
    """<p>The list of option group memberships for this DB instance.</p>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>If present, specifies the name of the character set that this instance is associated with.</p>"""
    nchar_character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the NCHAR character set for the Oracle DB instance. This character set specifies the Unicode encoding for data stored in table columns of type NCHAR, NCLOB, or NVARCHAR2.</p>"""
    secondary_availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.</p>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p> <p>For more information, see <a>CreateDBInstance</a>.</p>"""
    status_infos: NotRequired[
        "capo_rds.types.db_instance_status_info_list.DBInstanceStatusInfoList"
    ]
    """<p>The status of a read replica. If the DB instance isn't a read replica, the value is blank.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type associated with the DB instance.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the DB instance. Possible values:</p> <ul> <li> <p> <code>none</code> - The DB instance is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The DB instance is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The DB instance is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    tde_credential_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN from the key store with which the instance is associated for TDE encryption.</p>"""
    db_instance_port: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>If the DB instance is a member of a DB cluster, indicates the name of the DB cluster that the DB instance is a member of.</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance is encrypted.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>If <code>StorageEncrypted</code> is enabled, the Amazon Web Services KMS key identifier for the encrypted DB instance.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the DB instance. This identifier is found in Amazon Web Services CloudTrail log entries whenever the Amazon Web Services KMS key for the DB instance is accessed.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the CA certificate for this DB instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    domain_memberships: NotRequired[
        "capo_rds.types.domain_membership_list.DomainMembershipList"
    ]
    """<p>The Active Directory Domain membership records associated with the DB instance.</p>"""
    copy_tags_to_snapshot: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether tags are copied from the DB instance to snapshots of the DB instance.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting. For more information, see <code>DBCluster</code>.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.</p>"""
    enhanced_monitoring_resource_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.</p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.</p>"""
    promotion_tier: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance"> Fault Tolerance for an Aurora DB Cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    db_instance_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB instance.</p>"""
    timezone: NotRequired["capo_rds.types.string.String"]
    """<p>The time zone of the DB instance. In most cases, the <code>Timezone</code> element is empty. <code>Timezone</code> content appears only for RDS for Db2 and RDS for SQL Server DB instances that were created with a time zone specified.</p>"""
    iam_database_authentication_enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled for the DB instance.</p> <p>For a list of engine versions that support IAM database authentication, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.IamDatabaseAuthentication.html">IAM database authentication</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.html">IAM database authentication in Aurora</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>The mode of Database Insights that is enabled for the instance.</p>"""
    performance_insights_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether Performance Insights is enabled for the DB instance.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p>"""
    enabled_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>A list of log types that this DB instance is configured to export to CloudWatch Logs.</p> <p>Log types vary by DB engine. For information about the log types for each DB engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html">Monitoring Amazon RDS log files</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"> Deleting a DB Instance</a>.</p>"""
    associated_roles: NotRequired["capo_rds.types.db_instance_roles.DBInstanceRoles"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) roles associated with the DB instance.</p>"""
    listener_endpoint: NotRequired["capo_rds.types.endpoint.Endpoint"]
    """<p>The listener connection endpoint for SQL Server Always On.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    automation_mode: NotRequired["capo_rds.types.automation_mode.AutomationMode"]
    """<p>The automation mode of the RDS Custom DB instance: <code>full</code> or <code>all paused</code>. If <code>full</code>, the DB instance automates monitoring and instance recovery. If <code>all paused</code>, the instance pauses automation for the duration set by <code>--resume-full-automation-mode-minutes</code>.</p>"""
    resume_full_automation_mode_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.</p>"""
    customer_owned_ip_enabled: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether a customer-owned IP address (CoIP) is enabled for an RDS on Outposts DB instance.</p> <p>A <i>CoIP </i>provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about CoIPs, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing">Customer-owned IP addresses</a> in the <i>Amazon Web Services Outposts User Guide</i>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB instance. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid Values: <code>IPV4 | DUAL</code> </p>"""
    activity_stream_status: NotRequired[
        "capo_rds.types.activity_stream_status.ActivityStreamStatus"
    ]
    """<p>The status of the database activity stream.</p>"""
    activity_stream_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier used for encrypting messages in the database activity stream. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    activity_stream_kinesis_stream_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Amazon Kinesis data stream used for the database activity stream.</p>"""
    activity_stream_mode: NotRequired[
        "capo_rds.types.activity_stream_mode.ActivityStreamMode"
    ]
    """<p>The mode of the database activity stream. Database events such as a change or access generate an activity stream event. RDS for Oracle always handles these events asynchronously.</p>"""
    activity_stream_engine_native_audit_fields_included: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether engine-native audit fields are included in the database activity stream.</p>"""
    aws_backup_recovery_point_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.</p>"""
    db_instance_automated_backups_replications: NotRequired[
        "capo_rds.types.db_instance_automated_backups_replication_list.DBInstanceAutomatedBackupsReplicationList"
    ]
    """<p>The list of replicated automated backups associated with the DB instance.</p>"""
    backup_target: NotRequired["capo_rds.types.string.String"]
    """<p>The location where automated backups and manual snapshots are stored: Dedicated Local Zones, Amazon Web Services Outposts or the Amazon Web Services Region.</p>"""
    automatic_restart_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time when a stopped DB instance is restarted automatically.</p>"""
    custom_iam_instance_profile: NotRequired["capo_rds.types.string.String"]
    """<p>The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:</p> <ul> <li> <p>The profile must exist in your account.</p> </li> <li> <p>The profile must have an IAM role that Amazon EC2 has permissions to assume.</p> </li> <li> <p>The instance profile name and the associated IAM role name must start with the prefix <code>AWSRDSCustom</code>.</p> </li> </ul> <p>For the list of permissions required for the IAM role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc"> Configure IAM and your VPC</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    activity_stream_policy_status: NotRequired[
        "capo_rds.types.activity_stream_policy_status.ActivityStreamPolicyStatus"
    ]
    """<p>The status of the policy state of the activity stream.</p>"""
    certificate_details: NotRequired[
        "capo_rds.types.certificate_details.CertificateDetails"
    ]
    """<p>The details of the DB instance's server certificate.</p>"""
    db_system_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is only valid for RDS Custom DB instances.</p>"""
    master_user_secret: NotRequired[
        "capo_rds.types.master_user_secret.MasterUserSecret"
    ]
    """<p>The secret managed by RDS in Amazon Web Services Secrets Manager for the master user password.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    read_replica_source_db_cluster_identifier: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>The identifier of the source DB cluster if this DB instance is a read replica.</p>"""
    percent_progress: NotRequired["capo_rds.types.string.String"]
    """<p>The progress of the storage optimization operation as a percentage.</p>"""
    multi_tenant: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is in the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).</p>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</p>"""
    is_storage_config_upgrade_available: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether an upgrade is recommended for the storage file system configuration on the DB instance. To migrate to the preferred configuration, you can either create a blue/green deployment, or create a read replica from the DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.UpgradeFileSystem">Upgrading the storage file system for a DB instance</a>.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for the DB instance.</p> <p>For more information, see CreateDBInstance.</p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_output_list.AdditionalStorageVolumesOutputList"
    ]
    """<p>The additional storage volumes associated with the DB instance. RDS supports additional storage volumes for RDS for Oracle and RDS for SQL Server.</p>"""
    storage_volume_status: NotRequired["capo_rds.types.string.String"]
    """<p>The detailed status information for storage volumes associated with the DB instance. This information helps identify which specific volume is causing the instance to be in a storage-full state.</p>"""
    storage_operation_status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of an in-progress storage operation on the DB instance. This field appears only while a storage operation is in progress. It isn't present when no storage operation is active. Possible values:</p> <ul> <li> <p> <code>Initializing</code> - The volume is initializing from a snapshot, such as during a snapshot restore, point-in-time restore, read replica creation, or blue/green deployment. Performance can be lower than provisioned until initialization completes.</p> </li> <li> <p> <code>Optimizing</code> - The volume is optimizing following a storage scaling or modification operation.</p> </li> </ul>"""
    storage_operation_percent_progress: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The percentage of the in-progress storage operation on the DB instance that has completed, from <code>0</code> to <code>100</code>. This field appears only while a storage operation is in progress. It isn't present when no storage operation is active.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "db_instance_status" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceStatus", str(value["db_instance_status"]))
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "endpoint" in value:
        import capo_rds.types.endpoint

        capo_rds.types.endpoint.serialize_query(
            value["endpoint"], pairs, f"{key_prefix}Endpoint"
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "instance_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["instance_create_time"], pairs, f"{key_prefix}InstanceCreateTime"
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "db_security_groups" in value:
        import capo_rds.types.db_security_group_membership_list

        capo_rds.types.db_security_group_membership_list.serialize_query(
            value["db_security_groups"], pairs, f"{key_prefix}DBSecurityGroups"
        )
    if "vpc_security_groups" in value:
        import capo_rds.types.vpc_security_group_membership_list

        capo_rds.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_groups"], pairs, f"{key_prefix}VpcSecurityGroups"
        )
    if "db_parameter_groups" in value:
        import capo_rds.types.db_parameter_group_status_list

        capo_rds.types.db_parameter_group_status_list.serialize_query(
            value["db_parameter_groups"], pairs, f"{key_prefix}DBParameterGroups"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "db_subnet_group" in value:
        import capo_rds.types.db_subnet_group

        capo_rds.types.db_subnet_group.serialize_query(
            value["db_subnet_group"], pairs, f"{key_prefix}DBSubnetGroup"
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
    if "pending_modified_values" in value:
        import capo_rds.types.pending_modified_values

        capo_rds.types.pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "latest_restorable_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["latest_restorable_time"], pairs, f"{key_prefix}LatestRestorableTime"
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "read_replica_source_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}ReadReplicaSourceDBInstanceIdentifier",
                str(value["read_replica_source_db_instance_identifier"]),
            )
        )
    if "read_replica_db_instance_identifiers" in value:
        import capo_rds.types.read_replica_db_instance_identifier_list

        capo_rds.types.read_replica_db_instance_identifier_list.serialize_query(
            value["read_replica_db_instance_identifiers"],
            pairs,
            f"{key_prefix}ReadReplicaDBInstanceIdentifiers",
        )
    if "read_replica_db_cluster_identifiers" in value:
        import capo_rds.types.read_replica_db_cluster_identifier_list

        capo_rds.types.read_replica_db_cluster_identifier_list.serialize_query(
            value["read_replica_db_cluster_identifiers"],
            pairs,
            f"{key_prefix}ReadReplicaDBClusterIdentifiers",
        )
    if "replica_mode" in value:
        import capo_rds.types.replica_mode

        capo_rds.types.replica_mode.serialize_query(
            value["replica_mode"], pairs, f"{key_prefix}ReplicaMode"
        )
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "option_group_memberships" in value:
        import capo_rds.types.option_group_membership_list

        capo_rds.types.option_group_membership_list.serialize_query(
            value["option_group_memberships"],
            pairs,
            f"{key_prefix}OptionGroupMemberships",
        )
    if "character_set_name" in value:
        pairs.append(
            (f"{key_prefix}CharacterSetName", str(value["character_set_name"]))
        )
    if "nchar_character_set_name" in value:
        pairs.append(
            (
                f"{key_prefix}NcharCharacterSetName",
                str(value["nchar_character_set_name"]),
            )
        )
    if "secondary_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryAvailabilityZone",
                str(value["secondary_availability_zone"]),
            )
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "status_infos" in value:
        import capo_rds.types.db_instance_status_info_list

        capo_rds.types.db_instance_status_info_list.serialize_query(
            value["status_infos"], pairs, f"{key_prefix}StatusInfos"
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "storage_encryption_type" in value:
        import capo_rds.types.storage_encryption_type

        capo_rds.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
        )
    if "tde_credential_arn" in value:
        pairs.append(
            (f"{key_prefix}TdeCredentialArn", str(value["tde_credential_arn"]))
        )
    if "db_instance_port" in value:
        pairs.append((f"{key_prefix}DbInstancePort", str(value["db_instance_port"])))
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "domain_memberships" in value:
        import capo_rds.types.domain_membership_list

        capo_rds.types.domain_membership_list.serialize_query(
            value["domain_memberships"], pairs, f"{key_prefix}DomainMemberships"
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "monitoring_interval" in value:
        pairs.append(
            (f"{key_prefix}MonitoringInterval", str(value["monitoring_interval"]))
        )
    if "enhanced_monitoring_resource_arn" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedMonitoringResourceArn",
                str(value["enhanced_monitoring_resource_arn"]),
            )
        )
    if "monitoring_role_arn" in value:
        pairs.append(
            (f"{key_prefix}MonitoringRoleArn", str(value["monitoring_role_arn"]))
        )
    if "promotion_tier" in value:
        pairs.append((f"{key_prefix}PromotionTier", str(value["promotion_tier"])))
    if "db_instance_arn" in value:
        pairs.append((f"{key_prefix}DBInstanceArn", str(value["db_instance_arn"])))
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
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
    if "enabled_cloudwatch_logs_exports" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["enabled_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnabledCloudwatchLogsExports",
        )
    if "processor_features" in value:
        import capo_rds.types.processor_feature_list

        capo_rds.types.processor_feature_list.serialize_query(
            value["processor_features"], pairs, f"{key_prefix}ProcessorFeatures"
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "associated_roles" in value:
        import capo_rds.types.db_instance_roles

        capo_rds.types.db_instance_roles.serialize_query(
            value["associated_roles"], pairs, f"{key_prefix}AssociatedRoles"
        )
    if "listener_endpoint" in value:
        import capo_rds.types.endpoint

        capo_rds.types.endpoint.serialize_query(
            value["listener_endpoint"], pairs, f"{key_prefix}ListenerEndpoint"
        )
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{key_prefix}MaxAllocatedStorage", str(value["max_allocated_storage"]))
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )
    if "automation_mode" in value:
        import capo_rds.types.automation_mode

        capo_rds.types.automation_mode.serialize_query(
            value["automation_mode"], pairs, f"{key_prefix}AutomationMode"
        )
    if "resume_full_automation_mode_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["resume_full_automation_mode_time"],
            pairs,
            f"{key_prefix}ResumeFullAutomationModeTime",
        )
    if "customer_owned_ip_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}CustomerOwnedIpEnabled",
                "true" if value["customer_owned_ip_enabled"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
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
    if "activity_stream_mode" in value:
        import capo_rds.types.activity_stream_mode

        capo_rds.types.activity_stream_mode.serialize_query(
            value["activity_stream_mode"], pairs, f"{key_prefix}ActivityStreamMode"
        )
    if "activity_stream_engine_native_audit_fields_included" in value:
        pairs.append(
            (
                f"{key_prefix}ActivityStreamEngineNativeAuditFieldsIncluded",
                "true"
                if value["activity_stream_engine_native_audit_fields_included"]
                else "false",
            )
        )
    if "aws_backup_recovery_point_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AwsBackupRecoveryPointArn",
                str(value["aws_backup_recovery_point_arn"]),
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
    if "automatic_restart_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["automatic_restart_time"], pairs, f"{key_prefix}AutomaticRestartTime"
        )
    if "custom_iam_instance_profile" in value:
        pairs.append(
            (
                f"{key_prefix}CustomIamInstanceProfile",
                str(value["custom_iam_instance_profile"]),
            )
        )
    if "activity_stream_policy_status" in value:
        import capo_rds.types.activity_stream_policy_status

        capo_rds.types.activity_stream_policy_status.serialize_query(
            value["activity_stream_policy_status"],
            pairs,
            f"{key_prefix}ActivityStreamPolicyStatus",
        )
    if "certificate_details" in value:
        import capo_rds.types.certificate_details

        capo_rds.types.certificate_details.serialize_query(
            value["certificate_details"], pairs, f"{key_prefix}CertificateDetails"
        )
    if "db_system_id" in value:
        pairs.append((f"{key_prefix}DBSystemId", str(value["db_system_id"])))
    if "master_user_secret" in value:
        import capo_rds.types.master_user_secret

        capo_rds.types.master_user_secret.serialize_query(
            value["master_user_secret"], pairs, f"{key_prefix}MasterUserSecret"
        )
    if "read_replica_source_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}ReadReplicaSourceDBClusterIdentifier",
                str(value["read_replica_source_db_cluster_identifier"]),
            )
        )
    if "percent_progress" in value:
        pairs.append((f"{key_prefix}PercentProgress", str(value["percent_progress"])))
    if "multi_tenant" in value:
        pairs.append(
            (f"{key_prefix}MultiTenant", "true" if value["multi_tenant"] else "false")
        )
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "is_storage_config_upgrade_available" in value:
        pairs.append(
            (
                f"{key_prefix}IsStorageConfigUpgradeAvailable",
                "true" if value["is_storage_config_upgrade_available"] else "false",
            )
        )
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )
    if "additional_storage_volumes" in value:
        import capo_rds.types.additional_storage_volumes_output_list

        capo_rds.types.additional_storage_volumes_output_list.serialize_query(
            value["additional_storage_volumes"],
            pairs,
            f"{key_prefix}AdditionalStorageVolumes",
        )
    if "storage_volume_status" in value:
        pairs.append(
            (f"{key_prefix}StorageVolumeStatus", str(value["storage_volume_status"]))
        )
    if "storage_operation_status" in value:
        pairs.append(
            (
                f"{key_prefix}StorageOperationStatus",
                str(value["storage_operation_status"]),
            )
        )
    if "storage_operation_percent_progress" in value:
        pairs.append(
            (
                f"{key_prefix}StorageOperationPercentProgress",
                str(value["storage_operation_percent_progress"]),
            )
        )


def deserialize_query(el: Element) -> DBInstance:
    out: DBInstance = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_db_instance_status = el.find("DBInstanceStatus")
    if child_db_instance_status is not None:
        out["db_instance_status"] = str(child_db_instance_status.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        import capo_rds.types.endpoint

        out["endpoint"] = capo_rds.types.endpoint.deserialize_query(child_endpoint)
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_instance_create_time = el.find("InstanceCreateTime")
    if child_instance_create_time is not None:
        import capo_rds.types.t_stamp

        out["instance_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_instance_create_time
        )
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_db_security_groups = el.find("DBSecurityGroups")
    if child_db_security_groups is not None:
        import capo_rds.types.db_security_group_membership_list

        out["db_security_groups"] = (
            capo_rds.types.db_security_group_membership_list.deserialize_query(
                child_db_security_groups
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
    child_db_parameter_groups = el.find("DBParameterGroups")
    if child_db_parameter_groups is not None:
        import capo_rds.types.db_parameter_group_status_list

        out["db_parameter_groups"] = (
            capo_rds.types.db_parameter_group_status_list.deserialize_query(
                child_db_parameter_groups
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        import capo_rds.types.db_subnet_group

        out["db_subnet_group"] = capo_rds.types.db_subnet_group.deserialize_query(
            child_db_subnet_group
        )
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
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_rds.types.pending_modified_values

        out["pending_modified_values"] = (
            capo_rds.types.pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_latest_restorable_time = el.find("LatestRestorableTime")
    if child_latest_restorable_time is not None:
        import capo_rds.types.t_stamp

        out["latest_restorable_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_latest_restorable_time
        )
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_read_replica_source_db_instance_identifier = el.find(
        "ReadReplicaSourceDBInstanceIdentifier"
    )
    if child_read_replica_source_db_instance_identifier is not None:
        out["read_replica_source_db_instance_identifier"] = str(
            child_read_replica_source_db_instance_identifier.text or ""
        )
    child_read_replica_db_instance_identifiers = el.find(
        "ReadReplicaDBInstanceIdentifiers"
    )
    if child_read_replica_db_instance_identifiers is not None:
        import capo_rds.types.read_replica_db_instance_identifier_list

        out["read_replica_db_instance_identifiers"] = (
            capo_rds.types.read_replica_db_instance_identifier_list.deserialize_query(
                child_read_replica_db_instance_identifiers
            )
        )
    child_read_replica_db_cluster_identifiers = el.find(
        "ReadReplicaDBClusterIdentifiers"
    )
    if child_read_replica_db_cluster_identifiers is not None:
        import capo_rds.types.read_replica_db_cluster_identifier_list

        out["read_replica_db_cluster_identifiers"] = (
            capo_rds.types.read_replica_db_cluster_identifier_list.deserialize_query(
                child_read_replica_db_cluster_identifiers
            )
        )
    child_replica_mode = el.find("ReplicaMode")
    if child_replica_mode is not None:
        import capo_rds.types.replica_mode

        out["replica_mode"] = capo_rds.types.replica_mode.deserialize_query(
            child_replica_mode
        )
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_option_group_memberships = el.find("OptionGroupMemberships")
    if child_option_group_memberships is not None:
        import capo_rds.types.option_group_membership_list

        out["option_group_memberships"] = (
            capo_rds.types.option_group_membership_list.deserialize_query(
                child_option_group_memberships
            )
        )
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_nchar_character_set_name = el.find("NcharCharacterSetName")
    if child_nchar_character_set_name is not None:
        out["nchar_character_set_name"] = str(child_nchar_character_set_name.text or "")
    child_secondary_availability_zone = el.find("SecondaryAvailabilityZone")
    if child_secondary_availability_zone is not None:
        out["secondary_availability_zone"] = str(
            child_secondary_availability_zone.text or ""
        )
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_status_infos = el.find("StatusInfos")
    if child_status_infos is not None:
        import capo_rds.types.db_instance_status_info_list

        out["status_infos"] = (
            capo_rds.types.db_instance_status_info_list.deserialize_query(
                child_status_infos
            )
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_rds.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_rds.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_db_instance_port = el.find("DbInstancePort")
    if child_db_instance_port is not None:
        out["db_instance_port"] = int(child_db_instance_port.text or "")
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_domain_memberships = el.find("DomainMemberships")
    if child_domain_memberships is not None:
        import capo_rds.types.domain_membership_list

        out["domain_memberships"] = (
            capo_rds.types.domain_membership_list.deserialize_query(
                child_domain_memberships
            )
        )
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_enhanced_monitoring_resource_arn = el.find("EnhancedMonitoringResourceArn")
    if child_enhanced_monitoring_resource_arn is not None:
        out["enhanced_monitoring_resource_arn"] = str(
            child_enhanced_monitoring_resource_arn.text or ""
        )
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    child_db_instance_arn = el.find("DBInstanceArn")
    if child_db_instance_arn is not None:
        out["db_instance_arn"] = str(child_db_instance_arn.text or "")
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
    child_enabled_cloudwatch_logs_exports = el.find("EnabledCloudwatchLogsExports")
    if child_enabled_cloudwatch_logs_exports is not None:
        import capo_rds.types.log_type_list

        out["enabled_cloudwatch_logs_exports"] = (
            capo_rds.types.log_type_list.deserialize_query(
                child_enabled_cloudwatch_logs_exports
            )
        )
    child_processor_features = el.find("ProcessorFeatures")
    if child_processor_features is not None:
        import capo_rds.types.processor_feature_list

        out["processor_features"] = (
            capo_rds.types.processor_feature_list.deserialize_query(
                child_processor_features
            )
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_associated_roles = el.find("AssociatedRoles")
    if child_associated_roles is not None:
        import capo_rds.types.db_instance_roles

        out["associated_roles"] = capo_rds.types.db_instance_roles.deserialize_query(
            child_associated_roles
        )
    child_listener_endpoint = el.find("ListenerEndpoint")
    if child_listener_endpoint is not None:
        import capo_rds.types.endpoint

        out["listener_endpoint"] = capo_rds.types.endpoint.deserialize_query(
            child_listener_endpoint
        )
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    child_automation_mode = el.find("AutomationMode")
    if child_automation_mode is not None:
        import capo_rds.types.automation_mode

        out["automation_mode"] = capo_rds.types.automation_mode.deserialize_query(
            child_automation_mode
        )
    child_resume_full_automation_mode_time = el.find("ResumeFullAutomationModeTime")
    if child_resume_full_automation_mode_time is not None:
        import capo_rds.types.t_stamp

        out["resume_full_automation_mode_time"] = (
            capo_rds.types.t_stamp.deserialize_query(
                child_resume_full_automation_mode_time
            )
        )
    child_customer_owned_ip_enabled = el.find("CustomerOwnedIpEnabled")
    if child_customer_owned_ip_enabled is not None:
        out["customer_owned_ip_enabled"] = (
            child_customer_owned_ip_enabled.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
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
    child_activity_stream_mode = el.find("ActivityStreamMode")
    if child_activity_stream_mode is not None:
        import capo_rds.types.activity_stream_mode

        out["activity_stream_mode"] = (
            capo_rds.types.activity_stream_mode.deserialize_query(
                child_activity_stream_mode
            )
        )
    child_activity_stream_engine_native_audit_fields_included = el.find(
        "ActivityStreamEngineNativeAuditFieldsIncluded"
    )
    if child_activity_stream_engine_native_audit_fields_included is not None:
        out["activity_stream_engine_native_audit_fields_included"] = (
            child_activity_stream_engine_native_audit_fields_included.text or ""
        ).lower() == "true"
    child_aws_backup_recovery_point_arn = el.find("AwsBackupRecoveryPointArn")
    if child_aws_backup_recovery_point_arn is not None:
        out["aws_backup_recovery_point_arn"] = str(
            child_aws_backup_recovery_point_arn.text or ""
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
    child_automatic_restart_time = el.find("AutomaticRestartTime")
    if child_automatic_restart_time is not None:
        import capo_rds.types.t_stamp

        out["automatic_restart_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_automatic_restart_time
        )
    child_custom_iam_instance_profile = el.find("CustomIamInstanceProfile")
    if child_custom_iam_instance_profile is not None:
        out["custom_iam_instance_profile"] = str(
            child_custom_iam_instance_profile.text or ""
        )
    child_activity_stream_policy_status = el.find("ActivityStreamPolicyStatus")
    if child_activity_stream_policy_status is not None:
        import capo_rds.types.activity_stream_policy_status

        out["activity_stream_policy_status"] = (
            capo_rds.types.activity_stream_policy_status.deserialize_query(
                child_activity_stream_policy_status
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
    child_db_system_id = el.find("DBSystemId")
    if child_db_system_id is not None:
        out["db_system_id"] = str(child_db_system_id.text or "")
    child_master_user_secret = el.find("MasterUserSecret")
    if child_master_user_secret is not None:
        import capo_rds.types.master_user_secret

        out["master_user_secret"] = capo_rds.types.master_user_secret.deserialize_query(
            child_master_user_secret
        )
    child_read_replica_source_db_cluster_identifier = el.find(
        "ReadReplicaSourceDBClusterIdentifier"
    )
    if child_read_replica_source_db_cluster_identifier is not None:
        out["read_replica_source_db_cluster_identifier"] = str(
            child_read_replica_source_db_cluster_identifier.text or ""
        )
    child_percent_progress = el.find("PercentProgress")
    if child_percent_progress is not None:
        out["percent_progress"] = str(child_percent_progress.text or "")
    child_multi_tenant = el.find("MultiTenant")
    if child_multi_tenant is not None:
        out["multi_tenant"] = (child_multi_tenant.text or "").lower() == "true"
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_is_storage_config_upgrade_available = el.find(
        "IsStorageConfigUpgradeAvailable"
    )
    if child_is_storage_config_upgrade_available is not None:
        out["is_storage_config_upgrade_available"] = (
            child_is_storage_config_upgrade_available.text or ""
        ).lower() == "true"
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.additional_storage_volumes_output_list

        out["additional_storage_volumes"] = (
            capo_rds.types.additional_storage_volumes_output_list.deserialize_query(
                child_additional_storage_volumes
            )
        )
    child_storage_volume_status = el.find("StorageVolumeStatus")
    if child_storage_volume_status is not None:
        out["storage_volume_status"] = str(child_storage_volume_status.text or "")
    child_storage_operation_status = el.find("StorageOperationStatus")
    if child_storage_operation_status is not None:
        out["storage_operation_status"] = str(child_storage_operation_status.text or "")
    child_storage_operation_percent_progress = el.find(
        "StorageOperationPercentProgress"
    )
    if child_storage_operation_percent_progress is not None:
        out["storage_operation_percent_progress"] = int(
            child_storage_operation_percent_progress.text or ""
        )
    return out

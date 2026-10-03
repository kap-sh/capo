"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.aws_backup_recovery_point_arn
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.cloudwatch_logs_export_configuration
    import capo_rds.types.database_insights_mode
    import capo_rds.types.integer_optional
    import capo_rds.types.long_optional
    import capo_rds.types.master_user_authentication_type
    import capo_rds.types.scaling_configuration
    import capo_rds.types.sensitive_string
    import capo_rds.types.serverless_v2_scaling_configuration
    import capo_rds.types.string
    import capo_rds.types.vpc_security_group_id_list


class ModifyDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier for the cluster being modified. This parameter isn't case-sensitive.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB cluster.</p> </li> </ul>"""
    new_db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>"""
    apply_immediately: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether the modifications in this request are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the DB cluster. If this parameter is disabled, changes to the DB cluster are applied during the next maintenance window.</p> <p>Most modifications can be applied immediately or during the next scheduled maintenance window. Some modifications, such as turning on deletion protection and changing the master password, are applied immediately—regardless of when you choose to apply them.</p> <p>By default, this parameter is disabled.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. Specify a minimum value of <code>1</code>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Default: <code>1</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35.</p> </li> </ul>"""
    db_cluster_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group to use for the DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of EC2 VPC security groups to associate with this DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the DB cluster accepts connections.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p> <p>Valid Values: <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The new password for the master database user.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 8 to 41 characters.</p> </li> <li> <p>Can contain any printable ASCII character except \"/\", \"\"\", or \"@\".</p> </li> <li> <p>Can't be specified if <code>ManageMasterUserPassword</code> is turned on.</p> </li> </ul>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group to associate the DB cluster with.</p> <p>DB clusters are associated with a default option group that can't be modified.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. To view the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow"> Backup window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. To see the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora"> Adjusting the Preferred DB Cluster Maintenance Window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>ddd:hh24:mi-ddd:hh24:mi</code>.</p> </li> <li> <p>Days must be one of <code>Mon | Tue | Wed | Thu | Fri | Sat | Sun</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication</a> in the <i>Amazon Aurora User Guide</i> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html">IAM database authentication for MariaDB, MySQL, and PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    backtrack_window: NotRequired["capo_rds.types.long_optional.LongOptional"]
    """<p>The target backtrack window, in seconds. To disable backtracking, set this value to <code>0</code>.</p> <p>Valid for Cluster Type: Aurora MySQL DB clusters only</p> <p>Default: <code>0</code> </p> <p>Constraints:</p> <ul> <li> <p>If specified, this value must be set to a number from 0 to 259,200 (72 hours).</p> </li> </ul>"""
    cloudwatch_logs_export_configuration: NotRequired[
        "capo_rds.types.cloudwatch_logs_export_configuration.CloudwatchLogsExportConfiguration"
    ]
    """<p>The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>The following values are valid for each DB engine:</p> <ul> <li> <p>Aurora MySQL - <code>audit | error | general | instance | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>Aurora PostgreSQL - <code>instance | postgresql | iam-db-auth-error</code> </p> </li> <li> <p>RDS for MySQL - <code>error | general | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql | upgrade | iam-db-auth-error</code> </p> </li> </ul> <p>For more information about exporting CloudWatch Logs for Amazon RDS, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch"> Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless <code>ApplyImmediately</code> is enabled.</p> <p>If the cluster that you're modifying has one or more read replicas, all replicas must be running an engine version that's the same or later than the version you specify.</p> <p>To list all of the available engine versions for Aurora MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query "DBEngineVersions[].EngineVersion"</code> </p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    allow_major_version_upgrade: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether major version upgrades are allowed.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>You must allow major version upgrades when specifying a value for the <code>EngineVersion</code> parameter that is a different major version than the DB cluster's current version.</p> </li> </ul>"""
    db_instance_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group to apply to all instances of the DB cluster.</p> <note> <p>When you apply a parameter group using the <code>DBInstanceParameterGroupName</code> parameter, the DB cluster isn't rebooted automatically. Also, parameter changes are applied immediately rather than during the next maintenance window.</p> </note> <p>Valid for Cluster Type: Aurora DB clusters only</p> <p>Default: The existing name setting</p> <p>Constraints:</p> <ul> <li> <p>The DB parameter group must be in the same DB parameter group family as this DB cluster.</p> </li> <li> <p>The <code>DBInstanceParameterGroupName</code> parameter is valid in combination with the <code>AllowMajorVersionUpgrade</code> parameter for a major version upgrade only.</p> </li> </ul>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to move the DB cluster to. Specify <code>none</code> to remove the cluster from its current domain. The domain must be created prior to this operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html">Kerberos Authentication</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    scaling_configuration: NotRequired[
        "capo_rds.types.scaling_configuration.ScalingConfiguration"
    ]
    """<p>The scaling properties of the DB cluster. You can only modify scaling properties for DB clusters in <code>serverless</code> DB engine mode.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    enable_http_endpoint: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable the HTTP endpoint for an Aurora Serverless v1 DB cluster. By default, the HTTP endpoint isn't enabled.</p> <p>When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the Aurora Serverless v1 DB cluster. You can also query your database from inside the RDS console with the RDS query editor.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html">Using RDS Data API</a> in the <i>Amazon Aurora User Guide</i>.</p> <note> <p>This parameter applies only to Aurora Serverless v1 DB clusters. To enable or disable the HTTP endpoint for an Aurora Serverless v2 or provisioned DB cluster, use the <code>EnableHttpEndpoint</code> and <code>DisableHttpEndpoint</code> operations.</p> </note> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    enable_global_write_forwarding: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable this DB cluster to forward write operations to the primary cluster of a global cluster (Aurora global database). By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.</p> <p>You can set this value only on Aurora DB clusters that are members of an Aurora global database. With this parameter enabled, a secondary cluster can forward writes to the current primary cluster, and the resulting changes are replicated back to this cluster. For the primary DB cluster of an Aurora global database, this value is used immediately if the primary is demoted by a global cluster API operation, but it does nothing until then.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    db_cluster_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example <code>db.m6gd.xlarge</code>. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines.</p> <p>For the full list of DB instance classes and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html"> DB Instance Class</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Aurora DB clusters, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#aurora-storage-type">Storage configurations for Amazon Aurora DB clusters</a>. For information on storage types for Multi-AZ DB clusters, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html#create-multi-az-db-cluster-settings">Settings for creating Multi-AZ DB clusters</a>.</p> <p>When specified for a Multi-AZ DB cluster, a value for the <code>Iops</code> parameter is required.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values:</p> <ul> <li> <p>Aurora DB clusters - <code>aurora | aurora-iopt1</code> </p> </li> <li> <p>Multi-AZ DB clusters - <code>io1 | io2 | gp3</code> </p> </li> </ul> <p>Default:</p> <ul> <li> <p>Aurora DB clusters - <code>aurora</code> </p> </li> <li> <p>Multi-AZ DB clusters - <code>io1</code> </p> </li> </ul>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS">Amazon RDS Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p> <p>Constraints:</p> <ul> <li> <p>Must be a multiple between .5 and 50 of the storage amount for the DB cluster.</p> </li> </ul>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid for Cluster Type: Aurora DB clusters only</p> <p>Valid Values: <code>IPV4 | DUAL</code> </p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_rds.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify <code>0</code>.</p> <p>If <code>MonitoringRoleArn</code> is specified, also set <code>MonitoringInterval</code> to a value other than <code>0</code>.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p> <p>Valid Values: <code>0 | 1 | 5 | 10 | 15 | 30 | 60</code> </p> <p>Default: <code>0</code> </p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole">To create an IAM role for Amazon RDS Enhanced Monitoring</a> in the <i>Amazon RDS User Guide.</i> </p> <p>If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, supply a <code>MonitoringRoleArn</code> value.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>Specifies the mode of Database Insights to enable for the DB cluster.</p> <p>If you change the value from <code>standard</code> to <code>advanced</code>, you must set the <code>PerformanceInsightsEnabled</code> parameter to <code>true</code> and the <code>PerformanceInsightsRetentionPeriod</code> parameter to 465.</p> <p>If you change the value from <code>advanced</code> to <code>standard</code>, you can set the <code>PerformanceInsightsEnabled</code> parameter to <code>true</code> to collect detailed database counter and per-query metrics.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    enable_performance_insights: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to turn on Performance Insights for the DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html"> Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you don't specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p> <p>If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS issues an error.</p>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>If the DB cluster doesn't manage the master user password with Amazon Web Services Secrets Manager, you can turn on this management. In this case, you can't specify <code>MasterUserPassword</code>.</p> <p>If the DB cluster already manages the master user password with Amazon Web Services Secrets Manager, and you specify that the master user password is not managed with Amazon Web Services Secrets Manager, then you must specify <code>MasterUserPassword</code>. In this case, RDS deletes the secret and uses the new password for the master user specified by <code>MasterUserPassword</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    rotate_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB cluster. The secret value contains the updated password.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>You must apply the change immediately when rotating the master user password.</p> </li> </ul>"""
    enable_local_write_forwarding: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether read replicas can forward write operations to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.</p> <p>Valid for: Aurora DB clusters only</p>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if both of the following conditions are met:</p> <ul> <li> <p>The DB cluster doesn't manage the master user password in Amazon Web Services Secrets Manager.</p> <p>If the DB cluster already manages the master user password in Amazon Web Services Secrets Manager, you can't change the KMS key that is used to encrypt the secret.</p> </li> <li> <p>You are turning on <code>ManageMasterUserPassword</code> to manage the master user password in Amazon Web Services Secrets Manager.</p> <p>If you are turning on <code>ManageMasterUserPassword</code> and don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> </li> </ul> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    engine_mode: NotRequired["capo_rds.types.string.String"]
    """<p>The DB engine mode of the DB cluster, either <code>provisioned</code> or <code>serverless</code>.</p> <note> <p>The DB engine mode can be modified only from <code>serverless</code> to <code>provisioned</code>.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html"> CreateDBCluster</a>.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    allow_engine_mode_change: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether engine mode changes from <code>serverless</code> to <code>provisioned</code> are allowed.</p> <p>Valid for Cluster Type: Aurora Serverless v1 DB clusters only</p> <p>Constraints:</p> <ul> <li> <p>You must allow engine mode changes when specifying a different value for the <code>EngineMode</code> parameter from the DB cluster's current engine mode.</p> </li> </ul>"""
    aws_backup_recovery_point_arn: NotRequired[
        "capo_rds.types.aws_backup_recovery_point_arn.AwsBackupRecoveryPointArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.</p>"""
    enable_limitless_database: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable Aurora Limitless Database. You must enable Aurora Limitless Database to create a DB shard group.</p> <p>Valid for: Aurora DB clusters only</p> <note> <p>This setting is no longer used. Instead use the <code>ClusterScalabilityType</code> setting when you create your Aurora Limitless Database DB cluster.</p> </note>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the DB cluster's server certificate.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters</p>"""
    master_user_authentication_type: NotRequired[
        "capo_rds.types.master_user_authentication_type.MasterUserAuthenticationType"
    ]
    """<p>Specifies the authentication type for the master user. With IAM master user authentication, you can change the master DB user to use IAM database authentication.</p> <p>You can specify one of the following values:</p> <ul> <li> <p> <code>password</code> - Use standard database authentication with a password.</p> </li> <li> <p> <code>iam-db-auth</code> - Use IAM database authentication for the master user.</p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB cluster.</p> <p>You can use this setting to enroll your DB cluster into Amazon RDS Extended Support or to opt out. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:</p> <ul> <li> <p>Amazon Aurora - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html">Amazon RDS Extended Support with Amazon Aurora</a> in the <i>Amazon Aurora User Guide</i> </p> </li> <li> <p>Amazon RDS - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i> </p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "new_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}NewDBClusterIdentifier",
                str(value["new_db_cluster_identifier"]),
            )
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{key_prefix}ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
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
    if "enable_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}EnableIAMDatabaseAuthentication",
                "true" if value["enable_iam_database_authentication"] else "false",
            )
        )
    if "backtrack_window" in value:
        pairs.append((f"{key_prefix}BacktrackWindow", str(value["backtrack_window"])))
    if "cloudwatch_logs_export_configuration" in value:
        import capo_rds.types.cloudwatch_logs_export_configuration

        capo_rds.types.cloudwatch_logs_export_configuration.serialize_query(
            value["cloudwatch_logs_export_configuration"],
            pairs,
            f"{key_prefix}CloudwatchLogsExportConfiguration",
        )
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "allow_major_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AllowMajorVersionUpgrade",
                "true" if value["allow_major_version_upgrade"] else "false",
            )
        )
    if "db_instance_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBInstanceParameterGroupName",
                str(value["db_instance_parameter_group_name"]),
            )
        )
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "domain_iam_role_name" in value:
        pairs.append(
            (f"{key_prefix}DomainIAMRoleName", str(value["domain_iam_role_name"]))
        )
    if "scaling_configuration" in value:
        import capo_rds.types.scaling_configuration

        capo_rds.types.scaling_configuration.serialize_query(
            value["scaling_configuration"], pairs, f"{key_prefix}ScalingConfiguration"
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "enable_http_endpoint" in value:
        pairs.append(
            (
                f"{key_prefix}EnableHttpEndpoint",
                "true" if value["enable_http_endpoint"] else "false",
            )
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "enable_global_write_forwarding" in value:
        pairs.append(
            (
                f"{key_prefix}EnableGlobalWriteForwarding",
                "true" if value["enable_global_write_forwarding"] else "false",
            )
        )
    if "db_cluster_instance_class" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterInstanceClass",
                str(value["db_cluster_instance_class"]),
            )
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "serverless_v2_scaling_configuration" in value:
        import capo_rds.types.serverless_v2_scaling_configuration

        capo_rds.types.serverless_v2_scaling_configuration.serialize_query(
            value["serverless_v2_scaling_configuration"],
            pairs,
            f"{key_prefix}ServerlessV2ScalingConfiguration",
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
    if "enable_performance_insights" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePerformanceInsights",
                "true" if value["enable_performance_insights"] else "false",
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
    if "manage_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}ManageMasterUserPassword",
                "true" if value["manage_master_user_password"] else "false",
            )
        )
    if "rotate_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}RotateMasterUserPassword",
                "true" if value["rotate_master_user_password"] else "false",
            )
        )
    if "enable_local_write_forwarding" in value:
        pairs.append(
            (
                f"{key_prefix}EnableLocalWriteForwarding",
                "true" if value["enable_local_write_forwarding"] else "false",
            )
        )
    if "master_user_secret_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}MasterUserSecretKmsKeyId",
                str(value["master_user_secret_kms_key_id"]),
            )
        )
    if "engine_mode" in value:
        pairs.append((f"{key_prefix}EngineMode", str(value["engine_mode"])))
    if "allow_engine_mode_change" in value:
        pairs.append(
            (
                f"{key_prefix}AllowEngineModeChange",
                "true" if value["allow_engine_mode_change"] else "false",
            )
        )
    if "aws_backup_recovery_point_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AwsBackupRecoveryPointArn",
                str(value["aws_backup_recovery_point_arn"]),
            )
        )
    if "enable_limitless_database" in value:
        pairs.append(
            (
                f"{key_prefix}EnableLimitlessDatabase",
                "true" if value["enable_limitless_database"] else "false",
            )
        )
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "master_user_authentication_type" in value:
        import capo_rds.types.master_user_authentication_type

        capo_rds.types.master_user_authentication_type.serialize_query(
            value["master_user_authentication_type"],
            pairs,
            f"{key_prefix}MasterUserAuthenticationType",
        )
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )


def deserialize_query(el: Element) -> ModifyDBClusterMessage:
    out: ModifyDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_new_db_cluster_identifier = el.find("NewDBClusterIdentifier")
    if child_new_db_cluster_identifier is not None:
        out["new_db_cluster_identifier"] = str(
            child_new_db_cluster_identifier.text or ""
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_enable_iam_database_authentication = el.find(
        "EnableIAMDatabaseAuthentication"
    )
    if child_enable_iam_database_authentication is not None:
        out["enable_iam_database_authentication"] = (
            child_enable_iam_database_authentication.text or ""
        ).lower() == "true"
    child_backtrack_window = el.find("BacktrackWindow")
    if child_backtrack_window is not None:
        out["backtrack_window"] = int(child_backtrack_window.text or "")
    child_cloudwatch_logs_export_configuration = el.find(
        "CloudwatchLogsExportConfiguration"
    )
    if child_cloudwatch_logs_export_configuration is not None:
        import capo_rds.types.cloudwatch_logs_export_configuration

        out["cloudwatch_logs_export_configuration"] = (
            capo_rds.types.cloudwatch_logs_export_configuration.deserialize_query(
                child_cloudwatch_logs_export_configuration
            )
        )
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_allow_major_version_upgrade = el.find("AllowMajorVersionUpgrade")
    if child_allow_major_version_upgrade is not None:
        out["allow_major_version_upgrade"] = (
            child_allow_major_version_upgrade.text or ""
        ).lower() == "true"
    child_db_instance_parameter_group_name = el.find("DBInstanceParameterGroupName")
    if child_db_instance_parameter_group_name is not None:
        out["db_instance_parameter_group_name"] = str(
            child_db_instance_parameter_group_name.text or ""
        )
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_domain_iam_role_name = el.find("DomainIAMRoleName")
    if child_domain_iam_role_name is not None:
        out["domain_iam_role_name"] = str(child_domain_iam_role_name.text or "")
    child_scaling_configuration = el.find("ScalingConfiguration")
    if child_scaling_configuration is not None:
        import capo_rds.types.scaling_configuration

        out["scaling_configuration"] = (
            capo_rds.types.scaling_configuration.deserialize_query(
                child_scaling_configuration
            )
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_enable_http_endpoint = el.find("EnableHttpEndpoint")
    if child_enable_http_endpoint is not None:
        out["enable_http_endpoint"] = (
            child_enable_http_endpoint.text or ""
        ).lower() == "true"
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_enable_global_write_forwarding = el.find("EnableGlobalWriteForwarding")
    if child_enable_global_write_forwarding is not None:
        out["enable_global_write_forwarding"] = (
            child_enable_global_write_forwarding.text or ""
        ).lower() == "true"
    child_db_cluster_instance_class = el.find("DBClusterInstanceClass")
    if child_db_cluster_instance_class is not None:
        out["db_cluster_instance_class"] = str(
            child_db_cluster_instance_class.text or ""
        )
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_serverless_v2_scaling_configuration = el.find(
        "ServerlessV2ScalingConfiguration"
    )
    if child_serverless_v2_scaling_configuration is not None:
        import capo_rds.types.serverless_v2_scaling_configuration

        out["serverless_v2_scaling_configuration"] = (
            capo_rds.types.serverless_v2_scaling_configuration.deserialize_query(
                child_serverless_v2_scaling_configuration
            )
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
    child_enable_performance_insights = el.find("EnablePerformanceInsights")
    if child_enable_performance_insights is not None:
        out["enable_performance_insights"] = (
            child_enable_performance_insights.text or ""
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
    child_manage_master_user_password = el.find("ManageMasterUserPassword")
    if child_manage_master_user_password is not None:
        out["manage_master_user_password"] = (
            child_manage_master_user_password.text or ""
        ).lower() == "true"
    child_rotate_master_user_password = el.find("RotateMasterUserPassword")
    if child_rotate_master_user_password is not None:
        out["rotate_master_user_password"] = (
            child_rotate_master_user_password.text or ""
        ).lower() == "true"
    child_enable_local_write_forwarding = el.find("EnableLocalWriteForwarding")
    if child_enable_local_write_forwarding is not None:
        out["enable_local_write_forwarding"] = (
            child_enable_local_write_forwarding.text or ""
        ).lower() == "true"
    child_master_user_secret_kms_key_id = el.find("MasterUserSecretKmsKeyId")
    if child_master_user_secret_kms_key_id is not None:
        out["master_user_secret_kms_key_id"] = str(
            child_master_user_secret_kms_key_id.text or ""
        )
    child_engine_mode = el.find("EngineMode")
    if child_engine_mode is not None:
        out["engine_mode"] = str(child_engine_mode.text or "")
    child_allow_engine_mode_change = el.find("AllowEngineModeChange")
    if child_allow_engine_mode_change is not None:
        out["allow_engine_mode_change"] = (
            child_allow_engine_mode_change.text or ""
        ).lower() == "true"
    child_aws_backup_recovery_point_arn = el.find("AwsBackupRecoveryPointArn")
    if child_aws_backup_recovery_point_arn is not None:
        out["aws_backup_recovery_point_arn"] = str(
            child_aws_backup_recovery_point_arn.text or ""
        )
    child_enable_limitless_database = el.find("EnableLimitlessDatabase")
    if child_enable_limitless_database is not None:
        out["enable_limitless_database"] = (
            child_enable_limitless_database.text or ""
        ).lower() == "true"
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_master_user_authentication_type = el.find("MasterUserAuthenticationType")
    if child_master_user_authentication_type is not None:
        import capo_rds.types.master_user_authentication_type

        out["master_user_authentication_type"] = (
            capo_rds.types.master_user_authentication_type.deserialize_query(
                child_master_user_authentication_type
            )
        )
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    return out

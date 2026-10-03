"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBClusterFromSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zones
    import capo_rds.types.boolean_optional
    import capo_rds.types.db_cluster_associated_roles
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.long_optional
    import capo_rds.types.rds_custom_cluster_configuration
    import capo_rds.types.scaling_configuration
    import capo_rds.types.serverless_v2_scaling_configuration
    import capo_rds.types.string
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class RestoreDBClusterFromSnapshotMessage(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>Provides the list of Availability Zones (AZs) where instances in the restored DB cluster can be created.</p> <p>Valid for: Aurora DB clusters only</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the DB snapshot or DB cluster snapshot to restore from.</p> <p>You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing Snapshot.</p> </li> </ul> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine to use for the new DB cluster.</p> <p>Default: The same as source</p> <p>Constraint: Must be compatible with the engine of the source</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine to use for the new DB cluster. If you don't specify an engine version, the default version for the database engine in the Amazon Web Services Region is used.</p> <p>To list all of the available engine versions for Aurora MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query "DBEngineVersions[].EngineVersion"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>See <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html">Database engine updates for Amazon Aurora MySQL</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>See <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html">Amazon Aurora PostgreSQL releases and engine versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>MySQL</b> </p> <p>See <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt">Amazon RDS for MySQL</a> in the <i>Amazon RDS User Guide.</i> </p> <p> <b>PostgreSQL</b> </p> <p>See <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts">Amazon RDS for PostgreSQL versions and extensions</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the new DB cluster accepts connections.</p> <p>Constraints: This value must be <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB subnet group to use for the new DB cluster.</p> <p>Constraints: If supplied, must match the name of an existing DB subnet group.</p> <p>Example: <code>mydbsubnetgroup</code> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    database_name: NotRequired["capo_rds.types.string.String"]
    """<p>The database name for the restored DB cluster.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option group to use for the restored DB cluster.</p> <p>DB clusters are associated with a default option group that can't be modified.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security groups that the new DB cluster will belong to.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>The tags to be assigned to the restored DB cluster.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>When you don't specify a value for the <code>KmsKeyId</code> parameter, then the following occurs:</p> <ul> <li> <p>If the DB snapshot or DB cluster snapshot in <code>SnapshotIdentifier</code> is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.</p> </li> <li> <p>If the DB snapshot or DB cluster snapshot in <code>SnapshotIdentifier</code> isn't encrypted, then the restored DB cluster isn't encrypted.</p> </li> </ul> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication</a> in the <i>Amazon Aurora User Guide</i> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"> IAM database authentication for MariaDB, MySQL, and PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    backtrack_window: NotRequired["capo_rds.types.long_optional.LongOptional"]
    """<p>The target backtrack window, in seconds. To disable backtracking, set this value to 0.</p> <note> <p>Currently, Backtrack is only supported for Aurora MySQL DB clusters.</p> </note> <p>Default: 0</p> <p>Constraints:</p> <ul> <li> <p>If specified, this value must be set to a number from 0 to 259,200 (72 hours).</p> </li> </ul> <p>Valid for: Aurora DB clusters only</p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of logs that the restored DB cluster is to export to Amazon CloudWatch Logs. The values in the list depend on the DB engine being used.</p> <p> <b>RDS for MySQL</b> </p> <p>Possible values are <code>error</code>, <code>general</code>, <code>slowquery</code>, and <code>iam-db-auth-error</code>.</p> <p> <b>RDS for PostgreSQL</b> </p> <p>Possible values are <code>postgresql</code>, <code>upgrade</code>, and <code>iam-db-auth-error</code>.</p> <p> <b>Aurora MySQL</b> </p> <p>Possible values are <code>audit</code>, <code>error</code>, <code>general</code>, <code>instance</code>, <code>slowquery</code>, and <code>iam-db-auth-error</code>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>Possible value are <code>instance</code>, <code>postgresql</code>, and <code>iam-db-auth-error</code>.</p> <p>For more information about exporting CloudWatch Logs for Amazon RDS, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    engine_mode: NotRequired["capo_rds.types.string.String"]
    """<p>The DB engine mode of the DB cluster, either <code>provisioned</code> or <code>serverless</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html"> CreateDBCluster</a>.</p> <p>Valid for: Aurora DB clusters only</p>"""
    scaling_configuration: NotRequired[
        "capo_rds.types.scaling_configuration.ScalingConfiguration"
    ]
    """<p>For DB clusters in <code>serverless</code> DB engine mode, the scaling properties of the DB cluster.</p> <p>Valid for: Aurora DB clusters only</p>"""
    db_cluster_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default DB cluster parameter group for the specified engine is used.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing default DB cluster parameter group.</p> </li> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable deletion protection for the DB cluster. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the restored DB cluster to snapshots of the restored DB cluster. The default is not to copy them.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to restore the DB cluster in. The domain must be created prior to this operation. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html"> Kerberos Authentication</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for: Aurora DB clusters only</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to be used when making API calls to the Directory Service.</p> <p>Valid for: Aurora DB clusters only</p>"""
    db_cluster_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of the each DB instance in the Multi-AZ DB cluster, for example db.m6gd.xlarge. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines.</p> <p>For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB Instance Class</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid for: Multi-AZ DB clusters only</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the storage type to be associated with the DB cluster.</p> <p>When specified for a Multi-AZ DB cluster, a value for the <code>Iops</code> parameter is required.</p> <p>Valid Values: <code>aurora</code>, <code>aurora-iopt1</code> (Aurora DB clusters); <code>io1</code> (Multi-AZ DB clusters)</p> <p>Default: <code>aurora</code> (Aurora DB clusters); <code>io1</code> (Multi-AZ DB clusters)</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS">Amazon RDS Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints: Must be a multiple between .5 and 50 of the storage amount for the DB instance.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB cluster is publicly accessible.</p> <p>When the DB cluster is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB cluster's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB cluster's VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.</p> <p>Default: The default behavior varies depending on whether <code>DBSubnetGroupName</code> is specified.</p> <p>If <code>DBSubnetGroupName</code> isn't specified, and <code>PubliclyAccessible</code> isn't specified, the following applies:</p> <ul> <li> <p>If the default VPC in the target Region doesn’t have an internet gateway attached to it, the DB cluster is private.</p> </li> <li> <p>If the default VPC in the target Region has an internet gateway attached to it, the DB cluster is public.</p> </li> </ul> <p>If <code>DBSubnetGroupName</code> is specified, and <code>PubliclyAccessible</code> isn't specified, the following applies:</p> <ul> <li> <p>If the subnets are part of a VPC that doesn’t have an internet gateway attached to it, the DB cluster is private.</p> </li> <li> <p>If the subnets are part of a VPC that has an internet gateway attached to it, the DB cluster is public.</p> </li> </ul> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <code>IPV4</code> </p> </li> <li> <p> <code>DUAL</code> </p> </li> </ul> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid for: Aurora DB clusters only</p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_rds.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    rds_custom_cluster_configuration: NotRequired[
        "capo_rds.types.rds_custom_cluster_configuration.RdsCustomClusterConfiguration"
    ]
    """<p>Reserved for future use.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify <code>0</code>.</p> <p>If <code>MonitoringRoleArn</code> is specified, also set <code>MonitoringInterval</code> to a value other than <code>0</code>.</p> <p>Valid Values: <code>0 | 1 | 5 | 10 | 15 | 30 | 60</code> </p> <p>Default: <code>0</code> </p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is <code>arn:aws:iam:123456789012:role/emaccess</code>.</p> <p>If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, supply a <code>MonitoringRoleArn</code> value.</p>"""
    enable_performance_insights: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to turn on Performance Insights for the DB cluster.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you don't specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p> <p>If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS issues an error.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. Specify a minimum value of <code>1</code>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35.</p> </li> </ul>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. To view the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow"> Backup window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB cluster.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, RDS automatically upgrades your restored DB cluster to a higher engine version, if the major engine version is past its end of standard support date.</p> </note> <p>You can use this setting to enroll your DB cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:</p> <ul> <li> <p>Amazon Aurora - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html">Amazon RDS Extended Support with Amazon Aurora</a> in the <i>Amazon Aurora User Guide</i> </p> </li> <li> <p>Amazon RDS - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i> </p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB cluster.</p> <p>Valid Values: </p> <ul> <li> <p> <code>cluster-auto-backup</code> - The DB cluster's automated backup.</p> </li> </ul>"""
    enable_vpc_networking: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable VPC networking for the restored DB cluster. Set this parameter to <code>false</code> to create a cluster without the VPC network interface (ENI).</p> <p>This parameter must be used together with <code>EnableInternetAccessGateway</code>. When both parameters are specified, IAM database authentication is required. You must also specify <code>EnableIAMDatabaseAuthentication</code>.</p> <p>Valid for Cluster Type: Aurora PostgreSQL clusters</p>"""
    enable_internet_access_gateway: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies that the restored DB cluster should use internet-based connectivity through an internet access gateway. This allows clients to connect to the cluster over the internet without requiring a VPC.</p> <p>This parameter must be used together with <code>EnableVPCNetworking</code> set to <code>false</code>. When both parameters are specified, IAM database authentication is required. You must also specify <code>EnableIAMDatabaseAuthentication</code>.</p> <p>Valid for Cluster Type: Aurora PostgreSQL clusters</p>"""
    associated_roles: NotRequired[
        "capo_rds.types.db_cluster_associated_roles.DBClusterAssociatedRoles"
    ]
    """<p>A list of Amazon Web Services Identity and Access Management (IAM) roles to associate with the DB cluster when it's restored from a snapshot. Each role grants the DB cluster permission to access other Amazon Web Services on your behalf. For each role, specify a role ARN and, optionally, the feature name (such as <code>s3Import</code>, <code>s3Export</code>, or <code>Lambda</code>).</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBClusterFromSnapshotMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_rds.types.availability_zones

        capo_rds.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "database_name" in value:
        pairs.append((f"{key_prefix}DatabaseName", str(value["database_name"])))
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "vpc_security_group_ids" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "enable_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}EnableIAMDatabaseAuthentication",
                "true" if value["enable_iam_database_authentication"] else "false",
            )
        )
    if "backtrack_window" in value:
        pairs.append((f"{key_prefix}BacktrackWindow", str(value["backtrack_window"])))
    if "enable_cloudwatch_logs_exports" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["enable_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnableCloudwatchLogsExports",
        )
    if "engine_mode" in value:
        pairs.append((f"{key_prefix}EngineMode", str(value["engine_mode"])))
    if "scaling_configuration" in value:
        import capo_rds.types.scaling_configuration

        capo_rds.types.scaling_configuration.serialize_query(
            value["scaling_configuration"], pairs, f"{key_prefix}ScalingConfiguration"
        )
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "domain_iam_role_name" in value:
        pairs.append(
            (f"{key_prefix}DomainIAMRoleName", str(value["domain_iam_role_name"]))
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
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
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
    if "rds_custom_cluster_configuration" in value:
        import capo_rds.types.rds_custom_cluster_configuration

        capo_rds.types.rds_custom_cluster_configuration.serialize_query(
            value["rds_custom_cluster_configuration"],
            pairs,
            f"{key_prefix}RdsCustomClusterConfiguration",
        )
    if "monitoring_interval" in value:
        pairs.append(
            (f"{key_prefix}MonitoringInterval", str(value["monitoring_interval"]))
        )
    if "monitoring_role_arn" in value:
        pairs.append(
            (f"{key_prefix}MonitoringRoleArn", str(value["monitoring_role_arn"]))
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
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )
    if "tag_specifications" in value:
        import capo_rds.types.tag_specification_list

        capo_rds.types.tag_specification_list.serialize_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "enable_vpc_networking" in value:
        pairs.append(
            (
                f"{key_prefix}EnableVPCNetworking",
                "true" if value["enable_vpc_networking"] else "false",
            )
        )
    if "enable_internet_access_gateway" in value:
        pairs.append(
            (
                f"{key_prefix}EnableInternetAccessGateway",
                "true" if value["enable_internet_access_gateway"] else "false",
            )
        )
    if "associated_roles" in value:
        import capo_rds.types.db_cluster_associated_roles

        capo_rds.types.db_cluster_associated_roles.serialize_query(
            value["associated_roles"], pairs, f"{key_prefix}AssociatedRoles"
        )


def deserialize_query(el: Element) -> RestoreDBClusterFromSnapshotMessage:
    out: RestoreDBClusterFromSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_rds.types.availability_zones

        out["availability_zones"] = capo_rds.types.availability_zones.deserialize_query(
            child_availability_zones
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
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
    child_enable_cloudwatch_logs_exports = el.find("EnableCloudwatchLogsExports")
    if child_enable_cloudwatch_logs_exports is not None:
        import capo_rds.types.log_type_list

        out["enable_cloudwatch_logs_exports"] = (
            capo_rds.types.log_type_list.deserialize_query(
                child_enable_cloudwatch_logs_exports
            )
        )
    child_engine_mode = el.find("EngineMode")
    if child_engine_mode is not None:
        out["engine_mode"] = str(child_engine_mode.text or "")
    child_scaling_configuration = el.find("ScalingConfiguration")
    if child_scaling_configuration is not None:
        import capo_rds.types.scaling_configuration

        out["scaling_configuration"] = (
            capo_rds.types.scaling_configuration.deserialize_query(
                child_scaling_configuration
            )
        )
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_domain_iam_role_name = el.find("DomainIAMRoleName")
    if child_domain_iam_role_name is not None:
        out["domain_iam_role_name"] = str(child_domain_iam_role_name.text or "")
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
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
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
    child_rds_custom_cluster_configuration = el.find("RdsCustomClusterConfiguration")
    if child_rds_custom_cluster_configuration is not None:
        import capo_rds.types.rds_custom_cluster_configuration

        out["rds_custom_cluster_configuration"] = (
            capo_rds.types.rds_custom_cluster_configuration.deserialize_query(
                child_rds_custom_cluster_configuration
            )
        )
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
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
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_rds.types.tag_specification_list

        out["tag_specifications"] = (
            capo_rds.types.tag_specification_list.deserialize_query(
                child_tag_specifications
            )
        )
    child_enable_vpc_networking = el.find("EnableVPCNetworking")
    if child_enable_vpc_networking is not None:
        out["enable_vpc_networking"] = (
            child_enable_vpc_networking.text or ""
        ).lower() == "true"
    child_enable_internet_access_gateway = el.find("EnableInternetAccessGateway")
    if child_enable_internet_access_gateway is not None:
        out["enable_internet_access_gateway"] = (
            child_enable_internet_access_gateway.text or ""
        ).lower() == "true"
    child_associated_roles = el.find("AssociatedRoles")
    if child_associated_roles is not None:
        import capo_rds.types.db_cluster_associated_roles

        out["associated_roles"] = (
            capo_rds.types.db_cluster_associated_roles.deserialize_query(
                child_associated_roles
            )
        )
    return out

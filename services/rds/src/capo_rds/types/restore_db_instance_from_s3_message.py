"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBInstanceFromS3Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.boolean_optional
    import capo_rds.types.database_insights_mode
    import capo_rds.types.db_security_group_name_list
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.processor_feature_list
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class RestoreDBInstanceFromS3Message(TypedDict, closed=True):
    db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database to create when the DB instance is created. Follow the naming rules specified in <code>CreateDBInstance</code>.</p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage (in gibibytes) to allocate initially for the DB instance. Follow the allocation rules specified in <code>CreateDBInstance</code>.</p> <p>This setting isn't valid for RDS for SQL Server.</p> <note> <p>Be sure to allocate enough storage for your new DB instance so that the restore operation can succeed. You can also allocate additional storage for future growth.</p> </note>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of the DB instance, for example db.m4.large. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB Instance Class</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Importing from Amazon S3 isn't supported on the db.t2.micro DB instance class.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine to be used for this instance.</p> <p>Valid Values: <code>mysql</code> </p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The name for the master user.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 16 letters or numbers.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> </li> </ul>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The password for the master user.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>ManageMasterUserPassword</code> is turned on.</p> </li> <li> <p>Can include any printable ASCII character except \"/\", \"\"\", or \"@\". For RDS for Oracle, can't include the \"&amp;\" (ampersand) or the \"'\" (single quotes) character.</p> </li> </ul> <p>Length Constraints:</p> <ul> <li> <p>RDS for Db2 - Must contain from 8 to 128 characters.</p> </li> <li> <p>RDS for MariaDB - Must contain from 8 to 41 characters.</p> </li> <li> <p>RDS for Microsoft SQL Server - Must contain from 8 to 128 characters.</p> </li> <li> <p>RDS for MySQL - Must contain from 8 to 41 characters.</p> </li> <li> <p>RDS for Oracle - Must contain from 8 to 30 characters.</p> </li> <li> <p>RDS for PostgreSQL - Must contain from 8 to 128 characters.</p> </li> </ul>"""
    db_security_groups: NotRequired[
        "capo_rds.types.db_security_group_name_list.DBSecurityGroupNameList"
    ]
    """<p>A list of DB security groups to associate with this DB instance.</p> <p>Default: The default DB security group for the database engine.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security groups to associate with this DB instance.</p>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The Availability Zone that the DB instance is created in. For information about Amazon Web Services Regions and Availability Zones, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html">Regions and Availability Zones</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Default: A random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region.</p> <p>Example: <code>us-east-1d</code> </p> <p>Constraint: The <code>AvailabilityZone</code> parameter can't be specified if the DB instance is a Multi-AZ deployment. The specified Availability Zone must be in the same Amazon Web Services Region as the current endpoint.</p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>A DB subnet group to associate with this DB instance.</p> <p>Constraints: If supplied, must match the name of an existing DBSubnetGroup.</p> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC). For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance">Amazon RDS Maintenance Window</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>ddd:hh24:mi-ddd:hh24:mi</code>.</p> </li> <li> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred backup window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group to associate with this DB instance.</p> <p>If you do not specify a value for <code>DBParameterGroupName</code>, then the default <code>DBParameterGroup</code> for the specified DB engine is used.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. For more information, see <code>CreateDBInstance</code>.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The time range each day during which automated backups are created if automated backups are enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow">Backup window</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the database accepts connections.</p> <p>Type: Integer</p> <p>Valid Values: <code>1150</code>-<code>65535</code> </p> <p>Default: <code>3306</code> </p>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is a Multi-AZ deployment. If the DB instance is a Multi-AZ deployment, you can't set the <code>AvailabilityZone</code> parameter.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to use. Choose the latest minor version of your database engine. For information about engine versions, see <code>CreateDBInstance</code>, or call <code>DescribeDBEngineVersions</code>.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to automatically apply minor engine upgrades to the DB instance during the maintenance window. By default, minor engine upgrades are not applied automatically.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model for this DB instance. Use <code>general-public-license</code>.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to allocate initially for the DB instance. For information about valid IOPS values, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS">Amazon RDS Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Specifies the storage throughput value for the DB instance.</p> <p>This setting doesn't apply to RDS Custom or Amazon Aurora.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option group to associate with this DB instance. If this argument is omitted, the default option group for the specified engine is used.</p>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB instance's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB instance's VPC. Access to the DB instance is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB instance doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p> <p>For more information, see <a>CreateDBInstance</a>.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>A list of tags to associate with this DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html">Tagging Amazon RDS Resources</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the storage type to be associated with the DB instance.</p> <p>Valid Values: <code>gp2 | gp3 | io1 | io2 | standard</code> </p> <p>If you specify <code>io1</code>, <code>io2</code>, or <code>gp3</code>, you must also include a value for the <code>Iops</code> parameter.</p> <p>Default: <code>io1</code> if the <code>Iops</code> parameter is specified; otherwise <code>gp2</code> </p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the new DB instance is encrypted or not.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted DB instance.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If the <code>StorageEncrypted</code> parameter is enabled, and you do not specify a value for the <code>KmsKeyId</code> parameter, then Amazon RDS will use your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0.</p> <p>If <code>MonitoringRoleArn</code> is specified, then you must also set <code>MonitoringInterval</code> to a value other than 0.</p> <p>Valid Values: 0, 1, 5, 10, 15, 30, 60</p> <p>Default: <code>0</code> </p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling">Setting Up and Enabling Enhanced Monitoring</a> in the <i>Amazon RDS User Guide.</i> </p> <p>If <code>MonitoringInterval</code> is set to a value other than 0, then you must supply a <code>MonitoringRoleArn</code> value.</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information about IAM database authentication, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication for MySQL and PostgreSQL</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    source_engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the engine of your source database.</p> <p>Valid Values: <code>mysql</code> </p>"""
    source_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database that the backup files were created from.</p> <p>MySQL versions 5.6 and 5.7 are supported.</p> <p>Example: <code>5.6.40</code> </p>"""
    s3_bucket_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of your Amazon S3 bucket that contains your database backup file.</p>"""
    s3_prefix: NotRequired["capo_rds.types.string.String"]
    """<p>The prefix of your Amazon S3 bucket.</p>"""
    s3_ingestion_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>An Amazon Web Services Identity and Access Management (IAM) role with a trust policy and a permissions policy that allows Amazon RDS to access your Amazon S3 bucket. For information about this role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html#MySQL.Procedural.Importing.Enabling.IAM"> Creating an IAM role manually</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>Specifies the mode of Database Insights to enable for the DB instance.</p> <note> <p>Aurora DB instances inherit this value from the DB cluster, so you can't change this value.</p> </note>"""
    enable_performance_insights: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable Performance Insights for the DB instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html">Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you do not specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data. The default is 7 days. The following values are valid:</p> <ul> <li> <p>7</p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23</p> </li> <li> <p>731</p> </li> </ul> <p>For example, the following values are valid:</p> <ul> <li> <p>93 (3 months * 31)</p> </li> <li> <p>341 (11 months * 31)</p> </li> <li> <p>589 (19 months * 31)</p> </li> <li> <p>731</p> </li> </ul> <p>If you specify a retention period such as 94, which isn't a valid value, RDS issues an error.</p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of logs that the restored DB instance is to export to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p>"""
    use_default_processor_features: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance class of the DB instance uses its default processor features.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable deletion protection for the DB instance. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"> Deleting a DB Instance</a>.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.</p> <p>For more information about this setting, including limitations that apply to it, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling"> Managing capacity automatically with Amazon RDS storage autoscaling</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>Valid Values:</p> <ul> <li> <p> <code>IPV4</code> </p> </li> <li> <p> <code>DUAL</code> </p> </li> </ul> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB instance. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p> </li> </ul>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable a dedicated log volume (DLV) for the DB instance.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the DB instance's server certificate.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB instance.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, RDS automatically upgrades your restored DB instance to a higher engine version, if the major engine version is past its end of standard support date.</p> </note> <p>You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support Amazon RDS</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the engine lifecycle support is managed by the DB cluster.</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>A list of additional storage volumes to modify or delete for the DB instance. You can modify or delete up to three additional storage volumes using the names <code>rdsdbdata2</code>, <code>rdsdbdata3</code>, and <code>rdsdbdata4</code>. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.</p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB instance.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBInstanceFromS3Message, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "db_security_groups" in value:
        import capo_rds.types.db_security_group_name_list

        capo_rds.types.db_security_group_name_list.serialize_query(
            value["db_security_groups"], pairs, f"{key_prefix}DBSecurityGroups"
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
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
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
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
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
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
    if "monitoring_role_arn" in value:
        pairs.append(
            (f"{key_prefix}MonitoringRoleArn", str(value["monitoring_role_arn"]))
        )
    if "enable_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}EnableIAMDatabaseAuthentication",
                "true" if value["enable_iam_database_authentication"] else "false",
            )
        )
    if "source_engine" in value:
        pairs.append((f"{key_prefix}SourceEngine", str(value["source_engine"])))
    if "source_engine_version" in value:
        pairs.append(
            (f"{key_prefix}SourceEngineVersion", str(value["source_engine_version"]))
        )
    if "s3_bucket_name" in value:
        pairs.append((f"{key_prefix}S3BucketName", str(value["s3_bucket_name"])))
    if "s3_prefix" in value:
        pairs.append((f"{key_prefix}S3Prefix", str(value["s3_prefix"])))
    if "s3_ingestion_role_arn" in value:
        pairs.append(
            (f"{key_prefix}S3IngestionRoleArn", str(value["s3_ingestion_role_arn"]))
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
    if "enable_cloudwatch_logs_exports" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["enable_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnableCloudwatchLogsExports",
        )
    if "processor_features" in value:
        import capo_rds.types.processor_feature_list

        capo_rds.types.processor_feature_list.serialize_query(
            value["processor_features"], pairs, f"{key_prefix}ProcessorFeatures"
        )
    if "use_default_processor_features" in value:
        pairs.append(
            (
                f"{key_prefix}UseDefaultProcessorFeatures",
                "true" if value["use_default_processor_features"] else "false",
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{key_prefix}MaxAllocatedStorage", str(value["max_allocated_storage"]))
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "manage_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}ManageMasterUserPassword",
                "true" if value["manage_master_user_password"] else "false",
            )
        )
    if "master_user_secret_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}MasterUserSecretKmsKeyId",
                str(value["master_user_secret_kms_key_id"]),
            )
        )
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
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
        import capo_rds.types.additional_storage_volumes_list

        capo_rds.types.additional_storage_volumes_list.serialize_query(
            value["additional_storage_volumes"],
            pairs,
            f"{key_prefix}AdditionalStorageVolumes",
        )
    if "tag_specifications" in value:
        import capo_rds.types.tag_specification_list

        capo_rds.types.tag_specification_list.serialize_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )


def deserialize_query(el: Element) -> RestoreDBInstanceFromS3Message:
    out: RestoreDBInstanceFromS3Message = {}  # type: ignore[typeddict-item]
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_db_security_groups = el.find("DBSecurityGroups")
    if child_db_security_groups is not None:
        import capo_rds.types.db_security_group_name_list

        out["db_security_groups"] = (
            capo_rds.types.db_security_group_name_list.deserialize_query(
                child_db_security_groups
            )
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
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
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
    child_enable_iam_database_authentication = el.find(
        "EnableIAMDatabaseAuthentication"
    )
    if child_enable_iam_database_authentication is not None:
        out["enable_iam_database_authentication"] = (
            child_enable_iam_database_authentication.text or ""
        ).lower() == "true"
    child_source_engine = el.find("SourceEngine")
    if child_source_engine is not None:
        out["source_engine"] = str(child_source_engine.text or "")
    child_source_engine_version = el.find("SourceEngineVersion")
    if child_source_engine_version is not None:
        out["source_engine_version"] = str(child_source_engine_version.text or "")
    child_s3_bucket_name = el.find("S3BucketName")
    if child_s3_bucket_name is not None:
        out["s3_bucket_name"] = str(child_s3_bucket_name.text or "")
    child_s3_prefix = el.find("S3Prefix")
    if child_s3_prefix is not None:
        out["s3_prefix"] = str(child_s3_prefix.text or "")
    child_s3_ingestion_role_arn = el.find("S3IngestionRoleArn")
    if child_s3_ingestion_role_arn is not None:
        out["s3_ingestion_role_arn"] = str(child_s3_ingestion_role_arn.text or "")
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
    child_enable_cloudwatch_logs_exports = el.find("EnableCloudwatchLogsExports")
    if child_enable_cloudwatch_logs_exports is not None:
        import capo_rds.types.log_type_list

        out["enable_cloudwatch_logs_exports"] = (
            capo_rds.types.log_type_list.deserialize_query(
                child_enable_cloudwatch_logs_exports
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
    child_use_default_processor_features = el.find("UseDefaultProcessorFeatures")
    if child_use_default_processor_features is not None:
        out["use_default_processor_features"] = (
            child_use_default_processor_features.text or ""
        ).lower() == "true"
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_manage_master_user_password = el.find("ManageMasterUserPassword")
    if child_manage_master_user_password is not None:
        out["manage_master_user_password"] = (
            child_manage_master_user_password.text or ""
        ).lower() == "true"
    child_master_user_secret_kms_key_id = el.find("MasterUserSecretKmsKeyId")
    if child_master_user_secret_kms_key_id is not None:
        out["master_user_secret_kms_key_id"] = str(
            child_master_user_secret_kms_key_id.text or ""
        )
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.additional_storage_volumes_list

        out["additional_storage_volumes"] = (
            capo_rds.types.additional_storage_volumes_list.deserialize_query(
                child_additional_storage_volumes
            )
        )
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_rds.types.tag_specification_list

        out["tag_specifications"] = (
            capo_rds.types.tag_specification_list.deserialize_query(
                child_tag_specifications
            )
        )
    return out

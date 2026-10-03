"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBInstanceToPointInTimeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.processor_feature_list
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class RestoreDBInstanceToPointInTimeMessage(TypedDict, closed=True):
    source_db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the source DB instance from which to restore.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB instance.</p> </li> </ul>"""
    target_db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the new DB instance to create.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    restore_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time to restore from.</p> <p>Constraints:</p> <ul> <li> <p>Must be a time in Universal Coordinated Time (UTC) format.</p> </li> <li> <p>Must be before the latest restorable time for the DB instance.</p> </li> <li> <p>Can't be specified if the <code>UseLatestRestorableTime</code> parameter is enabled.</p> </li> </ul> <p>Example: <code>2009-09-07T23:45:00Z</code> </p>"""
    use_latest_restorable_time: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether the DB instance is restored from the latest backup time. By default, the DB instance isn't restored from the latest backup time.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if the <code>RestoreTime</code> parameter is provided.</p> </li> </ul>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of the Amazon RDS DB instance, for example db.m4.large. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB Instance Class</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Default: The same DB instance class as the original DB instance.</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the database accepts connections.</p> <p>Default: The same port as the original DB instance.</p> <p>Constraints:</p> <ul> <li> <p>The value must be <code>1150-65535</code>.</p> </li> </ul>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The Availability Zone (AZ) where the DB instance will be created.</p> <p>Default: A random, system-chosen Availability Zone.</p> <p>Constraints:</p> <ul> <li> <p>You can't specify the <code>AvailabilityZone</code> parameter if the DB instance is a Multi-AZ deployment.</p> </li> </ul> <p>Example: <code>us-east-1a</code> </p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The DB subnet group name to use for the new instance.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DB subnet group.</p> </li> </ul> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Secifies whether the DB instance is a Multi-AZ deployment.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>Constraints:</p> <ul> <li> <p>You can't specify the <code>AvailabilityZone</code> parameter if the DB instance is a Multi-AZ deployment.</p> </li> </ul>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is publicly accessible.</p> <p>When the DB cluster is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB cluster's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB cluster's VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p> <p>For more information, see <a>CreateDBInstance</a>.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether minor version upgrades are applied automatically to the DB instance during the maintenance window.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model information for the restored DB instance.</p> <note> <p>License models for RDS for Db2 require additional configuration. The bring your own license (BYOL) model requires a custom parameter group and an Amazon Web Services License Manager self-managed license. The Db2 license through Amazon Web Services Marketplace model requires an Amazon Web Services Marketplace subscription. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html">Amazon RDS for Db2 licensing options</a> in the <i>Amazon RDS User Guide</i>.</p> </note> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p> <p>Valid Values:</p> <ul> <li> <p>RDS for Db2 - <code>bring-your-own-license | marketplace-license</code> </p> </li> <li> <p>RDS for MariaDB - <code>general-public-license</code> </p> </li> <li> <p>RDS for Microsoft SQL Server - <code>license-included | bring-your-own-media</code> </p> </li> <li> <p>RDS for MySQL - <code>general-public-license</code> </p> </li> <li> <p>RDS for Oracle - <code>bring-your-own-license | license-included</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql-license</code> </p> </li> </ul> <p>Default: Same as the source.</p>"""
    db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The database name for the restored DB instance.</p> <p>This parameter doesn't apply to the following DB instances:</p> <ul> <li> <p>RDS Custom</p> </li> <li> <p>RDS for Db2</p> </li> <li> <p>RDS for MariaDB</p> </li> <li> <p>RDS for MySQL</p> </li> </ul>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine to use for the new instance.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>Valid Values:</p> <ul> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-ce</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul> <p>Default: The same as source</p> <p>Constraints:</p> <ul> <li> <p>Must be compatible with the engine of the source.</p> </li> </ul>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance.</p> <p>This setting doesn't apply to SQL Server.</p> <p>Constraints:</p> <ul> <li> <p>Must be an integer greater than 1000.</p> </li> </ul>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput value for the DB instance.</p> <p>This setting doesn't apply to RDS Custom or Amazon Aurora.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option group to use for the restored DB instance.</p> <p>Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance after it is associated with a DB instance</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the restored DB instance to snapshots of the DB instance. By default, tags are not copied.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type to associate with the DB instance.</p> <p>Valid Values: <code>gp2 | gp3 | io1 | io2 | standard</code> </p> <p>Default: <code>io1</code>, if the <code>Iops</code> parameter is specified. Otherwise, <code>gp3</code>.</p> <p>Constraints:</p> <ul> <li> <p>If you specify <code>io1</code>, <code>io2</code>, or <code>gp3</code>, you must also include a value for the <code>Iops</code> parameter.</p> </li> </ul>"""
    tde_credential_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN from the key store with which to associate the instance for TDE encryption.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    tde_credential_password: NotRequired[
        "capo_rds.types.sensitive_string.SensitiveString"
    ]
    """<p>The password for the given ARN from the key store in order to access the device.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of EC2 VPC security groups to associate with this DB instance.</p> <p>Default: The default EC2 VPC security group for the DB subnet group's VPC.</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to restore the DB instance in. Create the domain before running this command. Currently, you can create only the MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html"> Kerberos Authentication</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    domain_fqdn: NotRequired["capo_rds.types.string.String"]
    """<p>The fully qualified domain name (FQDN) of an Active Directory domain.</p> <p>Constraints:</p> <ul> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>mymanagedADtest.mymanagedAD.mydomain</code> </p>"""
    domain_ou: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory organizational unit for your DB instance to join.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the distinguished name format.</p> </li> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain</code> </p>"""
    domain_auth_secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the Secrets Manager secret with the credentials for the user joining the domain.</p> <p>Constraints:</p> <ul> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456</code> </p>"""
    domain_dns_ips: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.</p> <p>Constraints:</p> <ul> <li> <p>Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.</p> </li> </ul> <p>Example: <code>123.124.125.126,234.235.236.237</code> </p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>For more information about IAM database authentication, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication for MySQL and PostgreSQL</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of logs that the restored DB instance is to export to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    use_default_processor_features: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance class of the DB instance uses its default processor features.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group to associate with this DB instance.</p> <p>If you do not specify a value for <code>DBParameterGroupName</code>, then the default <code>DBParameterGroup</code> for the specified DB engine is used.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DB parameter group.</p> </li> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"> Deleting a DB Instance</a>.</p>"""
    source_dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The resource ID of the source DB instance from which to restore.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.</p> <p>For more information about this setting, including limitations that apply to it, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling"> Managing capacity automatically with Amazon RDS storage autoscaling</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    enable_customer_owned_ip: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.</p> <p>A <i>CoIP</i> provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.</p> <p>This setting doesn't apply to RDS Custom.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about CoIPs, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing">Customer-owned IP addresses</a> in the <i>Amazon Web Services Outposts User Guide</i>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB instance. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid Values:</p> <ul> <li> <p> <code>IPV4</code> </p> </li> <li> <p> <code>DUAL</code> </p> </li> </ul>"""
    source_db_instance_automated_backups_arn: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replicated automated backups from which to restore, for example, <code>arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE</code>.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    backup_target: NotRequired["capo_rds.types.string.String"]
    """<p>The location for storing automated backups and manual snapshots for the restored DB instance.</p> <p>Valid Values:</p> <ul> <li> <p> <code>local</code> (Dedicated Local Zone)</p> </li> <li> <p> <code>outposts</code> (Amazon Web Services Outposts)</p> </li> <li> <p> <code>region</code> (Amazon Web Services Region)</p> </li> </ul> <p>Default: <code>region</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    custom_iam_instance_profile: NotRequired["capo_rds.types.string.String"]
    """<p>The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:</p> <ul> <li> <p>The profile must exist in your account.</p> </li> <li> <p>The profile must have an IAM role that Amazon EC2 has permissions to assume.</p> </li> <li> <p>The instance profile name and the associated IAM role name must start with the prefix <code>AWSRDSCustom</code>.</p> </li> </ul> <p>For the list of permissions required for the IAM role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc"> Configure IAM and your VPC</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting is required for RDS Custom.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage (in gibibytes) to allocate initially for the DB instance. Follow the allocation rules specified in <code>CreateDBInstance</code>.</p> <p>This setting isn't valid for RDS for SQL Server.</p> <note> <p>Be sure to allocate enough storage for your new DB instance so that the restore operation can succeed. You can also allocate additional storage for future growth.</p> </note>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.</p> <note> <p>Enabling and disabling backups can result in a brief I/O suspension that lasts from a few seconds to a few minutes, depending on the size and class of your DB instance.</p> </note> <p>This setting doesn't apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster. For more information, see <code>ModifyDBCluster</code>.</p> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 0 to 35.</p> </li> <li> <p>Can't be set to 0 if the DB instance is a source to read replicas.</p> </li> <li> <p>Can't be set to 0 for an RDS Custom for Oracle DB instance.</p> </li> </ul>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code> parameter. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow">Backup window</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster. For more information, see <code>ModifyDBCluster</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable a dedicated log volume (DLV) for the DB instance.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the DB instance's server certificate.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB instance.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, RDS automatically upgrades your restored DB instance to a higher engine version, if the major engine version is past its end of standard support date.</p> </note> <p>You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the engine lifecycle support is managed by the DB cluster.</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>A list of additional storage volumes to restore to the DB instance. You can restore up to three additional storage volumes using the names <code>rdsdbdata2</code>, <code>rdsdbdata3</code>, and <code>rdsdbdata4</code>. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.</p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB instance.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> </ul>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager in the restored DB instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Applies to RDS for Oracle only.</p> </li> </ul>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBInstanceToPointInTimeMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBInstanceIdentifier",
                str(value["source_db_instance_identifier"]),
            )
        )
    if "target_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBInstanceIdentifier",
                str(value["target_db_instance_identifier"]),
            )
        )
    if "restore_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["restore_time"], pairs, f"{key_prefix}RestoreTime"
        )
    if "use_latest_restorable_time" in value:
        pairs.append(
            (
                f"{key_prefix}UseLatestRestorableTime",
                "true" if value["use_latest_restorable_time"] else "false",
            )
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
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
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "tde_credential_arn" in value:
        pairs.append(
            (f"{key_prefix}TdeCredentialArn", str(value["tde_credential_arn"]))
        )
    if "tde_credential_password" in value:
        pairs.append(
            (
                f"{key_prefix}TdeCredentialPassword",
                str(value["tde_credential_password"]),
            )
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "domain_iam_role_name" in value:
        pairs.append(
            (f"{key_prefix}DomainIAMRoleName", str(value["domain_iam_role_name"]))
        )
    if "domain_fqdn" in value:
        pairs.append((f"{key_prefix}DomainFqdn", str(value["domain_fqdn"])))
    if "domain_ou" in value:
        pairs.append((f"{key_prefix}DomainOu", str(value["domain_ou"])))
    if "domain_auth_secret_arn" in value:
        pairs.append(
            (f"{key_prefix}DomainAuthSecretArn", str(value["domain_auth_secret_arn"]))
        )
    if "domain_dns_ips" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["domain_dns_ips"], pairs, f"{key_prefix}DomainDnsIps"
        )
    if "enable_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}EnableIAMDatabaseAuthentication",
                "true" if value["enable_iam_database_authentication"] else "false",
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
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "source_dbi_resource_id" in value:
        pairs.append(
            (f"{key_prefix}SourceDbiResourceId", str(value["source_dbi_resource_id"]))
        )
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{key_prefix}MaxAllocatedStorage", str(value["max_allocated_storage"]))
        )
    if "enable_customer_owned_ip" in value:
        pairs.append(
            (
                f"{key_prefix}EnableCustomerOwnedIp",
                "true" if value["enable_customer_owned_ip"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "source_db_instance_automated_backups_arn" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBInstanceAutomatedBackupsArn",
                str(value["source_db_instance_automated_backups_arn"]),
            )
        )
    if "backup_target" in value:
        pairs.append((f"{key_prefix}BackupTarget", str(value["backup_target"])))
    if "custom_iam_instance_profile" in value:
        pairs.append(
            (
                f"{key_prefix}CustomIamInstanceProfile",
                str(value["custom_iam_instance_profile"]),
            )
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
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


def deserialize_query(el: Element) -> RestoreDBInstanceToPointInTimeMessage:
    out: RestoreDBInstanceToPointInTimeMessage = {}  # type: ignore[typeddict-item]
    child_source_db_instance_identifier = el.find("SourceDBInstanceIdentifier")
    if child_source_db_instance_identifier is not None:
        out["source_db_instance_identifier"] = str(
            child_source_db_instance_identifier.text or ""
        )
    child_target_db_instance_identifier = el.find("TargetDBInstanceIdentifier")
    if child_target_db_instance_identifier is not None:
        out["target_db_instance_identifier"] = str(
            child_target_db_instance_identifier.text or ""
        )
    child_restore_time = el.find("RestoreTime")
    if child_restore_time is not None:
        import capo_rds.types.t_stamp

        out["restore_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_restore_time
        )
    child_use_latest_restorable_time = el.find("UseLatestRestorableTime")
    if child_use_latest_restorable_time is not None:
        out["use_latest_restorable_time"] = (
            child_use_latest_restorable_time.text or ""
        ).lower() == "true"
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
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
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_tde_credential_password = el.find("TdeCredentialPassword")
    if child_tde_credential_password is not None:
        out["tde_credential_password"] = str(child_tde_credential_password.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_domain_iam_role_name = el.find("DomainIAMRoleName")
    if child_domain_iam_role_name is not None:
        out["domain_iam_role_name"] = str(child_domain_iam_role_name.text or "")
    child_domain_fqdn = el.find("DomainFqdn")
    if child_domain_fqdn is not None:
        out["domain_fqdn"] = str(child_domain_fqdn.text or "")
    child_domain_ou = el.find("DomainOu")
    if child_domain_ou is not None:
        out["domain_ou"] = str(child_domain_ou.text or "")
    child_domain_auth_secret_arn = el.find("DomainAuthSecretArn")
    if child_domain_auth_secret_arn is not None:
        out["domain_auth_secret_arn"] = str(child_domain_auth_secret_arn.text or "")
    child_domain_dns_ips = el.find("DomainDnsIps")
    if child_domain_dns_ips is not None:
        import capo_rds.types.string_list

        out["domain_dns_ips"] = capo_rds.types.string_list.deserialize_query(
            child_domain_dns_ips
        )
    child_enable_iam_database_authentication = el.find(
        "EnableIAMDatabaseAuthentication"
    )
    if child_enable_iam_database_authentication is not None:
        out["enable_iam_database_authentication"] = (
            child_enable_iam_database_authentication.text or ""
        ).lower() == "true"
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
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_source_dbi_resource_id = el.find("SourceDbiResourceId")
    if child_source_dbi_resource_id is not None:
        out["source_dbi_resource_id"] = str(child_source_dbi_resource_id.text or "")
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
    child_enable_customer_owned_ip = el.find("EnableCustomerOwnedIp")
    if child_enable_customer_owned_ip is not None:
        out["enable_customer_owned_ip"] = (
            child_enable_customer_owned_ip.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_source_db_instance_automated_backups_arn = el.find(
        "SourceDBInstanceAutomatedBackupsArn"
    )
    if child_source_db_instance_automated_backups_arn is not None:
        out["source_db_instance_automated_backups_arn"] = str(
            child_source_db_instance_automated_backups_arn.text or ""
        )
    child_backup_target = el.find("BackupTarget")
    if child_backup_target is not None:
        out["backup_target"] = str(child_backup_target.text or "")
    child_custom_iam_instance_profile = el.find("CustomIamInstanceProfile")
    if child_custom_iam_instance_profile is not None:
        out["custom_iam_instance_profile"] = str(
            child_custom_iam_instance_profile.text or ""
        )
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
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
    return out

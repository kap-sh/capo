"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBInstanceReadReplicaMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.boolean_optional
    import capo_rds.types.database_insights_mode
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.processor_feature_list
    import capo_rds.types.replica_mode
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class CreateDBInstanceReadReplicaMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance identifier of the read replica. This identifier is the unique key that identifies a DB instance. This parameter is stored as a lowercase string.</p>"""
    source_db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the DB instance that will act as the source for the read replica. Each DB instance can have up to 15 read replicas, except for the following engines:</p> <ul> <li> <p>Db2 - Can have up to three replicas.</p> </li> <li> <p>Oracle - Can have up to five read replicas.</p> </li> <li> <p>SQL Server - Can have up to five read replicas.</p> </li> </ul> <p>Constraints:</p> <ul> <li> <p>Must be the identifier of an existing Db2, MariaDB, MySQL, Oracle, PostgreSQL, or SQL Server DB instance.</p> </li> <li> <p>Can't be specified if the <code>SourceDBClusterIdentifier</code> parameter is also specified.</p> </li> <li> <p>For the limitations of Oracle read replicas, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.limitations.html#oracle-read-replicas.limitations.versions-and-licenses">Version and licensing considerations for RDS for Oracle replicas</a> in the <i>Amazon RDS User Guide</i>.</p> </li> <li> <p>For the limitations of SQL Server read replicas, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.html#SQLServer.ReadReplicas.Limitations">Read replica limitations with SQL Server</a> in the <i>Amazon RDS User Guide</i>.</p> </li> <li> <p>The specified DB instance must have automatic backups enabled, that is, its backup retention period must be greater than 0.</p> </li> <li> <p>If the source DB instance is in the same Amazon Web Services Region as the read replica, specify a valid DB instance identifier.</p> </li> <li> <p>If the source DB instance is in a different Amazon Web Services Region from the read replica, specify a valid DB instance ARN. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing">Constructing an ARN for Amazon RDS</a> in the <i>Amazon RDS User Guide</i>. This doesn't apply to SQL Server or RDS Custom, which don't support cross-Region replicas.</p> </li> </ul>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of the read replica, for example db.m4.large. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB Instance Class</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Default: Inherits the value from the source DB instance.</p>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The Availability Zone (AZ) where the read replica will be created.</p> <p>Default: A random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region.</p> <p>Example: <code>us-east-1d</code> </p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number that the DB instance uses for connections.</p> <p>Valid Values: <code>1150-65535</code> </p> <p>Default: Inherits the value from the source DB instance.</p>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the read replica is in a Multi-AZ deployment.</p> <p>You can create a read replica as a Multi-AZ DB instance. RDS creates a standby of your replica in another Availability Zone for failover support for the replica. Creating your read replica as a Multi-AZ DB instance is independent of whether the source is a Multi-AZ DB instance or a Multi-AZ DB cluster.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to automatically apply minor engine upgrades to the read replica during the maintenance window.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Default: Inherits the value from the source DB instance.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Specifies the storage throughput value for the read replica.</p> <p>This setting doesn't apply to RDS Custom or Amazon Aurora DB instances.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group to associate the DB instance with. If not specified, RDS uses the option group associated with the source DB instance or cluster.</p> <note> <p>For SQL Server, you must use the option group associated with the source.</p> </note> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group to associate with this read replica DB instance.</p> <p>For the Db2 DB engine, if your source DB instance uses the bring your own license (BYOL) model, then a custom parameter group must be associated with the replica. For a same Amazon Web Services Region replica, if you don't specify a custom parameter group, Amazon RDS associates the custom parameter group associated with the source DB instance. For a cross-Region replica, you must specify a custom parameter group. This custom parameter group must include your IBM Site ID and IBM Customer ID. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html#db2-prereqs-ibm-info">IBM IDs for bring your own license (BYOL) for Db2</a>. </p> <p>For Single-AZ or Multi-AZ DB instance read replica instances, if you don't specify a value for <code>DBParameterGroupName</code>, then Amazon RDS uses the <code>DBParameterGroup</code> of the source DB instance for a same Region read replica, or the default <code>DBParameterGroup</code> for the specified DB engine for a cross-Region read replica.</p> <p>For Multi-AZ DB cluster same Region read replica instances, if you don't specify a value for <code>DBParameterGroupName</code>, then Amazon RDS uses the default <code>DBParameterGroup</code>.</p> <p>Specifying a parameter group for this operation is only supported for MySQL DB instances for cross-Region read replicas, for Multi-AZ DB cluster read replica instances, for Db2 DB instances, and for Oracle DB instances. It isn't supported for MySQL DB instances for same Region read replicas or for RDS Custom.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is publicly accessible.</p> <p>When the DB cluster is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB cluster's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB cluster's VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p> <p>For more information, see <a>CreateDBInstance</a>.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>A DB subnet group for the DB instance. The new DB instance is created in the VPC associated with the DB subnet group. If no DB subnet group is specified, then the new DB instance isn't created in a VPC.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DB subnet group.</p> </li> <li> <p>The specified DB subnet group must be in the same Amazon Web Services Region in which the operation is running.</p> </li> <li> <p>All read replicas in one Amazon Web Services Region that are created from the same source DB instance must either:</p> <ul> <li> <p>Specify DB subnet groups from the same VPC. All these read replicas are created in the same VPC.</p> </li> <li> <p>Not specify a DB subnet group. All these read replicas are created outside of any VPC.</p> </li> </ul> </li> </ul> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of Amazon EC2 VPC security groups to associate with the read replica.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Default: The default EC2 VPC security group for the DB subnet group's VPC.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type to associate with the read replica.</p> <p>If you specify <code>io1</code>, <code>io2</code>, or <code>gp3</code>, you must also include a value for the <code>Iops</code> parameter.</p> <p>Valid Values: <code>gp2 | gp3 | io1 | io2 | standard</code> </p> <p>Default: <code>io1</code> if the <code>Iops</code> parameter is specified. Otherwise, <code>gp3</code>.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the read replica to snapshots of the read replica. By default, tags aren't copied.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the read replica. To disable collection of Enhanced Monitoring metrics, specify <code>0</code>. The default is <code>0</code>.</p> <p>If <code>MonitoringRoleArn</code> is specified, then you must set <code>MonitoringInterval</code> to a value other than <code>0</code>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values: <code>0, 1, 5, 10, 15, 30, 60</code> </p> <p>Default: <code>0</code> </p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, go to <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole">To create an IAM role for Amazon RDS Enhanced Monitoring</a> in the <i>Amazon RDS User Guide</i>.</p> <p>If <code>MonitoringInterval</code> is set to a value other than 0, then you must supply a <code>MonitoringRoleArn</code> value.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted read replica.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you create an encrypted read replica in the same Amazon Web Services Region as the source DB instance or Multi-AZ DB cluster, don't specify a value for this parameter. A read replica in the same Amazon Web Services Region is always encrypted with the same KMS key as the source DB instance or cluster.</p> <p>If you create an encrypted read replica in a different Amazon Web Services Region, then you must specify a KMS key identifier for the destination Amazon Web Services Region. KMS keys are specific to the Amazon Web Services Region that they are created in, and you can't use KMS keys from one Amazon Web Services Region in another Amazon Web Services Region.</p> <p>You can't create an encrypted read replica from an unencrypted DB instance or Multi-AZ DB cluster.</p> <p>This setting doesn't apply to RDS Custom, which uses the same KMS key as the primary replica.</p>"""
    pre_signed_url: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>When you are creating a read replica from one Amazon Web Services GovCloud (US) Region to another or from one China Amazon Web Services Region to another, the URL that contains a Signature Version 4 signed request for the <code>CreateDBInstanceReadReplica</code> API operation in the source Amazon Web Services Region that contains the source DB instance.</p> <p>This setting applies only to Amazon Web Services GovCloud (US) Regions and China Amazon Web Services Regions. It's ignored in other Amazon Web Services Regions.</p> <p>This setting applies only when replicating from a source DB <i>instance</i>. Source DB clusters aren't supported in Amazon Web Services GovCloud (US) Regions and China Amazon Web Services Regions.</p> <p>You must specify this parameter when you create an encrypted read replica from another Amazon Web Services Region by using the Amazon RDS API. Don't specify <code>PreSignedUrl</code> when you are creating an encrypted read replica in the same Amazon Web Services Region.</p> <p>The presigned URL must be a valid request for the <code>CreateDBInstanceReadReplica</code> API operation that can run in the source Amazon Web Services Region that contains the encrypted source DB instance. The presigned URL request must contain the following parameter values:</p> <ul> <li> <p> <code>DestinationRegion</code> - The Amazon Web Services Region that the encrypted read replica is created in. This Amazon Web Services Region is the same one where the <code>CreateDBInstanceReadReplica</code> operation is called that contains this presigned URL.</p> <p>For example, if you create an encrypted DB instance in the us-west-1 Amazon Web Services Region, from a source DB instance in the us-east-2 Amazon Web Services Region, then you call the <code>CreateDBInstanceReadReplica</code> operation in the us-east-1 Amazon Web Services Region and provide a presigned URL that contains a call to the <code>CreateDBInstanceReadReplica</code> operation in the us-west-2 Amazon Web Services Region. For this example, the <code>DestinationRegion</code> in the presigned URL must be set to the us-east-1 Amazon Web Services Region.</p> </li> <li> <p> <code>KmsKeyId</code> - The KMS key identifier for the key to use to encrypt the read replica in the destination Amazon Web Services Region. This is the same identifier for both the <code>CreateDBInstanceReadReplica</code> operation that is called in the destination Amazon Web Services Region, and the operation contained in the presigned URL.</p> </li> <li> <p> <code>SourceDBInstanceIdentifier</code> - The DB instance identifier for the encrypted DB instance to be replicated. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are creating an encrypted read replica from a DB instance in the us-west-2 Amazon Web Services Region, then your <code>SourceDBInstanceIdentifier</code> looks like the following example: <code>arn:aws:rds:us-west-2:123456789012:instance:mysql-instance1-20161115</code>.</p> </li> </ul> <p>To learn how to generate a Signature Version 4 signed request, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html">Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 Signing Process</a>.</p> <note> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.</p> </note> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information about IAM database authentication, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication for MySQL and PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>The mode of Database Insights to enable for the read replica.</p> <note> <p>This setting isn't supported.</p> </note>"""
    enable_performance_insights: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable Performance Insights for the read replica.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html">Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you do not specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p> <p>If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS returns an error.</p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of logs that the new DB instance is to export to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs </a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    use_default_processor_features: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance class of the DB instance uses its default processor features.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable deletion protection for the DB instance. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"> Deleting a DB Instance</a>.</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html"> Kerberos Authentication</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    domain_fqdn: NotRequired["capo_rds.types.string.String"]
    """<p>The fully qualified domain name (FQDN) of an Active Directory domain.</p> <p>Constraints:</p> <ul> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>mymanagedADtest.mymanagedAD.mydomain</code> </p>"""
    domain_ou: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory organizational unit for your DB instance to join.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the distinguished name format.</p> </li> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain</code> </p>"""
    domain_auth_secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the Secrets Manager secret with the credentials for the user joining the domain.</p> <p>Example: <code>arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456</code> </p>"""
    domain_dns_ips: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.</p> <p>Constraints:</p> <ul> <li> <p>Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.</p> </li> </ul> <p>Example: <code>123.124.125.126,234.235.236.237</code> </p>"""
    replica_mode: NotRequired["capo_rds.types.replica_mode.ReplicaMode"]
    """<p>The open mode of the replica database.</p> <p>This parameter is only supported for Db2 DB instances and Oracle DB instances.</p> <dl> <dt>Db2</dt> <dd> <p>Standby DB replicas are included in Db2 Advanced Edition (AE), Db2 Community Edition (CE), and Db2 Standard Edition (SE). The main use case for standby replicas is cross-Region disaster recovery. Because it doesn't accept user connections, a standby replica can't serve a read-only workload.</p> <p>You can create a combination of standby and read-only DB replicas for the same primary DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replication.html">Working with replicas for Amazon RDS for Db2</a> in the <i>Amazon RDS User Guide</i>.</p> <p>To create standby DB replicas for RDS for Db2, set this parameter to <code>mounted</code>.</p> </dd> <dt>Oracle</dt> <dd> <p>Mounted DB replicas are included in Oracle Database Enterprise Edition. The main use case for mounted replicas is cross-Region disaster recovery. The primary database doesn't use Active Data Guard to transmit information to the mounted replica. Because it doesn't accept user connections, a mounted replica can't serve a read-only workload.</p> <p>You can create a combination of mounted and read-only DB replicas for the same primary DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html">Working with read replicas for Amazon RDS for Oracle</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For RDS Custom, you must specify this parameter and set it to <code>mounted</code>. The value won't be set by default. After replica creation, you can manage the open mode manually.</p> </dd> </dl>"""
    enable_customer_owned_ip: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts read replica.</p> <p>A <i>CoIP</i> provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the read replica from outside of its virtual private cloud (VPC) on your local network.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about CoIPs, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing">Customer-owned IP addresses</a> in the <i>Amazon Web Services Outposts User Guide</i>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>Valid Values:</p> <ul> <li> <p> <code>IPV4</code> </p> </li> <li> <p> <code>DUAL</code> </p> </li> </ul> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for read replica. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.</p> <p>For more information about this setting, including limitations that apply to it, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling"> Managing capacity automatically with Amazon RDS storage autoscaling</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    backup_target: NotRequired["capo_rds.types.string.String"]
    """<p>The location where RDS stores automated backups and manual snapshots.</p> <p>Valid Values:</p> <ul> <li> <p> <code>local</code> for Dedicated Local Zones</p> </li> <li> <p> <code>region</code> for Amazon Web Services Region</p> </li> </ul>"""
    custom_iam_instance_profile: NotRequired["capo_rds.types.string.String"]
    """<p>The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:</p> <ul> <li> <p>The profile must exist in your account.</p> </li> <li> <p>The profile must have an IAM role that Amazon EC2 has permissions to assume.</p> </li> <li> <p>The instance profile name and the associated IAM role name must start with the prefix <code>AWSRDSCustom</code>.</p> </li> </ul> <p>For the list of permissions required for the IAM role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc"> Configure IAM and your VPC</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting is required for RDS Custom DB instances.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage (in gibibytes) to allocate initially for the read replica. Follow the allocation rules specified in <code>CreateDBInstance</code>.</p> <p>This setting isn't valid for RDS for SQL Server.</p> <note> <p>Be sure to allocate enough storage for your read replica so that the create operation can succeed. You can also allocate additional storage for future growth.</p> </note>"""
    source_db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.</p> <p>Constraints:</p> <ul> <li> <p>Must be the identifier of an existing Multi-AZ DB cluster.</p> </li> <li> <p>Can't be specified if the <code>SourceDBInstanceIdentifier</code> parameter is also specified.</p> </li> <li> <p>The specified DB cluster must have automatic backups enabled, that is, its backup retention period must be greater than 0.</p> </li> <li> <p>The source DB cluster must be in the same Amazon Web Services Region as the read replica. Cross-Region replication isn't supported.</p> </li> </ul>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</p>"""
    upgrade_storage_config: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to upgrade the storage file system configuration on the read replica. This option migrates the read replica from the old storage file system layout to the preferred layout.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the read replica's server certificate.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>A list of additional storage volumes to create for the DB instance. You can create up to three additional storage volumes using the names <code>rdsdbdata2</code>, <code>rdsdbdata3</code>, and <code>rdsdbdata4</code>. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.</p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB instance.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBInstanceReadReplicaMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "source_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBInstanceIdentifier",
                str(value["source_db_instance_identifier"]),
            )
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
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
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
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
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "pre_signed_url" in value:
        pairs.append((f"{key_prefix}PreSignedUrl", str(value["pre_signed_url"])))
    if "enable_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}EnableIAMDatabaseAuthentication",
                "true" if value["enable_iam_database_authentication"] else "false",
            )
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
    if "replica_mode" in value:
        import capo_rds.types.replica_mode

        capo_rds.types.replica_mode.serialize_query(
            value["replica_mode"], pairs, f"{key_prefix}ReplicaMode"
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
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{key_prefix}MaxAllocatedStorage", str(value["max_allocated_storage"]))
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
    if "source_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterIdentifier",
                str(value["source_db_cluster_identifier"]),
            )
        )
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "upgrade_storage_config" in value:
        pairs.append(
            (
                f"{key_prefix}UpgradeStorageConfig",
                "true" if value["upgrade_storage_config"] else "false",
            )
        )
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
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


def deserialize_query(el: Element) -> CreateDBInstanceReadReplicaMessage:
    out: CreateDBInstanceReadReplicaMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_source_db_instance_identifier = el.find("SourceDBInstanceIdentifier")
    if child_source_db_instance_identifier is not None:
        out["source_db_instance_identifier"] = str(
            child_source_db_instance_identifier.text or ""
        )
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
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
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_pre_signed_url = el.find("PreSignedUrl")
    if child_pre_signed_url is not None:
        out["pre_signed_url"] = str(child_pre_signed_url.text or "")
    child_enable_iam_database_authentication = el.find(
        "EnableIAMDatabaseAuthentication"
    )
    if child_enable_iam_database_authentication is not None:
        out["enable_iam_database_authentication"] = (
            child_enable_iam_database_authentication.text or ""
        ).lower() == "true"
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
    child_replica_mode = el.find("ReplicaMode")
    if child_replica_mode is not None:
        import capo_rds.types.replica_mode

        out["replica_mode"] = capo_rds.types.replica_mode.deserialize_query(
            child_replica_mode
        )
    child_enable_customer_owned_ip = el.find("EnableCustomerOwnedIp")
    if child_enable_customer_owned_ip is not None:
        out["enable_customer_owned_ip"] = (
            child_enable_customer_owned_ip.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
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
    child_source_db_cluster_identifier = el.find("SourceDBClusterIdentifier")
    if child_source_db_cluster_identifier is not None:
        out["source_db_cluster_identifier"] = str(
            child_source_db_cluster_identifier.text or ""
        )
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_upgrade_storage_config = el.find("UpgradeStorageConfig")
    if child_upgrade_storage_config is not None:
        out["upgrade_storage_config"] = (
            child_upgrade_storage_config.text or ""
        ).lower() == "true"
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
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

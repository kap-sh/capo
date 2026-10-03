"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zones
    import capo_rds.types.boolean_optional
    import capo_rds.types.cluster_scalability_type
    import capo_rds.types.database_insights_mode
    import capo_rds.types.db_cluster_associated_roles
    import capo_rds.types.global_cluster_identifier
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.long_optional
    import capo_rds.types.master_user_authentication_type
    import capo_rds.types.rds_custom_cluster_configuration
    import capo_rds.types.scaling_configuration
    import capo_rds.types.sensitive_string
    import capo_rds.types.serverless_v2_scaling_configuration
    import capo_rds.types.string
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class CreateDBClusterMessage(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>A list of Availability Zones (AZs) where you specifically want to create DB instances in the DB cluster.</p> <p>For the first three DB instances that you create, RDS distributes each DB instance to a different AZ that you specify. For additional DB instances that you create, RDS randomly distributes them to the AZs that you specified. For example, if you create a DB cluster with one writer instance and three reader instances, RDS might distribute the writer instance to AZ 1, the first reader instance to AZ 2, the second reader instance to AZ 3, and the third reader instance to either AZ 1, AZ 2, or AZ 3. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.AvailabilityZones">Availability Zones</a> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Concepts.AuroraHighAvailability.Instances">High availability for Aurora DB instances</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p> <p>Constraints:</p> <ul> <li> <p>Can't specify more than three AZs.</p> </li> </ul>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Default: <code>1</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35.</p> </li> </ul>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the character set (<code>CharacterSet</code>) to associate the DB cluster with.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    database_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name for your database of up to 64 alphanumeric characters. A database named <code>postgres</code> is always created. If this parameter is specified, an additional database with this name is created.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for this DB cluster. This parameter is stored as a lowercase string.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 (for Aurora DB clusters) or 1 to 52 (for Multi-AZ DB clusters) letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>"""
    db_cluster_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group to associate with this DB cluster. If you don't specify a value, then the default DB cluster parameter group for the specified DB engine and version is used.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DB cluster parameter group.</p> </li> </ul>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of EC2 VPC security groups to associate with this DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>A DB subnet group to associate with this DB cluster.</p> <p>This setting is required to create a Multi-AZ DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DB subnet group.</p> </li> </ul> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine to use for this DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>neptune</code> - For information about using Amazon Neptune, see the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/intro.html"> <i>Amazon Neptune User Guide</i> </a>.</p> </li> </ul>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to use.</p> <p>To list all of the available engine versions for Aurora MySQL version 2 (5.7-compatible) and version 3 (MySQL 8.0-compatible), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>You can supply either <code>5.7</code> or <code>8.0</code> to use the default engine version for Aurora MySQL version 2 or version 3, respectively.</p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query "DBEngineVersions[].EngineVersion"</code> </p> <p>For information about a specific engine, see the following topics:</p> <ul> <li> <p>Aurora MySQL - see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html">Database engine updates for Amazon Aurora MySQL</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> <li> <p>Aurora PostgreSQL - see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html">Amazon Aurora PostgreSQL releases and engine versions</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> <li> <p>RDS for MySQL - see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt">Amazon RDS for MySQL</a> in the <i>Amazon RDS User Guide</i>.</p> </li> <li> <p>RDS for PostgreSQL - see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts">Amazon RDS for PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the instances in the DB cluster accept connections.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values: <code>1150-65535</code> </p> <p>Default:</p> <ul> <li> <p>RDS for MySQL and Aurora MySQL - <code>3306</code> </p> </li> <li> <p>RDS for PostgreSQL and Aurora PostgreSQL - <code>5432</code> </p> </li> </ul>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the master user for the DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 16 letters or numbers.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> </li> </ul>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The password for the master database user.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 8 to 41 characters.</p> </li> <li> <p>Can contain any printable ASCII character except \"/\", \"\"\", or \"@\".</p> </li> <li> <p>Can't be specified if <code>ManageMasterUserPassword</code> is turned on.</p> </li> </ul>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group to associate the DB cluster with.</p> <p>DB clusters are associated with a default option group that can't be modified.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled using the <code>BackupRetentionPeriod</code> parameter.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. To view the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow"> Backup window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. To see the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora"> Adjusting the Preferred DB Cluster Maintenance Window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>ddd:hh24:mi-ddd:hh24:mi</code>.</p> </li> <li> <p>Days must be one of <code>Mon | Tue | Wed | Thu | Fri | Sat | Sun</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    replication_source_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a read replica.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB cluster is encrypted.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>When a KMS key isn't specified in <code>KmsKeyId</code>:</p> <ul> <li> <p>If <code>ReplicationSourceIdentifier</code> identifies an encrypted source, then Amazon RDS uses the KMS key used to encrypt the source. Otherwise, Amazon RDS uses your default KMS key.</p> </li> <li> <p>If the <code>StorageEncrypted</code> parameter is enabled and <code>ReplicationSourceIdentifier</code> isn't specified, then Amazon RDS uses your default KMS key.</p> </li> </ul> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>If you create a read replica of an encrypted DB cluster in another Amazon Web Services Region, make sure to set <code>KmsKeyId</code> to a KMS key identifier that is valid in the destination Amazon Web Services Region. This KMS key is used to encrypt the read replica in that Amazon Web Services Region.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    pre_signed_url: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>When you are replicating a DB cluster from one Amazon Web Services GovCloud (US) Region to another, an URL that contains a Signature Version 4 signed request for the <code>CreateDBCluster</code> operation to be called in the source Amazon Web Services Region where the DB cluster is replicated from. Specify <code>PreSignedUrl</code> only when you are performing cross-Region replication from an encrypted DB cluster.</p> <p>The presigned URL must be a valid request for the <code>CreateDBCluster</code> API operation that can run in the source Amazon Web Services Region that contains the encrypted DB cluster to copy.</p> <p>The presigned URL request must contain the following parameter values:</p> <ul> <li> <p> <code>KmsKeyId</code> - The KMS key identifier for the KMS key to use to encrypt the copy of the DB cluster in the destination Amazon Web Services Region. This should refer to the same KMS key for both the <code>CreateDBCluster</code> operation that is called in the destination Amazon Web Services Region, and the operation contained in the presigned URL.</p> </li> <li> <p> <code>DestinationRegion</code> - The name of the Amazon Web Services Region that Aurora read replica will be created in.</p> </li> <li> <p> <code>ReplicationSourceIdentifier</code> - The DB cluster identifier for the encrypted DB cluster to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted DB cluster from the us-west-2 Amazon Web Services Region, then your <code>ReplicationSourceIdentifier</code> would look like Example: <code>arn:aws:rds:us-west-2:123456789012:cluster:aurora-cluster1</code>.</p> </li> </ul> <p>To learn how to generate a Signature Version 4 signed request, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html"> Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"> Signature Version 4 Signing Process</a>.</p> <note> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.</p> </note> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication</a> in the <i>Amazon Aurora User Guide</i> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html">IAM database authentication for MariaDB, MySQL, and PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    backtrack_window: NotRequired["capo_rds.types.long_optional.LongOptional"]
    """<p>The target backtrack window, in seconds. To disable backtracking, set this value to <code>0</code>.</p> <p>Valid for Cluster Type: Aurora MySQL DB clusters only</p> <p>Default: <code>0</code> </p> <p>Constraints:</p> <ul> <li> <p>If specified, this value must be set to a number from 0 to 259,200 (72 hours).</p> </li> </ul>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of log types that need to be enabled for exporting to CloudWatch Logs.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>The following values are valid for each DB engine:</p> <ul> <li> <p>Aurora MySQL - <code>audit | error | general | instance | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>Aurora PostgreSQL - <code>instance | postgresql | iam-db-auth-error</code> </p> </li> <li> <p>RDS for MySQL - <code>error | general | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql | upgrade | iam-db-auth-error</code> </p> </li> </ul> <p>For more information about exporting CloudWatch Logs for Amazon RDS, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    engine_mode: NotRequired["capo_rds.types.string.String"]
    """<p>The DB engine mode of the DB cluster, either <code>provisioned</code> or <code>serverless</code>.</p> <p>The <code>serverless</code> engine mode only applies for Aurora Serverless v1 DB clusters. Aurora Serverless v2 DB clusters use the <code>provisioned</code> engine mode.</p> <p>For information about limitations and requirements for Serverless DB clusters, see the following sections in the <i>Amazon Aurora User Guide</i>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html#aurora-serverless.limitations">Limitations of Aurora Serverless v1</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html">Requirements for Aurora Serverless v2</a> </p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    scaling_configuration: NotRequired[
        "capo_rds.types.scaling_configuration.ScalingConfiguration"
    ]
    """<p>For DB clusters in <code>serverless</code> DB engine mode, the scaling properties of the DB cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    rds_custom_cluster_configuration: NotRequired[
        "capo_rds.types.rds_custom_cluster_configuration.RdsCustomClusterConfiguration"
    ]
    """<p>Reserved for future use.</p>"""
    db_cluster_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example <code>db.m6gd.xlarge</code>. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines.</p> <p>For the full list of DB instance classes and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB instance class</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting is required to create a Multi-AZ DB cluster.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p> <p>This setting is required to create a Multi-AZ DB cluster.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Aurora DB clusters, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#aurora-storage-type">Storage configurations for Amazon Aurora DB clusters</a>. For information on storage types for Multi-AZ DB clusters, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html#create-multi-az-db-cluster-settings">Settings for creating Multi-AZ DB clusters</a>.</p> <p>This setting is required to create a Multi-AZ DB cluster.</p> <p>When specified for a Multi-AZ DB cluster, a value for the <code>Iops</code> parameter is required.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values:</p> <ul> <li> <p>Aurora DB clusters - <code>aurora | aurora-iopt1</code> </p> </li> <li> <p>Multi-AZ DB clusters - <code>io1 | io2 | gp3</code> </p> </li> </ul> <p>Default:</p> <ul> <li> <p>Aurora DB clusters - <code>aurora</code> </p> </li> <li> <p>Multi-AZ DB clusters - <code>io1</code> </p> </li> </ul> <note> <p>When you create an Aurora DB cluster with the storage type set to <code>aurora-iopt1</code>, the storage type is returned in the response. The storage type isn't returned when you set it to <code>aurora</code>.</p> </note>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS">Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting is required to create a Multi-AZ DB cluster.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p> <p>Constraints:</p> <ul> <li> <p>Must be a multiple between .5 and 50 of the storage amount for the DB cluster.</p> </li> </ul>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB cluster is publicly accessible.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters only</p> <p>When the DB cluster is publicly accessible and you connect from outside of the DB cluster's virtual private cloud (VPC), its domain name system (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB cluster, the endpoint resolves to the private IP address. Access to the DB cluster is controlled by its security group settings.</p> <p>When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.</p> <p>The default behavior when <code>PubliclyAccessible</code> is not specified depends on whether a <code>DBSubnetGroup</code> is specified.</p> <p>If <code>DBSubnetGroup</code> isn't specified, <code>PubliclyAccessible</code> defaults to <code>true</code>.</p> <p>If <code>DBSubnetGroup</code> is specified, <code>PubliclyAccessible</code> defaults to <code>false</code> unless the value of <code>DBSubnetGroup</code> is <code>default</code>, in which case <code>PubliclyAccessible</code> defaults to <code>true</code>.</p> <p>If <code>PubliclyAccessible</code> is true and the VPC that the <code>DBSubnetGroup</code> is in doesn't have an internet gateway attached to it, Amazon RDS returns an error.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB cluster.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    global_cluster_identifier: NotRequired[
        "capo_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The global cluster ID of an Aurora cluster that becomes the primary cluster in the new global database cluster.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    enable_http_endpoint: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable the HTTP endpoint for the DB cluster. By default, the HTTP endpoint isn't enabled.</p> <p>When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the DB cluster. You can also query your database from inside the RDS console with the RDS query editor.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html">Using RDS Data API</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to create the DB cluster in.</p> <p>For Amazon Aurora DB clusters, Amazon RDS can use Kerberos authentication to authenticate users that connect to the DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html">Kerberos authentication</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    enable_global_write_forwarding: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable this DB cluster to forward write operations to the primary cluster of a global cluster (Aurora global database). By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.</p> <p>You can set this value only on Aurora DB clusters that are members of an Aurora global database. With this parameter enabled, a secondary cluster can forward writes to the current primary cluster, and the resulting changes are replicated back to this cluster. For the primary DB cluster of an Aurora global database, this value is used immediately if the primary is demoted by a global cluster API operation, but it does nothing until then.</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid for Cluster Type: Aurora DB clusters only</p> <p>Valid Values: <code>IPV4 | DUAL</code> </p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_rds.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify <code>0</code>.</p> <p>If <code>MonitoringRoleArn</code> is specified, also set <code>MonitoringInterval</code> to a value other than <code>0</code>.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values: <code>0 | 1 | 5 | 10 | 15 | 30 | 60</code> </p> <p>Default: <code>0</code> </p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling">Setting up and enabling Enhanced Monitoring</a> in the <i>Amazon RDS User Guide</i>.</p> <p>If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, supply a <code>MonitoringRoleArn</code> value.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>The mode of Database Insights to enable for the DB cluster.</p> <p>If you set this value to <code>advanced</code>, you must also set the <code>PerformanceInsightsEnabled</code> parameter to <code>true</code> and the <code>PerformanceInsightsRetentionPeriod</code> parameter to 465.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
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
    enable_limitless_database: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable Aurora Limitless Database. You must enable Aurora Limitless Database to create a DB shard group.</p> <p>Valid for: Aurora DB clusters only</p> <note> <p>This setting is no longer used. Instead use the <code>ClusterScalabilityType</code> setting.</p> </note>"""
    cluster_scalability_type: NotRequired[
        "capo_rds.types.cluster_scalability_type.ClusterScalabilityType"
    ]
    """<p>Specifies the scalability mode of the Aurora DB cluster. When set to <code>limitless</code>, the cluster operates as an Aurora Limitless Database. When set to <code>standard</code> (the default), the cluster uses normal DB instance creation.</p> <p>Valid for: Aurora DB clusters only</p> <note> <p>You can't modify this setting after you create the DB cluster.</p> </note>"""
    db_system_id: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Constraints:</p> <ul> <li> <p>Can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p> </li> </ul>"""
    enable_local_write_forwarding: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether read replicas can forward write operations to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.</p> <p>Valid for: Aurora DB clusters only</p>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the DB cluster's server certificate.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for Cluster Type: Multi-AZ DB clusters</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB cluster.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, creating the DB cluster will fail if the DB major version is past its end of standard support date.</p> </note> <p>You can use this setting to enroll your DB cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:</p> <ul> <li> <p>Amazon Aurora - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html">Amazon RDS Extended Support with Amazon Aurora</a> in the <i>Amazon Aurora User Guide</i> </p> </li> <li> <p>Amazon RDS - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i> </p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB cluster.</p> <p>Valid Values: </p> <ul> <li> <p> <code>cluster-auto-backup</code> - The DB cluster's automated backup.</p> </li> </ul>"""
    master_user_authentication_type: NotRequired[
        "capo_rds.types.master_user_authentication_type.MasterUserAuthenticationType"
    ]
    """<p>Specifies the authentication type for the master user. With IAM master user authentication, you can configure the master DB user with IAM database authentication when you create a DB cluster.</p> <p>You can specify one of the following values:</p> <ul> <li> <p> <code>password</code> - Use standard database authentication with a password.</p> </li> <li> <p> <code>iam-db-auth</code> - Use IAM database authentication for the master user.</p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.</p>"""
    with_express_configuration: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies to create an Aurora DB Cluster with express configuration in seconds. Express configuration provides a cluster with a writer instance and feature specific values set to all other input parameters of this API. </p> <p>Valid for Cluster Type: Aurora DB clusters</p>"""
    associated_roles: NotRequired[
        "capo_rds.types.db_cluster_associated_roles.DBClusterAssociatedRoles"
    ]
    """<p>A list of Amazon Web Services Identity and Access Management (IAM) roles to associate with the DB cluster. Each role grants the DB cluster permission to access other Amazon Web Services on your behalf. For each role, specify a role ARN and, optionally, the feature name (such as <code>s3Import</code>, <code>s3Export</code>, or <code>Lambda</code>).</p> <p>Valid for Cluster Type: Aurora DB clusters only</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
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
    if "replication_source_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}ReplicationSourceIdentifier",
                str(value["replication_source_identifier"]),
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
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
    if "pre_signed_url" in value:
        pairs.append((f"{key_prefix}PreSignedUrl", str(value["pre_signed_url"])))
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
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
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
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
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
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "domain_iam_role_name" in value:
        pairs.append(
            (f"{key_prefix}DomainIAMRoleName", str(value["domain_iam_role_name"]))
        )
    if "enable_global_write_forwarding" in value:
        pairs.append(
            (
                f"{key_prefix}EnableGlobalWriteForwarding",
                "true" if value["enable_global_write_forwarding"] else "false",
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
    if "enable_limitless_database" in value:
        pairs.append(
            (
                f"{key_prefix}EnableLimitlessDatabase",
                "true" if value["enable_limitless_database"] else "false",
            )
        )
    if "cluster_scalability_type" in value:
        import capo_rds.types.cluster_scalability_type

        capo_rds.types.cluster_scalability_type.serialize_query(
            value["cluster_scalability_type"],
            pairs,
            f"{key_prefix}ClusterScalabilityType",
        )
    if "db_system_id" in value:
        pairs.append((f"{key_prefix}DBSystemId", str(value["db_system_id"])))
    if "manage_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}ManageMasterUserPassword",
                "true" if value["manage_master_user_password"] else "false",
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
    if "tag_specifications" in value:
        import capo_rds.types.tag_specification_list

        capo_rds.types.tag_specification_list.serialize_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "master_user_authentication_type" in value:
        import capo_rds.types.master_user_authentication_type

        capo_rds.types.master_user_authentication_type.serialize_query(
            value["master_user_authentication_type"],
            pairs,
            f"{key_prefix}MasterUserAuthenticationType",
        )
    if "with_express_configuration" in value:
        pairs.append(
            (
                f"{key_prefix}WithExpressConfiguration",
                "true" if value["with_express_configuration"] else "false",
            )
        )
    if "associated_roles" in value:
        import capo_rds.types.db_cluster_associated_roles

        capo_rds.types.db_cluster_associated_roles.serialize_query(
            value["associated_roles"], pairs, f"{key_prefix}AssociatedRoles"
        )


def deserialize_query(el: Element) -> CreateDBClusterMessage:
    out: CreateDBClusterMessage = {}  # type: ignore[typeddict-item]
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
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
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
    child_replication_source_identifier = el.find("ReplicationSourceIdentifier")
    if child_replication_source_identifier is not None:
        out["replication_source_identifier"] = str(
            child_replication_source_identifier.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
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
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
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
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
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
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_domain_iam_role_name = el.find("DomainIAMRoleName")
    if child_domain_iam_role_name is not None:
        out["domain_iam_role_name"] = str(child_domain_iam_role_name.text or "")
    child_enable_global_write_forwarding = el.find("EnableGlobalWriteForwarding")
    if child_enable_global_write_forwarding is not None:
        out["enable_global_write_forwarding"] = (
            child_enable_global_write_forwarding.text or ""
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
    child_enable_limitless_database = el.find("EnableLimitlessDatabase")
    if child_enable_limitless_database is not None:
        out["enable_limitless_database"] = (
            child_enable_limitless_database.text or ""
        ).lower() == "true"
    child_cluster_scalability_type = el.find("ClusterScalabilityType")
    if child_cluster_scalability_type is not None:
        import capo_rds.types.cluster_scalability_type

        out["cluster_scalability_type"] = (
            capo_rds.types.cluster_scalability_type.deserialize_query(
                child_cluster_scalability_type
            )
        )
    child_db_system_id = el.find("DBSystemId")
    if child_db_system_id is not None:
        out["db_system_id"] = str(child_db_system_id.text or "")
    child_manage_master_user_password = el.find("ManageMasterUserPassword")
    if child_manage_master_user_password is not None:
        out["manage_master_user_password"] = (
            child_manage_master_user_password.text or ""
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
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
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
    child_master_user_authentication_type = el.find("MasterUserAuthenticationType")
    if child_master_user_authentication_type is not None:
        import capo_rds.types.master_user_authentication_type

        out["master_user_authentication_type"] = (
            capo_rds.types.master_user_authentication_type.deserialize_query(
                child_master_user_authentication_type
            )
        )
    child_with_express_configuration = el.find("WithExpressConfiguration")
    if child_with_express_configuration is not None:
        out["with_express_configuration"] = (
            child_with_express_configuration.text or ""
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

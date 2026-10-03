"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBClusterFromS3Message``."""

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
    import capo_rds.types.sensitive_string
    import capo_rds.types.serverless_v2_scaling_configuration
    import capo_rds.types.string
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class RestoreDBClusterFromS3Message(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>A list of Availability Zones (AZs) where instances in the restored DB cluster can be created.</p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups of the restored DB cluster are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35</p> </li> </ul>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>A value that indicates that the restored DB cluster should be associated with the specified CharacterSet.</p>"""
    database_name: NotRequired["capo_rds.types.string.String"]
    """<p>The database name for the restored DB cluster.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster to create from the source data in the Amazon S3 bucket. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>"""
    db_cluster_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group to associate with the restored DB cluster. If this argument is omitted, the default parameter group for the engine version is used.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of EC2 VPC security groups to associate with the restored DB cluster.</p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>A DB subnet group to associate with the restored DB cluster.</p> <p>Constraints: If supplied, must match the name of an existing DBSubnetGroup.</p> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine to be used for this DB cluster.</p> <p>Valid Values: <code>aurora-mysql</code> (for Aurora MySQL)</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to use.</p> <p>To list all of the available engine versions for <code>aurora-mysql</code> (Aurora MySQL), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions[].EngineVersion"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>Examples: <code>5.7.mysql_aurora.2.12.0</code>, <code>8.0.mysql_aurora.3.04.0</code> </p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the instances in the restored DB cluster accept connections.</p> <p>Default: <code>3306</code> </p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the master user for the restored DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 16 letters or numbers.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> </li> </ul>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The password for the master database user. This password can contain any printable ASCII character except \"/\", \"\"\", or \"@\".</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 8 to 41 characters.</p> </li> <li> <p>Can't be specified if <code>ManageMasterUserPassword</code> is turned on.</p> </li> </ul>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>A value that indicates that the restored DB cluster should be associated with the specified option group.</p> <p>Permanent options can't be removed from an option group. An option group can't be removed from a DB cluster once it is associated with a DB cluster.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. To view the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow"> Backup window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. To see the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora"> Adjusting the Preferred Maintenance Window</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> <p>Constraints: Minimum 30-minute window.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    storage_encrypted: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the restored DB cluster is encrypted.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If the StorageEncrypted parameter is enabled, and you do not specify a value for the <code>KmsKeyId</code> parameter, then Amazon RDS will use your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    source_engine: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the database engine that was backed up to create the files stored in the Amazon S3 bucket.</p> <p>Valid Values: <code>mysql</code> </p>"""
    source_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database that the backup files were created from.</p> <p>MySQL versions 5.7 and 8.0 are supported.</p> <p>Example: <code>5.7.40</code>, <code>8.0.28</code> </p>"""
    s3_bucket_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Amazon S3 bucket that contains the data used to create the Amazon Aurora DB cluster.</p>"""
    s3_prefix: NotRequired["capo_rds.types.string.String"]
    """<p>The prefix for all of the file names that contain the data used to create the Amazon Aurora DB cluster. If you do not specify a <b>SourceS3Prefix</b> value, then the Amazon Aurora DB cluster is created by using all of the files in the Amazon S3 bucket.</p>"""
    s3_ingestion_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on your behalf.</p>"""
    backtrack_window: NotRequired["capo_rds.types.long_optional.LongOptional"]
    """<p>The target backtrack window, in seconds. To disable backtracking, set this value to 0.</p> <note> <p>Currently, Backtrack is only supported for Aurora MySQL DB clusters.</p> </note> <p>Default: 0</p> <p>Constraints:</p> <ul> <li> <p>If specified, this value must be set to a number from 0 to 259,200 (72 hours).</p> </li> </ul>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of logs that the restored DB cluster is to export to CloudWatch Logs. The values in the list depend on the DB engine being used.</p> <p> <b>Aurora MySQL</b> </p> <p>Possible values are <code>audit</code>, <code>error</code>, <code>general</code>, <code>instance</code>, <code>slowquery</code>, and <code>iam-db-auth-error</code>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>Possible value are <code>instance</code>, <code>postgresql</code>, and <code>iam-db-auth-error</code>.</p> <p>For more information about exporting CloudWatch Logs for Amazon RDS, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable deletion protection for the DB cluster. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the restored DB cluster to snapshots of the restored DB cluster. The default is not to copy them.</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>Specify the Active Directory directory ID to restore the DB cluster in. The domain must be created prior to this operation.</p> <p>For Amazon Aurora DB clusters, Amazon RDS can use Kerberos Authentication to authenticate users that connect to the DB cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html">Kerberos Authentication</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>Specify the name of the IAM role to be used when making API calls to the Directory Service.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the storage type to be associated with the DB cluster.</p> <p>Valid Values: <code>aurora</code>, <code>aurora-iopt1</code> </p> <p>Default: <code>aurora</code> </p> <p>Valid for: Aurora DB clusters only</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <code>IPV4</code> </p> </li> <li> <p> <code>DUAL</code> </p> </li> </ul> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon Aurora User Guide.</i> </p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_rds.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon Aurora User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p> </li> </ul>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB cluster.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, RDS automatically upgrades your restored DB cluster to a higher engine version, if the major engine version is past its end of standard support date.</p> </note> <p>You can use this setting to enroll your DB cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:</p> <ul> <li> <p>Amazon Aurora - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html">Amazon RDS Extended Support with Amazon Aurora</a> in the <i>Amazon Aurora User Guide</i> </p> </li> <li> <p>Amazon RDS - <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i> </p> </li> </ul> <p>Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB cluster.</p> <p>Valid Values: </p> <ul> <li> <p> <code>cluster-auto-backup</code> - The DB cluster's automated backup.</p> </li> </ul>"""
    associated_roles: NotRequired[
        "capo_rds.types.db_cluster_associated_roles.DBClusterAssociatedRoles"
    ]
    """<p>A list of Amazon Web Services Identity and Access Management (IAM) roles to associate with the DB cluster when it's restored from Amazon S3. Each role grants the DB cluster permission to access other Amazon Web Services on your behalf. For each role, specify a role ARN and, optionally, the feature name (such as <code>s3Import</code>, <code>s3Export</code>, or <code>Lambda</code>).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBClusterFromS3Message, pairs: list[tuple[str, str]], prefix: str
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
    if "backtrack_window" in value:
        pairs.append((f"{key_prefix}BacktrackWindow", str(value["backtrack_window"])))
    if "enable_cloudwatch_logs_exports" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["enable_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnableCloudwatchLogsExports",
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
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "serverless_v2_scaling_configuration" in value:
        import capo_rds.types.serverless_v2_scaling_configuration

        capo_rds.types.serverless_v2_scaling_configuration.serialize_query(
            value["serverless_v2_scaling_configuration"],
            pairs,
            f"{key_prefix}ServerlessV2ScalingConfiguration",
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
    if "associated_roles" in value:
        import capo_rds.types.db_cluster_associated_roles

        capo_rds.types.db_cluster_associated_roles.serialize_query(
            value["associated_roles"], pairs, f"{key_prefix}AssociatedRoles"
        )


def deserialize_query(el: Element) -> RestoreDBClusterFromS3Message:
    out: RestoreDBClusterFromS3Message = {}  # type: ignore[typeddict-item]
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
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
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
    child_associated_roles = el.find("AssociatedRoles")
    if child_associated_roles is not None:
        import capo_rds.types.db_cluster_associated_roles

        out["associated_roles"] = (
            capo_rds.types.db_cluster_associated_roles.deserialize_query(
                child_associated_roles
            )
        )
    return out

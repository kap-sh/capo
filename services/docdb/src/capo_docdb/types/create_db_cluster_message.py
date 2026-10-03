"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.availability_zones
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.global_cluster_identifier
    import capo_docdb.types.integer_optional
    import capo_docdb.types.log_type_list
    import capo_docdb.types.serverless_v2_scaling_configuration
    import capo_docdb.types.string
    import capo_docdb.types.tag_list
    import capo_docdb.types.vpc_security_group_id_list


class CreateDBClusterMessage(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_docdb.types.availability_zones.AvailabilityZones"
    ]
    """<p>A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.</p>"""
    backup_retention_period: NotRequired[
        "capo_docdb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35.</p> </li> </ul>"""
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The cluster identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens. </p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster</code> </p>"""
    db_cluster_parameter_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the cluster parameter group to associate with this cluster.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_docdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of EC2 VPC security groups to associate with this cluster. </p>"""
    db_subnet_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>A subnet group to associate with this cluster.</p> <p>Constraints: Must match the name of an existing <code>DBSubnetGroup</code>. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    engine: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the database engine to be used for this cluster.</p> <p>Valid values: <code>docdb</code> </p>"""
    engine_version: NotRequired["capo_docdb.types.string.String"]
    """<p>The version number of the database engine to use. The <code>--engine-version</code> will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.</p>"""
    port: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the instances in the cluster accept connections.</p>"""
    master_username: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the master user for the cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must be from 1 to 63 letters or numbers.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot be a reserved word for the chosen database engine. </p> </li> </ul>"""
    master_user_password: NotRequired["capo_docdb.types.string.String"]
    """<p>The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).</p> <p>Constraints: Must contain from 8 to 100 characters.</p>"""
    preferred_backup_window: NotRequired["capo_docdb.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled using the <code>BackupRetentionPeriod</code> parameter. </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window. </p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_docdb.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>"""
    tags: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the cluster.</p>"""
    storage_encrypted: NotRequired["capo_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the cluster is encrypted.</p>"""
    kms_key_id: NotRequired["capo_docdb.types.string.String"]
    """<p>The KMS key identifier for an encrypted cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon Web Services account that owns the KMS encryption key that is used to encrypt the new cluster, you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>If an encryption key is not specified in <code>KmsKeyId</code>: </p> <ul> <li> <p>If the <code>StorageEncrypted</code> parameter is <code>true</code>, Amazon DocumentDB uses your default encryption key. </p> </li> </ul> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Regions.</p>"""
    pre_signed_url: NotRequired["capo_docdb.types.string.String"]
    """<p>Not currently supported. </p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_docdb.types.log_type_list.LogTypeList"
    ]
    """<p>A list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/event-auditing.html"> Auditing Amazon DocumentDB Events</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/profiling.html"> Profiling Amazon DocumentDB Operations</a>. </p>"""
    deletion_protection: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether this cluster can be deleted. If <code>DeletionProtection</code> is enabled, the cluster cannot be deleted unless it is modified and <code>DeletionProtection</code> is disabled. <code>DeletionProtection</code> protects clusters from being accidentally deleted.</p>"""
    global_cluster_identifier: NotRequired[
        "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The cluster identifier of the new global cluster.</p>"""
    storage_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p> <note> <p>When you create an Amazon DocumentDB cluster with the storage type set to <code>iopt1</code>, the storage type is returned in the response. The storage type isn't returned when you set it to <code>standard</code>.</p> </note>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_docdb.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    """<p>Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.</p>"""
    manage_master_user_password: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>Constraint: You can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p>"""
    master_user_secret_kms_key_id: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager. This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    network_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The network type of the cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html">DocumentDB clusters in a VPC</a> in the Amazon DocumentDB Developer Guide.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_docdb.types.availability_zones

        capo_docdb.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
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
        import capo_docdb.types.vpc_security_group_id_list

        capo_docdb.types.vpc_security_group_id_list.serialize_query(
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
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
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
    if "enable_cloudwatch_logs_exports" in value:
        import capo_docdb.types.log_type_list

        capo_docdb.types.log_type_list.serialize_query(
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
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "serverless_v2_scaling_configuration" in value:
        import capo_docdb.types.serverless_v2_scaling_configuration

        capo_docdb.types.serverless_v2_scaling_configuration.serialize_query(
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
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )


def deserialize_query(el: Element) -> CreateDBClusterMessage:
    out: CreateDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_docdb.types.availability_zones

        out["availability_zones"] = (
            capo_docdb.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
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
        import capo_docdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_docdb.types.vpc_security_group_id_list.deserialize_query(
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
        import capo_docdb.types.tag_list

        out["tags"] = capo_docdb.types.tag_list.deserialize_query(child_tags)
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
    child_enable_cloudwatch_logs_exports = el.find("EnableCloudwatchLogsExports")
    if child_enable_cloudwatch_logs_exports is not None:
        import capo_docdb.types.log_type_list

        out["enable_cloudwatch_logs_exports"] = (
            capo_docdb.types.log_type_list.deserialize_query(
                child_enable_cloudwatch_logs_exports
            )
        )
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
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_serverless_v2_scaling_configuration = el.find(
        "ServerlessV2ScalingConfiguration"
    )
    if child_serverless_v2_scaling_configuration is not None:
        import capo_docdb.types.serverless_v2_scaling_configuration

        out["serverless_v2_scaling_configuration"] = (
            capo_docdb.types.serverless_v2_scaling_configuration.deserialize_query(
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
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    return out

"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.cloudwatch_logs_export_configuration
    import capo_neptune.types.integer_optional
    import capo_neptune.types.serverless_v2_scaling_configuration
    import capo_neptune.types.string
    import capo_neptune.types.vpc_security_group_id_list


class ModifyDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul>"""
    new_db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> </li> <li> <p>The first character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>"""
    apply_immediately: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the DB cluster. If this parameter is set to <code>false</code>, changes to the DB cluster are applied during the next maintenance window.</p> <p>The <code>ApplyImmediately</code> parameter only affects <code>NewDBClusterIdentifier</code> values. If you set the <code>ApplyImmediately</code> parameter value to false, then changes to <code>NewDBClusterIdentifier</code> values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the <code>ApplyImmediately</code> parameter.</p> <p>Default: <code>false</code> </p>"""
    backup_retention_period: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35</p> </li> </ul>"""
    db_cluster_parameter_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB cluster parameter group to use for the DB cluster.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security groups that the DB cluster will belong to.</p>"""
    port: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the DB cluster accepts connections.</p> <p>Constraints: Value must be <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p>"""
    master_user_password: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    option_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p> <i>Not supported by Neptune.</i> </p>"""
    preferred_backup_window: NotRequired["capo_neptune.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_neptune.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.</p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> <p>Constraints: Minimum 30-minute window.</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.</p> <p>Default: <code>false</code> </p>"""
    cloudwatch_logs_export_configuration: NotRequired[
        "capo_neptune.types.cloudwatch_logs_export_configuration.CloudwatchLogsExportConfiguration"
    ]
    """<p>The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html#cloudwatch-logs-cli">Using the CLI to publish Neptune audit logs to CloudWatch Logs</a>.</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is set to true.</p> <p>For a list of valid engine versions, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html">Engine Releases for Amazon Neptune</a>, or call <a>DescribeDBEngineVersions</a>.</p>"""
    allow_major_version_upgrade: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>A value that indicates whether upgrades between different major versions are allowed.</p> <p>Constraints: You must set the allow-major-version-upgrade flag when providing an <code>EngineVersion</code> parameter that uses a different major version than the DB cluster's current version.</p>"""
    db_instance_parameter_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB parameter group to apply to all instances of the DB cluster. </p> <note> <p>When you apply a parameter group using <code>DBInstanceParameterGroupName</code>, parameter changes aren't applied during the next maintenance window but instead are applied immediately.</p> </note> <p>Default: The existing name setting</p> <p>Constraints:</p> <ul> <li> <p>The DB parameter group must be in the same DB parameter group family as the target DB cluster version.</p> </li> <li> <p>The <code>DBInstanceParameterGroupName</code> parameter is only valid in combination with the <code>AllowMajorVersionUpgrade</code> parameter.</p> </li> </ul>"""
    deletion_protection: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p> <i>If set to <code>true</code>, tags are copied to any snapshot of the DB cluster that is created.</i> </p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_neptune.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    """<p>Contains the scaling configuration of a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>"""
    storage_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The storage type to associate with the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>standard</code> </b> – ( <i>the default</i> ) Configures cost-effective database storage for applications with moderate to small I/O usage.</p> </li> <li> <p> <b> <code>iopt1</code> </b> – Enables <a href="https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage">I/O-Optimized storage</a> that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.</p> <p>Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.</p> </li> </ul>"""
    network_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication. The DB subnet group associated with the cluster must support IPv6.</p> </li> </ul>"""


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
        import capo_neptune.types.vpc_security_group_id_list

        capo_neptune.types.vpc_security_group_id_list.serialize_query(
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
    if "cloudwatch_logs_export_configuration" in value:
        import capo_neptune.types.cloudwatch_logs_export_configuration

        capo_neptune.types.cloudwatch_logs_export_configuration.serialize_query(
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
    if "serverless_v2_scaling_configuration" in value:
        import capo_neptune.types.serverless_v2_scaling_configuration

        capo_neptune.types.serverless_v2_scaling_configuration.serialize_query(
            value["serverless_v2_scaling_configuration"],
            pairs,
            f"{key_prefix}ServerlessV2ScalingConfiguration",
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))


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
        import capo_neptune.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_neptune.types.vpc_security_group_id_list.deserialize_query(
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
    child_cloudwatch_logs_export_configuration = el.find(
        "CloudwatchLogsExportConfiguration"
    )
    if child_cloudwatch_logs_export_configuration is not None:
        import capo_neptune.types.cloudwatch_logs_export_configuration

        out["cloudwatch_logs_export_configuration"] = (
            capo_neptune.types.cloudwatch_logs_export_configuration.deserialize_query(
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
    child_serverless_v2_scaling_configuration = el.find(
        "ServerlessV2ScalingConfiguration"
    )
    if child_serverless_v2_scaling_configuration is not None:
        import capo_neptune.types.serverless_v2_scaling_configuration

        out["serverless_v2_scaling_configuration"] = (
            capo_neptune.types.serverless_v2_scaling_configuration.deserialize_query(
                child_serverless_v2_scaling_configuration
            )
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    return out

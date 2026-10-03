"""Generated from Smithy shape ``com.amazonaws.neptune#RestoreDBClusterFromSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.availability_zones
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.integer_optional
    import capo_neptune.types.log_type_list
    import capo_neptune.types.serverless_v2_scaling_configuration
    import capo_neptune.types.string
    import capo_neptune.types.tag_list
    import capo_neptune.types.vpc_security_group_id_list


class RestoreDBClusterFromSnapshotMessage(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_neptune.types.availability_zones.AvailabilityZones"
    ]
    """<p>Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.</p>"""
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p>"""
    snapshot_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier for the DB snapshot or DB cluster snapshot to restore from.</p> <p>You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing Snapshot.</p> </li> </ul>"""
    engine: NotRequired["capo_neptune.types.string.String"]
    """<p>The database engine to use for the new DB cluster.</p> <p>Default: The same as source</p> <p>Constraint: Must be compatible with the engine of the source</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>The version of the database engine to use for the new DB cluster.</p>"""
    port: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the new DB cluster accepts connections.</p> <p>Constraints: Value must be <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p>"""
    db_subnet_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB subnet group to use for the new DB cluster.</p> <p>Constraints: If supplied, must match the name of an existing DBSubnetGroup.</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    database_name: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported.</p>"""
    option_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    vpc_security_group_ids: NotRequired[
        "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security groups that the new DB cluster will belong to.</p>"""
    tags: NotRequired["capo_neptune.types.tag_list.TagList"]
    """<p>The tags to be assigned to the restored DB cluster.</p>"""
    kms_key_id: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>If you do not specify a value for the <code>KmsKeyId</code> parameter, then the following will occur:</p> <ul> <li> <p>If the DB snapshot or DB cluster snapshot in <code>SnapshotIdentifier</code> is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.</p> </li> <li> <p>If the DB snapshot or DB cluster snapshot in <code>SnapshotIdentifier</code> is not encrypted, then the restored DB cluster is not encrypted.</p> </li> </ul>"""
    enable_iam_database_authentication: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.</p> <p>Default: <code>false</code> </p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_neptune.types.log_type_list.LogTypeList"
    ]
    """<p>The list of logs that the restored DB cluster is to export to Amazon CloudWatch Logs.</p>"""
    db_cluster_parameter_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB cluster parameter group to associate with the new DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>"""
    deletion_protection: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. </p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p> <i>If set to <code>true</code>, tags are copied to any snapshot of the restored DB cluster that is created.</i> </p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_neptune.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    """<p>Contains the scaling configuration of a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>"""
    storage_type: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the storage type to be associated with the DB cluster.</p> <p>Valid values: <code>standard</code>, <code>iopt1</code> </p> <p>Default: <code>standard</code> </p>"""
    network_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – ( <i>the default</i> ) The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication. The DB subnet group associated with the cluster must support IPv6.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBClusterFromSnapshotMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_neptune.types.availability_zones

        capo_neptune.types.availability_zones.serialize_query(
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
        import capo_neptune.types.vpc_security_group_id_list

        capo_neptune.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "tags" in value:
        import capo_neptune.types.tag_list

        capo_neptune.types.tag_list.serialize_query(
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
    if "enable_cloudwatch_logs_exports" in value:
        import capo_neptune.types.log_type_list

        capo_neptune.types.log_type_list.serialize_query(
            value["enable_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnableCloudwatchLogsExports",
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


def deserialize_query(el: Element) -> RestoreDBClusterFromSnapshotMessage:
    out: RestoreDBClusterFromSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_neptune.types.availability_zones

        out["availability_zones"] = (
            capo_neptune.types.availability_zones.deserialize_query(
                child_availability_zones
            )
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
        import capo_neptune.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_neptune.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_neptune.types.tag_list

        out["tags"] = capo_neptune.types.tag_list.deserialize_query(child_tags)
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
    child_enable_cloudwatch_logs_exports = el.find("EnableCloudwatchLogsExports")
    if child_enable_cloudwatch_logs_exports is not None:
        import capo_neptune.types.log_type_list

        out["enable_cloudwatch_logs_exports"] = (
            capo_neptune.types.log_type_list.deserialize_query(
                child_enable_cloudwatch_logs_exports
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

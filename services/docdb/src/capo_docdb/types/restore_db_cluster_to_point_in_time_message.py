"""Generated from Smithy shape ``com.amazonaws.docdb#RestoreDBClusterToPointInTimeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.integer_optional
    import capo_docdb.types.log_type_list
    import capo_docdb.types.serverless_v2_scaling_configuration
    import capo_docdb.types.string
    import capo_docdb.types.t_stamp
    import capo_docdb.types.tag_list
    import capo_docdb.types.vpc_security_group_id_list


class RestoreDBClusterToPointInTimeMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the new cluster to be created.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    restore_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The type of restore to be performed. You can specify one of the following values:</p> <ul> <li> <p> <code>full-copy</code> - The new DB cluster is restored as a full copy of the source DB cluster.</p> </li> <li> <p> <code>copy-on-write</code> - The new DB cluster is restored as a clone of the source DB cluster.</p> </li> </ul> <p>Constraints: You can't specify <code>copy-on-write</code> if the engine version of the source DB cluster is earlier than 1.11.</p> <p>If you don't specify a <code>RestoreType</code> value, then the new DB cluster is restored as a full copy of the source DB cluster.</p>"""
    source_db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The identifier of the source cluster from which to restore.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul>"""
    restore_to_time: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p>The date and time to restore the cluster to.</p> <p>Valid values: A time in Universal Coordinated Time (UTC) format.</p> <p>Constraints:</p> <ul> <li> <p>Must be before the latest restorable time for the instance.</p> </li> <li> <p>Must be specified if the <code>UseLatestRestorableTime</code> parameter is not provided.</p> </li> <li> <p>Cannot be specified if the <code>UseLatestRestorableTime</code> parameter is <code>true</code>.</p> </li> <li> <p>Cannot be specified if the <code>RestoreType</code> parameter is <code>copy-on-write</code>.</p> </li> </ul> <p>Example: <code>2015-03-07T23:45:00Z</code> </p>"""
    use_latest_restorable_time: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p>A value that is set to <code>true</code> to restore the cluster to the latest restorable backup time, and <code>false</code> otherwise. </p> <p>Default: <code>false</code> </p> <p>Constraints: Cannot be specified if the <code>RestoreToTime</code> parameter is provided.</p>"""
    port: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the new cluster accepts connections.</p> <p>Constraints: Must be a value from <code>1150</code> to <code>65535</code>. </p> <p>Default: The default port for the engine.</p>"""
    db_subnet_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The subnet group name to use for the new cluster.</p> <p>Constraints: If provided, must match the name of an existing <code>DBSubnetGroup</code>.</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    vpc_security_group_ids: NotRequired[
        "capo_docdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security groups that the new cluster belongs to.</p>"""
    tags: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the restored cluster.</p>"""
    kms_key_id: NotRequired["capo_docdb.types.string.String"]
    """<p>The KMS key identifier to use when restoring an encrypted cluster from an encrypted cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a cluster with the same Amazon Web Services account that owns the KMS encryption key used to encrypt the new cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>You can restore to a new cluster and encrypt the new cluster with an KMS key that is different from the KMS key used to encrypt the source cluster. The new DB cluster is encrypted with the KMS key identified by the <code>KmsKeyId</code> parameter.</p> <p>If you do not specify a value for the <code>KmsKeyId</code> parameter, then the following occurs:</p> <ul> <li> <p>If the cluster is encrypted, then the restored cluster is encrypted using the KMS key that was used to encrypt the source cluster.</p> </li> <li> <p>If the cluster is not encrypted, then the restored cluster is not encrypted.</p> </li> </ul> <p>If <code>DBClusterIdentifier</code> refers to a cluster that is not encrypted, then the restore request is rejected.</p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_docdb.types.log_type_list.LogTypeList"
    ]
    """<p>A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.</p>"""
    deletion_protection: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether this cluster can be deleted. If <code>DeletionProtection</code> is enabled, the cluster cannot be deleted unless it is modified and <code>DeletionProtection</code> is disabled. <code>DeletionProtection</code> protects clusters from being accidentally deleted.</p>"""
    serverless_v2_scaling_configuration: NotRequired[
        "capo_docdb.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
    ]
    """<p>Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.</p>"""
    storage_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p>"""
    network_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The network type of the cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html">DocumentDB clusters in a VPC</a> in the Amazon DocumentDB Developer Guide.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the restored DB cluster to snapshots of the restored DB cluster. The default is not to copy them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBClusterToPointInTimeMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "restore_type" in value:
        pairs.append((f"{key_prefix}RestoreType", str(value["restore_type"])))
    if "source_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterIdentifier",
                str(value["source_db_cluster_identifier"]),
            )
        )
    if "restore_to_time" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["restore_to_time"], pairs, f"{key_prefix}RestoreToTime"
        )
    if "use_latest_restorable_time" in value:
        pairs.append(
            (
                f"{key_prefix}UseLatestRestorableTime",
                "true" if value["use_latest_restorable_time"] else "false",
            )
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "vpc_security_group_ids" in value:
        import capo_docdb.types.vpc_security_group_id_list

        capo_docdb.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "tags" in value:
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
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
    if "serverless_v2_scaling_configuration" in value:
        import capo_docdb.types.serverless_v2_scaling_configuration

        capo_docdb.types.serverless_v2_scaling_configuration.serialize_query(
            value["serverless_v2_scaling_configuration"],
            pairs,
            f"{key_prefix}ServerlessV2ScalingConfiguration",
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )


def deserialize_query(el: Element) -> RestoreDBClusterToPointInTimeMessage:
    out: RestoreDBClusterToPointInTimeMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_restore_type = el.find("RestoreType")
    if child_restore_type is not None:
        out["restore_type"] = str(child_restore_type.text or "")
    child_source_db_cluster_identifier = el.find("SourceDBClusterIdentifier")
    if child_source_db_cluster_identifier is not None:
        out["source_db_cluster_identifier"] = str(
            child_source_db_cluster_identifier.text or ""
        )
    child_restore_to_time = el.find("RestoreToTime")
    if child_restore_to_time is not None:
        import capo_docdb.types.t_stamp

        out["restore_to_time"] = capo_docdb.types.t_stamp.deserialize_query(
            child_restore_to_time
        )
    child_use_latest_restorable_time = el.find("UseLatestRestorableTime")
    if child_use_latest_restorable_time is not None:
        out["use_latest_restorable_time"] = (
            child_use_latest_restorable_time.text or ""
        ).lower() == "true"
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_docdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_docdb.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_docdb.types.tag_list

        out["tags"] = capo_docdb.types.tag_list.deserialize_query(child_tags)
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
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
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    return out

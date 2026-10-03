"""Generated from Smithy shape ``com.amazonaws.elasticache#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.automatic_failover_status
    import capo_elasticache.types.boolean
    import capo_elasticache.types.data_tiering_status
    import capo_elasticache.types.durability
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.node_snapshot_list
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp


class Snapshot(TypedDict, closed=True):
    snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.</p>"""
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique identifier of the source replication group.</p>"""
    replication_group_description: NotRequired["capo_elasticache.types.string.String"]
    """<p>A description of the source replication group.</p>"""
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The user-supplied identifier of the source cluster.</p>"""
    snapshot_status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The status of the snapshot. Valid values: <code>creating</code> | <code>available</code> | <code>restoring</code> | <code>copying</code> | <code>deleting</code>.</p>"""
    snapshot_source: NotRequired["capo_elasticache.types.string.String"]
    """<p>Indicates whether the snapshot is from an automatic backup (<code>automated</code>) or was created manually (<code>manual</code>).</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the compute and memory capacity node type for the source cluster.</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache engine (<code>memcached</code> or <code>redis</code>) used by the source cluster.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The version of the cache engine version that is used by the source cluster.</p>"""
    num_cache_nodes: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of cache nodes in the source cluster.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p>"""
    preferred_availability_zone: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Availability Zone in which the source cluster is located.</p>"""
    preferred_outpost_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the preferred outpost.</p>"""
    cache_cluster_create_time: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time when the source cluster was created.</p>"""
    preferred_maintenance_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    topic_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.</p>"""
    port: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The port number used by each cache nodes in the source cluster.</p>"""
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cache parameter group that is associated with the source cluster.</p>"""
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache subnet group associated with the source cluster.</p>"""
    vpc_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p> If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.</p> <p>For manual snapshots, this field reflects the <code>SnapshotRetentionLimit</code> for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the <code>DeleteSnapshot</code> operation. </p> <p> <b>Important</b> If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.</p>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range during which ElastiCache takes daily snapshots of the source cluster.</p>"""
    num_node_groups: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.</p>"""
    automatic_failover: NotRequired[
        "capo_elasticache.types.automatic_failover_status.AutomaticFailoverStatus"
    ]
    """<p>Indicates the status of automatic failover for the source Valkey or Redis OSS replication group.</p>"""
    node_snapshots: NotRequired[
        "capo_elasticache.types.node_snapshot_list.NodeSnapshotList"
    ]
    """<p>A list of the cache nodes in the source cluster.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the snapshot.</p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the snapshot.</p>"""
    data_tiering: NotRequired[
        "capo_elasticache.types.data_tiering_status.DataTieringStatus"
    ]
    """<p>Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html">Data tiering</a>.</p>"""
    durability: NotRequired["capo_elasticache.types.durability.Durability"]
    """<p>The durability setting of the cluster when the snapshot was taken. When restoring from this snapshot, the cluster uses this durability setting unless overridden in the restore request. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html">Durability</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Snapshot, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_name" in value:
        pairs.append((f"{key_prefix}SnapshotName", str(value["snapshot_name"])))
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "replication_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}ReplicationGroupDescription",
                str(value["replication_group_description"]),
            )
        )
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "snapshot_status" in value:
        pairs.append((f"{key_prefix}SnapshotStatus", str(value["snapshot_status"])))
    if "snapshot_source" in value:
        pairs.append((f"{key_prefix}SnapshotSource", str(value["snapshot_source"])))
    if "cache_node_type" in value:
        pairs.append((f"{key_prefix}CacheNodeType", str(value["cache_node_type"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "num_cache_nodes" in value:
        pairs.append((f"{key_prefix}NumCacheNodes", str(value["num_cache_nodes"])))
    if "preferred_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredAvailabilityZone",
                str(value["preferred_availability_zone"]),
            )
        )
    if "preferred_outpost_arn" in value:
        pairs.append(
            (f"{key_prefix}PreferredOutpostArn", str(value["preferred_outpost_arn"]))
        )
    if "cache_cluster_create_time" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["cache_cluster_create_time"],
            pairs,
            f"{key_prefix}CacheClusterCreateTime",
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "cache_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}CacheSubnetGroupName", str(value["cache_subnet_group_name"]))
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "snapshot_retention_limit" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotRetentionLimit",
                str(value["snapshot_retention_limit"]),
            )
        )
    if "snapshot_window" in value:
        pairs.append((f"{key_prefix}SnapshotWindow", str(value["snapshot_window"])))
    if "num_node_groups" in value:
        pairs.append((f"{key_prefix}NumNodeGroups", str(value["num_node_groups"])))
    if "automatic_failover" in value:
        import capo_elasticache.types.automatic_failover_status

        capo_elasticache.types.automatic_failover_status.serialize_query(
            value["automatic_failover"], pairs, f"{key_prefix}AutomaticFailover"
        )
    if "node_snapshots" in value:
        import capo_elasticache.types.node_snapshot_list

        capo_elasticache.types.node_snapshot_list.serialize_query(
            value["node_snapshots"], pairs, f"{key_prefix}NodeSnapshots"
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))
    if "data_tiering" in value:
        import capo_elasticache.types.data_tiering_status

        capo_elasticache.types.data_tiering_status.serialize_query(
            value["data_tiering"], pairs, f"{key_prefix}DataTiering"
        )
    if "durability" in value:
        import capo_elasticache.types.durability

        capo_elasticache.types.durability.serialize_query(
            value["durability"], pairs, f"{key_prefix}Durability"
        )


def deserialize_query(el: Element) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    child_snapshot_name = el.find("SnapshotName")
    if child_snapshot_name is not None:
        out["snapshot_name"] = str(child_snapshot_name.text or "")
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_replication_group_description = el.find("ReplicationGroupDescription")
    if child_replication_group_description is not None:
        out["replication_group_description"] = str(
            child_replication_group_description.text or ""
        )
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_snapshot_status = el.find("SnapshotStatus")
    if child_snapshot_status is not None:
        out["snapshot_status"] = str(child_snapshot_status.text or "")
    child_snapshot_source = el.find("SnapshotSource")
    if child_snapshot_source is not None:
        out["snapshot_source"] = str(child_snapshot_source.text or "")
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_num_cache_nodes = el.find("NumCacheNodes")
    if child_num_cache_nodes is not None:
        out["num_cache_nodes"] = int(child_num_cache_nodes.text or "")
    child_preferred_availability_zone = el.find("PreferredAvailabilityZone")
    if child_preferred_availability_zone is not None:
        out["preferred_availability_zone"] = str(
            child_preferred_availability_zone.text or ""
        )
    child_preferred_outpost_arn = el.find("PreferredOutpostArn")
    if child_preferred_outpost_arn is not None:
        out["preferred_outpost_arn"] = str(child_preferred_outpost_arn.text or "")
    child_cache_cluster_create_time = el.find("CacheClusterCreateTime")
    if child_cache_cluster_create_time is not None:
        import capo_elasticache.types.t_stamp

        out["cache_cluster_create_time"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_cache_cluster_create_time
            )
        )
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_cache_subnet_group_name = el.find("CacheSubnetGroupName")
    if child_cache_subnet_group_name is not None:
        out["cache_subnet_group_name"] = str(child_cache_subnet_group_name.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_snapshot_retention_limit = el.find("SnapshotRetentionLimit")
    if child_snapshot_retention_limit is not None:
        out["snapshot_retention_limit"] = int(child_snapshot_retention_limit.text or "")
    child_snapshot_window = el.find("SnapshotWindow")
    if child_snapshot_window is not None:
        out["snapshot_window"] = str(child_snapshot_window.text or "")
    child_num_node_groups = el.find("NumNodeGroups")
    if child_num_node_groups is not None:
        out["num_node_groups"] = int(child_num_node_groups.text or "")
    child_automatic_failover = el.find("AutomaticFailover")
    if child_automatic_failover is not None:
        import capo_elasticache.types.automatic_failover_status

        out["automatic_failover"] = (
            capo_elasticache.types.automatic_failover_status.deserialize_query(
                child_automatic_failover
            )
        )
    child_node_snapshots = el.find("NodeSnapshots")
    if child_node_snapshots is not None:
        import capo_elasticache.types.node_snapshot_list

        out["node_snapshots"] = (
            capo_elasticache.types.node_snapshot_list.deserialize_query(
                child_node_snapshots
            )
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_data_tiering = el.find("DataTiering")
    if child_data_tiering is not None:
        import capo_elasticache.types.data_tiering_status

        out["data_tiering"] = (
            capo_elasticache.types.data_tiering_status.deserialize_query(
                child_data_tiering
            )
        )
    child_durability = el.find("Durability")
    if child_durability is not None:
        import capo_elasticache.types.durability

        out["durability"] = capo_elasticache.types.durability.deserialize_query(
            child_durability
        )
    return out

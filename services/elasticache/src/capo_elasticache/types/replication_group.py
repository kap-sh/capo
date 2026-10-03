"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicationGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.automatic_failover_status
    import capo_elasticache.types.boolean
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cluster_id_list
    import capo_elasticache.types.cluster_mode
    import capo_elasticache.types.data_tiering_status
    import capo_elasticache.types.durability
    import capo_elasticache.types.effective_durability
    import capo_elasticache.types.endpoint
    import capo_elasticache.types.global_replication_group_info
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.log_delivery_configuration_list
    import capo_elasticache.types.multi_az_status
    import capo_elasticache.types.network_type
    import capo_elasticache.types.node_group_list
    import capo_elasticache.types.replication_group_outpost_arn_list
    import capo_elasticache.types.replication_group_pending_modified_values
    import capo_elasticache.types.storage_encryption_type
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp
    import capo_elasticache.types.transit_encryption_mode
    import capo_elasticache.types.user_group_id_list


class ReplicationGroup(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier for the replication group.</p>"""
    description: NotRequired["capo_elasticache.types.string.String"]
    """<p>The user supplied description of the replication group.</p>"""
    global_replication_group_info: NotRequired[
        "capo_elasticache.types.global_replication_group_info.GlobalReplicationGroupInfo"
    ]
    """<p>The name of the Global datastore and role of this replication group in the Global datastore.</p>"""
    status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The current state of this replication group - <code>creating</code>, <code>available</code>, <code>modifying</code>, <code>deleting</code>, <code>create-failed</code>, <code>snapshotting</code>.</p>"""
    pending_modified_values: NotRequired[
        "capo_elasticache.types.replication_group_pending_modified_values.ReplicationGroupPendingModifiedValues"
    ]
    """<p>A group of settings to be applied to the replication group, either immediately or during the next maintenance window.</p>"""
    member_clusters: NotRequired["capo_elasticache.types.cluster_id_list.ClusterIdList"]
    """<p>The names of all the cache clusters that are part of this replication group.</p>"""
    node_groups: NotRequired["capo_elasticache.types.node_group_list.NodeGroupList"]
    """<p>A list of node groups in this replication group. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is a single-element list. For Valkey or Redis OSS (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).</p>"""
    snapshotting_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cluster ID that is used as the daily snapshot source for the replication group.</p>"""
    automatic_failover: NotRequired[
        "capo_elasticache.types.automatic_failover_status.AutomaticFailoverStatus"
    ]
    """<p>Indicates the status of automatic failover for this Valkey or Redis OSS replication group.</p>"""
    multi_az: NotRequired["capo_elasticache.types.multi_az_status.MultiAZStatus"]
    """<p>A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html">Minimizing Downtime: Multi-AZ</a> </p>"""
    configuration_endpoint: NotRequired["capo_elasticache.types.endpoint.Endpoint"]
    """<p>The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.</p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <important> <p> If the value of <code>SnapshotRetentionLimit</code> is set to zero (0), backups are turned off.</p> </important>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>"""
    cluster_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).</p> <p>Valid values: <code>true</code> | <code>false</code> </p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the compute and memory capacity node type for each node in the replication group.</p>"""
    auth_token_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables using an <code>AuthToken</code> (password) when issuing Valkey or Redis OSS commands.</p> <p>Default: <code>false</code> </p>"""
    auth_token_last_modified_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date the auth token was last modified</p>"""
    transit_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables in-transit encryption when set to <code>true</code>.</p> <p> <b>Required:</b> Only available when creating a replication group in an Amazon VPC using Redis OSS version <code>3.2.6</code>, <code>4.x</code> or later.</p> <p>Default: <code>false</code> </p>"""
    at_rest_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables encryption at-rest on the cluster when set to <code>true</code>. In some cases, encryption at-rest may be enabled even when this value is false. Use <code>StorageEncryptionType</code> to view the effective encryption state of a cluster.</p> <p>You cannot modify the value of <code>AtRestEncryptionEnabled</code> after the cluster is created.</p> <p>Default: <code>true</code> when using Valkey, <code>false</code> when using Redis OSS</p>"""
    member_clusters_outpost_arns: NotRequired[
        "capo_elasticache.types.replication_group_outpost_arn_list.ReplicationGroupOutpostArnList"
    ]
    """<p>The outpost ARNs of the replication group's member clusters.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the disk in the cluster.</p>"""
    storage_encryption_type: NotRequired[
        "capo_elasticache.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>Indicates the type of encryption for data stored at rest in the replication group. The value is <code>none</code> if at-rest encryption is not enabled, <code>sse-elasticache</code> if an ElastiCache service-managed key is used, or <code>sse-kms</code> if a customer-managed KMS key is used.</p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the replication group.</p>"""
    user_group_ids: NotRequired[
        "capo_elasticache.types.user_group_id_list.UserGroupIdList"
    ]
    """<p>The ID of the user group associated to the replication group.</p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.log_delivery_configuration_list.LogDeliveryConfigurationList"
    ]
    """<p>Returns the destination, format and type of the logs. </p>"""
    replication_group_create_time: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time when the cluster was created.</p>"""
    data_tiering: NotRequired[
        "capo_elasticache.types.data_tiering_status.DataTieringStatus"
    ]
    """<p>Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html">Data tiering</a>.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>If you are running Valkey 7.2 and above, or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    network_type: NotRequired["capo_elasticache.types.network_type.NetworkType"]
    """<p>Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    ip_discovery: NotRequired["capo_elasticache.types.ip_discovery.IpDiscovery"]
    """<p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    transit_encryption_mode: NotRequired[
        "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
    ]
    """<p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p>"""
    cluster_mode: NotRequired["capo_elasticache.types.cluster_mode.ClusterMode"]
    """<p>Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.</p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The engine used in a replication group. The options are valkey, memcached or redis.</p>"""
    durability: NotRequired["capo_elasticache.types.durability.Durability"]
    """<p>The durability setting of the replication group. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html">Durability</a>.</p>"""
    effective_durability: NotRequired[
        "capo_elasticache.types.effective_durability.EffectiveDurability"
    ]
    """<p>The effective durability of the replication group. When <code>Durability</code> is set to <code>default</code>, the service resolves the actual durability based on the engine version, cluster mode, and other parameters. This field reflects the resolved value. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Durability.Configuring.html">Configuring Durability</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicationGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "global_replication_group_info" in value:
        import capo_elasticache.types.global_replication_group_info

        capo_elasticache.types.global_replication_group_info.serialize_query(
            value["global_replication_group_info"],
            pairs,
            f"{key_prefix}GlobalReplicationGroupInfo",
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "pending_modified_values" in value:
        import capo_elasticache.types.replication_group_pending_modified_values

        capo_elasticache.types.replication_group_pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "member_clusters" in value:
        import capo_elasticache.types.cluster_id_list

        capo_elasticache.types.cluster_id_list.serialize_query(
            value["member_clusters"], pairs, f"{key_prefix}MemberClusters"
        )
    if "node_groups" in value:
        import capo_elasticache.types.node_group_list

        capo_elasticache.types.node_group_list.serialize_query(
            value["node_groups"], pairs, f"{key_prefix}NodeGroups"
        )
    if "snapshotting_cluster_id" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshottingClusterId",
                str(value["snapshotting_cluster_id"]),
            )
        )
    if "automatic_failover" in value:
        import capo_elasticache.types.automatic_failover_status

        capo_elasticache.types.automatic_failover_status.serialize_query(
            value["automatic_failover"], pairs, f"{key_prefix}AutomaticFailover"
        )
    if "multi_az" in value:
        import capo_elasticache.types.multi_az_status

        capo_elasticache.types.multi_az_status.serialize_query(
            value["multi_az"], pairs, f"{key_prefix}MultiAZ"
        )
    if "configuration_endpoint" in value:
        import capo_elasticache.types.endpoint

        capo_elasticache.types.endpoint.serialize_query(
            value["configuration_endpoint"], pairs, f"{key_prefix}ConfigurationEndpoint"
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
    if "cluster_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterEnabled",
                "true" if value["cluster_enabled"] else "false",
            )
        )
    if "cache_node_type" in value:
        pairs.append((f"{key_prefix}CacheNodeType", str(value["cache_node_type"])))
    if "auth_token_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}AuthTokenEnabled",
                "true" if value["auth_token_enabled"] else "false",
            )
        )
    if "auth_token_last_modified_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["auth_token_last_modified_date"],
            pairs,
            f"{key_prefix}AuthTokenLastModifiedDate",
        )
    if "transit_encryption_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}TransitEncryptionEnabled",
                "true" if value["transit_encryption_enabled"] else "false",
            )
        )
    if "at_rest_encryption_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}AtRestEncryptionEnabled",
                "true" if value["at_rest_encryption_enabled"] else "false",
            )
        )
    if "member_clusters_outpost_arns" in value:
        import capo_elasticache.types.replication_group_outpost_arn_list

        capo_elasticache.types.replication_group_outpost_arn_list.serialize_query(
            value["member_clusters_outpost_arns"],
            pairs,
            f"{key_prefix}MemberClustersOutpostArns",
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "storage_encryption_type" in value:
        import capo_elasticache.types.storage_encryption_type

        capo_elasticache.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
        )
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))
    if "user_group_ids" in value:
        import capo_elasticache.types.user_group_id_list

        capo_elasticache.types.user_group_id_list.serialize_query(
            value["user_group_ids"], pairs, f"{key_prefix}UserGroupIds"
        )
    if "log_delivery_configurations" in value:
        import capo_elasticache.types.log_delivery_configuration_list

        capo_elasticache.types.log_delivery_configuration_list.serialize_query(
            value["log_delivery_configurations"],
            pairs,
            f"{key_prefix}LogDeliveryConfigurations",
        )
    if "replication_group_create_time" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["replication_group_create_time"],
            pairs,
            f"{key_prefix}ReplicationGroupCreateTime",
        )
    if "data_tiering" in value:
        import capo_elasticache.types.data_tiering_status

        capo_elasticache.types.data_tiering_status.serialize_query(
            value["data_tiering"], pairs, f"{key_prefix}DataTiering"
        )
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "network_type" in value:
        import capo_elasticache.types.network_type

        capo_elasticache.types.network_type.serialize_query(
            value["network_type"], pairs, f"{key_prefix}NetworkType"
        )
    if "ip_discovery" in value:
        import capo_elasticache.types.ip_discovery

        capo_elasticache.types.ip_discovery.serialize_query(
            value["ip_discovery"], pairs, f"{key_prefix}IpDiscovery"
        )
    if "transit_encryption_mode" in value:
        import capo_elasticache.types.transit_encryption_mode

        capo_elasticache.types.transit_encryption_mode.serialize_query(
            value["transit_encryption_mode"],
            pairs,
            f"{key_prefix}TransitEncryptionMode",
        )
    if "cluster_mode" in value:
        import capo_elasticache.types.cluster_mode

        capo_elasticache.types.cluster_mode.serialize_query(
            value["cluster_mode"], pairs, f"{key_prefix}ClusterMode"
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "durability" in value:
        import capo_elasticache.types.durability

        capo_elasticache.types.durability.serialize_query(
            value["durability"], pairs, f"{key_prefix}Durability"
        )
    if "effective_durability" in value:
        import capo_elasticache.types.effective_durability

        capo_elasticache.types.effective_durability.serialize_query(
            value["effective_durability"], pairs, f"{key_prefix}EffectiveDurability"
        )


def deserialize_query(el: Element) -> ReplicationGroup:
    out: ReplicationGroup = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_global_replication_group_info = el.find("GlobalReplicationGroupInfo")
    if child_global_replication_group_info is not None:
        import capo_elasticache.types.global_replication_group_info

        out["global_replication_group_info"] = (
            capo_elasticache.types.global_replication_group_info.deserialize_query(
                child_global_replication_group_info
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_elasticache.types.replication_group_pending_modified_values

        out["pending_modified_values"] = (
            capo_elasticache.types.replication_group_pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_member_clusters = el.find("MemberClusters")
    if child_member_clusters is not None:
        import capo_elasticache.types.cluster_id_list

        out["member_clusters"] = (
            capo_elasticache.types.cluster_id_list.deserialize_query(
                child_member_clusters
            )
        )
    child_node_groups = el.find("NodeGroups")
    if child_node_groups is not None:
        import capo_elasticache.types.node_group_list

        out["node_groups"] = capo_elasticache.types.node_group_list.deserialize_query(
            child_node_groups
        )
    child_snapshotting_cluster_id = el.find("SnapshottingClusterId")
    if child_snapshotting_cluster_id is not None:
        out["snapshotting_cluster_id"] = str(child_snapshotting_cluster_id.text or "")
    child_automatic_failover = el.find("AutomaticFailover")
    if child_automatic_failover is not None:
        import capo_elasticache.types.automatic_failover_status

        out["automatic_failover"] = (
            capo_elasticache.types.automatic_failover_status.deserialize_query(
                child_automatic_failover
            )
        )
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        import capo_elasticache.types.multi_az_status

        out["multi_az"] = capo_elasticache.types.multi_az_status.deserialize_query(
            child_multi_az
        )
    child_configuration_endpoint = el.find("ConfigurationEndpoint")
    if child_configuration_endpoint is not None:
        import capo_elasticache.types.endpoint

        out["configuration_endpoint"] = (
            capo_elasticache.types.endpoint.deserialize_query(
                child_configuration_endpoint
            )
        )
    child_snapshot_retention_limit = el.find("SnapshotRetentionLimit")
    if child_snapshot_retention_limit is not None:
        out["snapshot_retention_limit"] = int(child_snapshot_retention_limit.text or "")
    child_snapshot_window = el.find("SnapshotWindow")
    if child_snapshot_window is not None:
        out["snapshot_window"] = str(child_snapshot_window.text or "")
    child_cluster_enabled = el.find("ClusterEnabled")
    if child_cluster_enabled is not None:
        out["cluster_enabled"] = (child_cluster_enabled.text or "").lower() == "true"
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_auth_token_enabled = el.find("AuthTokenEnabled")
    if child_auth_token_enabled is not None:
        out["auth_token_enabled"] = (
            child_auth_token_enabled.text or ""
        ).lower() == "true"
    child_auth_token_last_modified_date = el.find("AuthTokenLastModifiedDate")
    if child_auth_token_last_modified_date is not None:
        import capo_elasticache.types.t_stamp

        out["auth_token_last_modified_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_auth_token_last_modified_date
            )
        )
    child_transit_encryption_enabled = el.find("TransitEncryptionEnabled")
    if child_transit_encryption_enabled is not None:
        out["transit_encryption_enabled"] = (
            child_transit_encryption_enabled.text or ""
        ).lower() == "true"
    child_at_rest_encryption_enabled = el.find("AtRestEncryptionEnabled")
    if child_at_rest_encryption_enabled is not None:
        out["at_rest_encryption_enabled"] = (
            child_at_rest_encryption_enabled.text or ""
        ).lower() == "true"
    child_member_clusters_outpost_arns = el.find("MemberClustersOutpostArns")
    if child_member_clusters_outpost_arns is not None:
        import capo_elasticache.types.replication_group_outpost_arn_list

        out["member_clusters_outpost_arns"] = (
            capo_elasticache.types.replication_group_outpost_arn_list.deserialize_query(
                child_member_clusters_outpost_arns
            )
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_elasticache.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_elasticache.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_user_group_ids = el.find("UserGroupIds")
    if child_user_group_ids is not None:
        import capo_elasticache.types.user_group_id_list

        out["user_group_ids"] = (
            capo_elasticache.types.user_group_id_list.deserialize_query(
                child_user_group_ids
            )
        )
    child_log_delivery_configurations = el.find("LogDeliveryConfigurations")
    if child_log_delivery_configurations is not None:
        import capo_elasticache.types.log_delivery_configuration_list

        out["log_delivery_configurations"] = (
            capo_elasticache.types.log_delivery_configuration_list.deserialize_query(
                child_log_delivery_configurations
            )
        )
    child_replication_group_create_time = el.find("ReplicationGroupCreateTime")
    if child_replication_group_create_time is not None:
        import capo_elasticache.types.t_stamp

        out["replication_group_create_time"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_replication_group_create_time
            )
        )
    child_data_tiering = el.find("DataTiering")
    if child_data_tiering is not None:
        import capo_elasticache.types.data_tiering_status

        out["data_tiering"] = (
            capo_elasticache.types.data_tiering_status.deserialize_query(
                child_data_tiering
            )
        )
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        import capo_elasticache.types.network_type

        out["network_type"] = capo_elasticache.types.network_type.deserialize_query(
            child_network_type
        )
    child_ip_discovery = el.find("IpDiscovery")
    if child_ip_discovery is not None:
        import capo_elasticache.types.ip_discovery

        out["ip_discovery"] = capo_elasticache.types.ip_discovery.deserialize_query(
            child_ip_discovery
        )
    child_transit_encryption_mode = el.find("TransitEncryptionMode")
    if child_transit_encryption_mode is not None:
        import capo_elasticache.types.transit_encryption_mode

        out["transit_encryption_mode"] = (
            capo_elasticache.types.transit_encryption_mode.deserialize_query(
                child_transit_encryption_mode
            )
        )
    child_cluster_mode = el.find("ClusterMode")
    if child_cluster_mode is not None:
        import capo_elasticache.types.cluster_mode

        out["cluster_mode"] = capo_elasticache.types.cluster_mode.deserialize_query(
            child_cluster_mode
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_durability = el.find("Durability")
    if child_durability is not None:
        import capo_elasticache.types.durability

        out["durability"] = capo_elasticache.types.durability.deserialize_query(
            child_durability
        )
    child_effective_durability = el.find("EffectiveDurability")
    if child_effective_durability is not None:
        import capo_elasticache.types.effective_durability

        out["effective_durability"] = (
            capo_elasticache.types.effective_durability.deserialize_query(
                child_effective_durability
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyCacheClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.auth_token_update_strategy_type
    import capo_elasticache.types.az_mode
    import capo_elasticache.types.boolean
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_node_ids_list
    import capo_elasticache.types.cache_security_group_name_list
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.log_delivery_configuration_request_list
    import capo_elasticache.types.preferred_availability_zone_list
    import capo_elasticache.types.scale_config
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.string


class ModifyCacheClusterMessage(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cluster identifier. This value is stored as a lowercase string.</p>"""
    num_cache_nodes: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of cache nodes that the cluster should have. If the value for <code>NumCacheNodes</code> is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.</p> <p>If you are removing cache nodes, you must use the <code>CacheNodeIdsToRemove</code> parameter to provide the IDs of the specific cache nodes to remove.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p> <note> <p>Adding or removing Memcached cache nodes can be applied immediately or as a pending operation (see <code>ApplyImmediately</code>).</p> <p>A pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the <code>ModifyCacheCluster</code> request and set <code>NumCacheNodes</code> equal to the number of cache nodes currently in the cluster.</p> </note>"""
    cache_node_ids_to_remove: NotRequired[
        "capo_elasticache.types.cache_node_ids_list.CacheNodeIdsList"
    ]
    """<p>A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when <code>NumCacheNodes</code> is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of <code>NumCacheNodes</code> in the request.</p> <p>For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this <code>ModifyCacheCluster</code> call is 5, you must list 2 (7 - 5) cache node IDs to remove.</p>"""
    az_mode: NotRequired["capo_elasticache.types.az_mode.AZMode"]
    """<p>Specifies whether the new nodes in this Memcached cluster are all created in a single Availability Zone or created across multiple Availability Zones.</p> <p>Valid values: <code>single-az</code> | <code>cross-az</code>.</p> <p>This option is only supported for Memcached clusters.</p> <note> <p>You cannot specify <code>single-az</code> if the Memcached cluster already has cache nodes in different Availability Zones. If <code>cross-az</code> is specified, existing Memcached nodes remain in their current Availability Zone.</p> <p>Only newly created nodes are located in different Availability Zones. </p> </note>"""
    new_availability_zones: NotRequired[
        "capo_elasticache.types.preferred_availability_zone_list.PreferredAvailabilityZoneList"
    ]
    """<note> <p>This option is only supported on Memcached clusters.</p> </note> <p>The list of Availability Zones where the new Memcached cache nodes are created.</p> <p>This parameter is only valid when <code>NumCacheNodes</code> in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.</p> <p>Scenarios:</p> <ul> <li> <p> <b>Scenario 1:</b> You have 3 active nodes and wish to add 2 nodes. Specify <code>NumCacheNodes=5</code> (3 + 2) and optionally specify two Availability Zones for the two new nodes.</p> </li> <li> <p> <b>Scenario 2:</b> You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify <code>NumCacheNodes=6</code> ((3 + 2) + 1) and optionally specify an Availability Zone for the new node.</p> </li> <li> <p> <b>Scenario 3:</b> You want to cancel all pending operations. Specify <code>NumCacheNodes=3</code> to cancel all pending operations.</p> </li> </ul> <p>The Availability Zone placement of nodes pending creation cannot be modified. If you wish to cancel any nodes pending creation, add 0 nodes by setting <code>NumCacheNodes</code> to the number of current nodes.</p> <p>If <code>cross-az</code> is specified, existing Memcached nodes remain in their current Availability Zone. Only newly created nodes can be located in different Availability Zones. For guidance on how to move existing Memcached nodes to different Availability Zones, see the <b>Availability Zone Considerations</b> section of <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html">Cache Node Considerations for Memcached</a>.</p> <p> <b>Impact of new add/remove requests upon pending requests</b> </p> <ul> <li> <p>Scenario-1</p> <ul> <li> <p>Pending Action: Delete</p> </li> <li> <p>New Request: Delete</p> </li> <li> <p>Result: The new delete, pending or immediate, replaces the pending delete.</p> </li> </ul> </li> <li> <p>Scenario-2</p> <ul> <li> <p>Pending Action: Delete</p> </li> <li> <p>New Request: Create</p> </li> <li> <p>Result: The new create, pending or immediate, replaces the pending delete.</p> </li> </ul> </li> <li> <p>Scenario-3</p> <ul> <li> <p>Pending Action: Create</p> </li> <li> <p>New Request: Delete</p> </li> <li> <p>Result: The new delete, pending or immediate, replaces the pending create.</p> </li> </ul> </li> <li> <p>Scenario-4</p> <ul> <li> <p>Pending Action: Create</p> </li> <li> <p>New Request: Create</p> </li> <li> <p>Result: The new create is added to the pending create.</p> <important> <p> <b>Important:</b> If the new create request is <b>Apply Immediately - Yes</b>, all creates are performed immediately. If the new create request is <b>Apply Immediately - No</b>, all creates are pending.</p> </important> </li> </ul> </li> </ul>"""
    cache_security_group_names: NotRequired[
        "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
    ]
    """<p>A list of cache security group names to authorize on this cluster. This change is asynchronously applied as soon as possible.</p> <p>You can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).</p> <p>Constraints: Must contain no more than 255 alphanumeric characters. Must not be "Default".</p>"""
    security_group_ids: NotRequired[
        "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>Specifies the VPC Security Groups associated with the cluster.</p> <p>This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).</p>"""
    preferred_maintenance_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    notification_topic_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be same as the cluster owner.</p> </note>"""
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to apply to this cluster. This change is asynchronously applied as soon as possible for parameters when the <code>ApplyImmediately</code> parameter is specified as <code>true</code> for this request.</p>"""
    notification_topic_status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The status of the Amazon SNS notification topic. Notifications are sent only if the status is <code>active</code>.</p> <p>Valid values: <code>active</code> | <code>inactive</code> </p>"""
    apply_immediately: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>If <code>true</code>, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the cluster.</p> <p>If <code>false</code>, changes to the cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.</p> <important> <p>If you perform a <code>ModifyCacheCluster</code> before a pending modification is applied, the pending modification is replaced by the newer modification. However, a pending node-count increase on Memcached clusters cannot be superseded by a request to add fewer nodes. To change a pending node addition, first cancel it by setting <code>NumCacheNodes</code> equal to the current number of nodes in the cluster, then submit the new request. See the <code>NumCacheNodes</code> parameter for details on node scaling behavior.</p> </important> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default: <code>false</code> </p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The engine type used by the cache cluster. The options are valkey, memcached or redis.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The upgraded version of the cache engine to be run on the cache nodes.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version. </p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p> If you are running Valkey 7.2 or Redis OSS engine version 6.0 or later, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <note> <p>If the value of <code>SnapshotRetentionLimit</code> is set to zero (0), backups are turned off.</p> </note>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster. </p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>A valid cache node type that you want to scale this cluster up to.</p>"""
    auth_token: NotRequired["capo_elasticache.types.string.String"]
    """<p>Reserved parameter. The password used to access a password protected server. This parameter must be specified with the <code>auth-token-update</code> parameter. Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length</p> </li> <li> <p>Cannot contain any of the following characters: '/', '"', or '@', '%'</p> </li> </ul> <p> For more information, see AUTH password at <a href="http://redis.io/commands/AUTH">AUTH</a>.</p>"""
    auth_token_update_strategy: NotRequired[
        "capo_elasticache.types.auth_token_update_strategy_type.AuthTokenUpdateStrategyType"
    ]
    """<p>Specifies the strategy to use to update the AUTH token. This parameter must be specified with the <code>auth-token</code> parameter. Possible values:</p> <ul> <li> <p>ROTATE - default, if no update strategy is provided</p> </li> <li> <p>SET - allowed only after ROTATE</p> </li> <li> <p>DELETE - allowed only when transitioning to RBAC</p> </li> </ul> <p> For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html">Authenticating Users with AUTH</a> </p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
    ]
    """<p>Specifies the destination, format and type of the logs.</p>"""
    ip_discovery: NotRequired["capo_elasticache.types.ip_discovery.IpDiscovery"]
    """<p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    scale_config: NotRequired["capo_elasticache.types.scale_config.ScaleConfig"]
    """<p>Configures horizontal or vertical scaling for Memcached clusters, specifying the scaling percentage and interval.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCacheClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "num_cache_nodes" in value:
        pairs.append((f"{key_prefix}NumCacheNodes", str(value["num_cache_nodes"])))
    if "cache_node_ids_to_remove" in value:
        import capo_elasticache.types.cache_node_ids_list

        capo_elasticache.types.cache_node_ids_list.serialize_query(
            value["cache_node_ids_to_remove"],
            pairs,
            f"{key_prefix}CacheNodeIdsToRemove",
        )
    if "az_mode" in value:
        import capo_elasticache.types.az_mode

        capo_elasticache.types.az_mode.serialize_query(
            value["az_mode"], pairs, f"{key_prefix}AZMode"
        )
    if "new_availability_zones" in value:
        import capo_elasticache.types.preferred_availability_zone_list

        capo_elasticache.types.preferred_availability_zone_list.serialize_query(
            value["new_availability_zones"], pairs, f"{key_prefix}NewAvailabilityZones"
        )
    if "cache_security_group_names" in value:
        import capo_elasticache.types.cache_security_group_name_list

        capo_elasticache.types.cache_security_group_name_list.serialize_query(
            value["cache_security_group_names"],
            pairs,
            f"{key_prefix}CacheSecurityGroupNames",
        )
    if "security_group_ids" in value:
        import capo_elasticache.types.security_group_ids_list

        capo_elasticache.types.security_group_ids_list.serialize_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupIds"
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "notification_topic_arn" in value:
        pairs.append(
            (f"{key_prefix}NotificationTopicArn", str(value["notification_topic_arn"]))
        )
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "notification_topic_status" in value:
        pairs.append(
            (
                f"{key_prefix}NotificationTopicStatus",
                str(value["notification_topic_status"]),
            )
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{key_prefix}ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
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
    if "cache_node_type" in value:
        pairs.append((f"{key_prefix}CacheNodeType", str(value["cache_node_type"])))
    if "auth_token" in value:
        pairs.append((f"{key_prefix}AuthToken", str(value["auth_token"])))
    if "auth_token_update_strategy" in value:
        import capo_elasticache.types.auth_token_update_strategy_type

        capo_elasticache.types.auth_token_update_strategy_type.serialize_query(
            value["auth_token_update_strategy"],
            pairs,
            f"{key_prefix}AuthTokenUpdateStrategy",
        )
    if "log_delivery_configurations" in value:
        import capo_elasticache.types.log_delivery_configuration_request_list

        capo_elasticache.types.log_delivery_configuration_request_list.serialize_query(
            value["log_delivery_configurations"],
            pairs,
            f"{key_prefix}LogDeliveryConfigurations",
        )
    if "ip_discovery" in value:
        import capo_elasticache.types.ip_discovery

        capo_elasticache.types.ip_discovery.serialize_query(
            value["ip_discovery"], pairs, f"{key_prefix}IpDiscovery"
        )
    if "scale_config" in value:
        import capo_elasticache.types.scale_config

        capo_elasticache.types.scale_config.serialize_query(
            value["scale_config"], pairs, f"{key_prefix}ScaleConfig"
        )


def deserialize_query(el: Element) -> ModifyCacheClusterMessage:
    out: ModifyCacheClusterMessage = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_num_cache_nodes = el.find("NumCacheNodes")
    if child_num_cache_nodes is not None:
        out["num_cache_nodes"] = int(child_num_cache_nodes.text or "")
    child_cache_node_ids_to_remove = el.find("CacheNodeIdsToRemove")
    if child_cache_node_ids_to_remove is not None:
        import capo_elasticache.types.cache_node_ids_list

        out["cache_node_ids_to_remove"] = (
            capo_elasticache.types.cache_node_ids_list.deserialize_query(
                child_cache_node_ids_to_remove
            )
        )
    child_az_mode = el.find("AZMode")
    if child_az_mode is not None:
        import capo_elasticache.types.az_mode

        out["az_mode"] = capo_elasticache.types.az_mode.deserialize_query(child_az_mode)
    child_new_availability_zones = el.find("NewAvailabilityZones")
    if child_new_availability_zones is not None:
        import capo_elasticache.types.preferred_availability_zone_list

        out["new_availability_zones"] = (
            capo_elasticache.types.preferred_availability_zone_list.deserialize_query(
                child_new_availability_zones
            )
        )
    child_cache_security_group_names = el.find("CacheSecurityGroupNames")
    if child_cache_security_group_names is not None:
        import capo_elasticache.types.cache_security_group_name_list

        out["cache_security_group_names"] = (
            capo_elasticache.types.cache_security_group_name_list.deserialize_query(
                child_cache_security_group_names
            )
        )
    child_security_group_ids = el.find("SecurityGroupIds")
    if child_security_group_ids is not None:
        import capo_elasticache.types.security_group_ids_list

        out["security_group_ids"] = (
            capo_elasticache.types.security_group_ids_list.deserialize_query(
                child_security_group_ids
            )
        )
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_notification_topic_arn = el.find("NotificationTopicArn")
    if child_notification_topic_arn is not None:
        out["notification_topic_arn"] = str(child_notification_topic_arn.text or "")
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_notification_topic_status = el.find("NotificationTopicStatus")
    if child_notification_topic_status is not None:
        out["notification_topic_status"] = str(
            child_notification_topic_status.text or ""
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
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
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_auth_token = el.find("AuthToken")
    if child_auth_token is not None:
        out["auth_token"] = str(child_auth_token.text or "")
    child_auth_token_update_strategy = el.find("AuthTokenUpdateStrategy")
    if child_auth_token_update_strategy is not None:
        import capo_elasticache.types.auth_token_update_strategy_type

        out["auth_token_update_strategy"] = (
            capo_elasticache.types.auth_token_update_strategy_type.deserialize_query(
                child_auth_token_update_strategy
            )
        )
    child_log_delivery_configurations = el.find("LogDeliveryConfigurations")
    if child_log_delivery_configurations is not None:
        import capo_elasticache.types.log_delivery_configuration_request_list

        out["log_delivery_configurations"] = (
            capo_elasticache.types.log_delivery_configuration_request_list.deserialize_query(
                child_log_delivery_configurations
            )
        )
    child_ip_discovery = el.find("IpDiscovery")
    if child_ip_discovery is not None:
        import capo_elasticache.types.ip_discovery

        out["ip_discovery"] = capo_elasticache.types.ip_discovery.deserialize_query(
            child_ip_discovery
        )
    child_scale_config = el.find("ScaleConfig")
    if child_scale_config is not None:
        import capo_elasticache.types.scale_config

        out["scale_config"] = capo_elasticache.types.scale_config.deserialize_query(
            child_scale_config
        )
    return out

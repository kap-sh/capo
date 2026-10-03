"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.auth_token_update_strategy_type
    import capo_elasticache.types.boolean
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_security_group_name_list
    import capo_elasticache.types.cluster_mode
    import capo_elasticache.types.durability
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.log_delivery_configuration_request_list
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.string
    import capo_elasticache.types.transit_encryption_mode
    import capo_elasticache.types.user_group_id_list


class ModifyReplicationGroupMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the replication group to modify.</p>"""
    replication_group_description: NotRequired["capo_elasticache.types.string.String"]
    """<p>A description for the replication group. Maximum length is 255 characters.</p>"""
    primary_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.</p>"""
    snapshotting_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Valkey or Redis OSS (cluster mode enabled) replication groups.</p>"""
    automatic_failover_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.</p> <p>Valid values: <code>true</code> | <code>false</code> </p>"""
    multi_az_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag to indicate MultiAZ is enabled.</p>"""
    node_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>Deprecated. This parameter is not used.</p>"""
    cache_security_group_names: NotRequired[
        "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
    ]
    """<p>A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.</p> <p>This parameter can be used only with replication group containing clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).</p> <p>Constraints: Must contain no more than 255 alphanumeric characters. Must not be <code>Default</code>.</p>"""
    security_group_ids: NotRequired[
        "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>Specifies the VPC Security Groups associated with the clusters in the replication group.</p> <p>This parameter can be used only with replication group containing clusters running in an Amazon Virtual Private Cloud (Amazon VPC).</p>"""
    preferred_maintenance_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    notification_topic_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be same as the replication group owner. </p> </note>"""
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the <code>ApplyImmediately</code> parameter is specified as <code>true</code> for this request.</p>"""
    notification_topic_status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is <code>active</code>.</p> <p>Valid values: <code>active</code> | <code>inactive</code> </p>"""
    apply_immediately: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>If <code>true</code>, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the replication group.</p> <p>If <code>false</code>, changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default: <code>false</code> </p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>Modifies the engine listed in a replication group message. The options are valkey, memcached or redis.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The upgraded version of the cache engine to be run on the clusters in the replication group.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version. </p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p> If you are running Valkey or Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <p> <b>Important</b> If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.</p>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by <code>SnapshottingClusterId</code>.</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>A valid cache node type that you want to scale this replication group to.</p>"""
    auth_token: NotRequired["capo_elasticache.types.string.String"]
    """<p>Reserved parameter. The password used to access a password protected server. This parameter must be specified with the <code>auth-token-update-strategy </code> parameter. Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length</p> </li> <li> <p>Cannot contain any of the following characters: '/', '"', or '@', '%'</p> </li> </ul> <p> For more information, see AUTH password at <a href="http://redis.io/commands/AUTH">AUTH</a>.</p>"""
    auth_token_update_strategy: NotRequired[
        "capo_elasticache.types.auth_token_update_strategy_type.AuthTokenUpdateStrategyType"
    ]
    """<p>Specifies the strategy to use to update the AUTH token. This parameter must be specified with the <code>auth-token</code> parameter. Possible values:</p> <ul> <li> <p>ROTATE - default, if no update strategy is provided</p> </li> <li> <p>SET - allowed only after ROTATE</p> </li> <li> <p>DELETE - allowed only when transitioning to RBAC</p> </li> </ul> <p> For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html">Authenticating Users with AUTH</a> </p>"""
    user_group_ids_to_add: NotRequired[
        "capo_elasticache.types.user_group_id_list.UserGroupIdList"
    ]
    """<p>The ID of the user group you are associating with the replication group.</p>"""
    user_group_ids_to_remove: NotRequired[
        "capo_elasticache.types.user_group_id_list.UserGroupIdList"
    ]
    """<p>The ID of the user group to disassociate from the replication group, meaning the users in the group no longer can access the replication group.</p>"""
    remove_user_groups: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Removes the user group associated with this replication group.</p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
    ]
    """<p>Specifies the destination, format and type of the logs.</p>"""
    ip_discovery: NotRequired["capo_elasticache.types.ip_discovery.IpDiscovery"]
    """<p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    transit_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables in-transit encryption when set to true. If you are enabling in-transit encryption for an existing cluster, you must also set <code>TransitEncryptionMode</code> to <code>preferred</code>.</p>"""
    transit_encryption_mode: NotRequired[
        "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
    ]
    """<p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p> <p>You must set <code>TransitEncryptionEnabled</code> to <code>true</code>, for your existing cluster, and set <code>TransitEncryptionMode</code> to <code>preferred</code> in the same request to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Valkey or Redis OSS clients to use encrypted connections you can set the value to <code>required</code> to allow encrypted connections only.</p> <p>Setting <code>TransitEncryptionMode</code> to <code>required</code> is a two-step process that requires you to first set the <code>TransitEncryptionMode</code> to <code>preferred</code>, after that you can set <code>TransitEncryptionMode</code> to <code>required</code>. </p>"""
    cluster_mode: NotRequired["capo_elasticache.types.cluster_mode.ClusterMode"]
    """<p>Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.</p>"""
    durability: NotRequired["capo_elasticache.types.durability.Durability"]
    """<p>Specifies the durability setting for the replication group. Use this parameter to change the durability mode of an existing replication group, for example from <code>sync</code> to <code>async</code> or vice versa. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html">Durability</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyReplicationGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
    if "primary_cluster_id" in value:
        pairs.append(
            (f"{key_prefix}PrimaryClusterId", str(value["primary_cluster_id"]))
        )
    if "snapshotting_cluster_id" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshottingClusterId",
                str(value["snapshotting_cluster_id"]),
            )
        )
    if "automatic_failover_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}AutomaticFailoverEnabled",
                "true" if value["automatic_failover_enabled"] else "false",
            )
        )
    if "multi_az_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}MultiAZEnabled",
                "true" if value["multi_az_enabled"] else "false",
            )
        )
    if "node_group_id" in value:
        pairs.append((f"{key_prefix}NodeGroupId", str(value["node_group_id"])))
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
    if "user_group_ids_to_add" in value:
        import capo_elasticache.types.user_group_id_list

        capo_elasticache.types.user_group_id_list.serialize_query(
            value["user_group_ids_to_add"], pairs, f"{key_prefix}UserGroupIdsToAdd"
        )
    if "user_group_ids_to_remove" in value:
        import capo_elasticache.types.user_group_id_list

        capo_elasticache.types.user_group_id_list.serialize_query(
            value["user_group_ids_to_remove"],
            pairs,
            f"{key_prefix}UserGroupIdsToRemove",
        )
    if "remove_user_groups" in value:
        pairs.append(
            (
                f"{key_prefix}RemoveUserGroups",
                "true" if value["remove_user_groups"] else "false",
            )
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
    if "transit_encryption_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}TransitEncryptionEnabled",
                "true" if value["transit_encryption_enabled"] else "false",
            )
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
    if "durability" in value:
        import capo_elasticache.types.durability

        capo_elasticache.types.durability.serialize_query(
            value["durability"], pairs, f"{key_prefix}Durability"
        )


def deserialize_query(el: Element) -> ModifyReplicationGroupMessage:
    out: ModifyReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_replication_group_description = el.find("ReplicationGroupDescription")
    if child_replication_group_description is not None:
        out["replication_group_description"] = str(
            child_replication_group_description.text or ""
        )
    child_primary_cluster_id = el.find("PrimaryClusterId")
    if child_primary_cluster_id is not None:
        out["primary_cluster_id"] = str(child_primary_cluster_id.text or "")
    child_snapshotting_cluster_id = el.find("SnapshottingClusterId")
    if child_snapshotting_cluster_id is not None:
        out["snapshotting_cluster_id"] = str(child_snapshotting_cluster_id.text or "")
    child_automatic_failover_enabled = el.find("AutomaticFailoverEnabled")
    if child_automatic_failover_enabled is not None:
        out["automatic_failover_enabled"] = (
            child_automatic_failover_enabled.text or ""
        ).lower() == "true"
    child_multi_az_enabled = el.find("MultiAZEnabled")
    if child_multi_az_enabled is not None:
        out["multi_az_enabled"] = (child_multi_az_enabled.text or "").lower() == "true"
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
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
    child_user_group_ids_to_add = el.find("UserGroupIdsToAdd")
    if child_user_group_ids_to_add is not None:
        import capo_elasticache.types.user_group_id_list

        out["user_group_ids_to_add"] = (
            capo_elasticache.types.user_group_id_list.deserialize_query(
                child_user_group_ids_to_add
            )
        )
    child_user_group_ids_to_remove = el.find("UserGroupIdsToRemove")
    if child_user_group_ids_to_remove is not None:
        import capo_elasticache.types.user_group_id_list

        out["user_group_ids_to_remove"] = (
            capo_elasticache.types.user_group_id_list.deserialize_query(
                child_user_group_ids_to_remove
            )
        )
    child_remove_user_groups = el.find("RemoveUserGroups")
    if child_remove_user_groups is not None:
        out["remove_user_groups"] = (
            child_remove_user_groups.text or ""
        ).lower() == "true"
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
    child_transit_encryption_enabled = el.find("TransitEncryptionEnabled")
    if child_transit_encryption_enabled is not None:
        out["transit_encryption_enabled"] = (
            child_transit_encryption_enabled.text or ""
        ).lower() == "true"
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
    child_durability = el.find("Durability")
    if child_durability is not None:
        import capo_elasticache.types.durability

        out["durability"] = capo_elasticache.types.durability.deserialize_query(
            child_durability
        )
    return out

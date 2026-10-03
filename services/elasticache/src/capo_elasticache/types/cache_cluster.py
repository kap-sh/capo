"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_node_list
    import capo_elasticache.types.cache_parameter_group_status
    import capo_elasticache.types.cache_security_group_membership_list
    import capo_elasticache.types.endpoint
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.log_delivery_configuration_list
    import capo_elasticache.types.network_type
    import capo_elasticache.types.notification_configuration
    import capo_elasticache.types.pending_modified_values
    import capo_elasticache.types.security_group_membership_list
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp
    import capo_elasticache.types.transit_encryption_mode


class CacheCluster(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.</p>"""
    configuration_endpoint: NotRequired["capo_elasticache.types.endpoint.Endpoint"]
    """<p>Represents a Memcached cluster endpoint which can be used by an application to connect to any node in the cluster. The configuration endpoint will always have <code>.cfg</code> in it.</p> <p>Example: <code>mem-3.9dvc4r<u>.cfg</u>.usw2.cache.amazonaws.com:11211</code> </p>"""
    client_download_landing_page: NotRequired["capo_elasticache.types.string.String"]
    """<p>The URL of the web page where you can download the latest ElastiCache client library.</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the compute and memory capacity node type for the cluster.</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache engine (<code>memcached</code> or <code>redis</code>) to be used for this cluster.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The version of the cache engine that is used in this cluster.</p>"""
    cache_cluster_status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The current state of this cluster, one of the following values: <code>available</code>, <code>creating</code>, <code>deleted</code>, <code>deleting</code>, <code>incompatible-network</code>, <code>modifying</code>, <code>rebooting cluster nodes</code>, <code>restore-failed</code>, or <code>snapshotting</code>.</p>"""
    num_cache_nodes: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of cache nodes in the cluster.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p>"""
    preferred_availability_zone: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.</p>"""
    preferred_outpost_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The outpost ARN in which the cache cluster is created.</p>"""
    cache_cluster_create_time: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time when the cluster was created.</p>"""
    preferred_maintenance_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    pending_modified_values: NotRequired[
        "capo_elasticache.types.pending_modified_values.PendingModifiedValues"
    ]
    notification_configuration: NotRequired[
        "capo_elasticache.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). </p>"""
    cache_security_groups: NotRequired[
        "capo_elasticache.types.cache_security_group_membership_list.CacheSecurityGroupMembershipList"
    ]
    """<p>A list of cache security group elements, composed of name and status sub-elements.</p>"""
    cache_parameter_group: NotRequired[
        "capo_elasticache.types.cache_parameter_group_status.CacheParameterGroupStatus"
    ]
    """<p>Status of the cache parameter group.</p>"""
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache subnet group associated with the cluster.</p>"""
    cache_nodes: NotRequired["capo_elasticache.types.cache_node_list.CacheNodeList"]
    """<p>A list of cache nodes that are members of the cluster.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p> If you are running Valkey or Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    security_groups: NotRequired[
        "capo_elasticache.types.security_group_membership_list.SecurityGroupMembershipList"
    ]
    """<p>A list of VPC Security Groups associated with the cluster.</p>"""
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.</p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <important> <p> If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.</p> </important>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.</p> <p>Example: <code>05:00-09:00</code> </p>"""
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
    """<p>A flag that enables encryption at-rest when set to <code>true</code>.</p> <p>You cannot modify the value of <code>AtRestEncryptionEnabled</code> after the cluster is created. To enable at-rest encryption on a cluster you must set <code>AtRestEncryptionEnabled</code> to <code>true</code> when you create a cluster.</p> <p> <b>Required:</b> Only available when creating a replication group in an Amazon VPC using Redis OSS version <code>3.2.6</code>, <code>4.x</code> or later.</p> <p>Default: <code>false</code> </p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the cache cluster.</p>"""
    replication_group_log_delivery_enabled: NotRequired[
        "capo_elasticache.types.boolean.Boolean"
    ]
    """<p>A boolean value indicating whether log delivery is enabled for the replication group.</p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.log_delivery_configuration_list.LogDeliveryConfigurationList"
    ]
    """<p>Returns the destination, format and type of the logs.</p>"""
    network_type: NotRequired["capo_elasticache.types.network_type.NetworkType"]
    """<p>Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    ip_discovery: NotRequired["capo_elasticache.types.ip_discovery.IpDiscovery"]
    """<p>The network type associated with the cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    transit_encryption_mode: NotRequired[
        "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
    ]
    """<p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheCluster, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "configuration_endpoint" in value:
        import capo_elasticache.types.endpoint

        capo_elasticache.types.endpoint.serialize_query(
            value["configuration_endpoint"], pairs, f"{key_prefix}ConfigurationEndpoint"
        )
    if "client_download_landing_page" in value:
        pairs.append(
            (
                f"{key_prefix}ClientDownloadLandingPage",
                str(value["client_download_landing_page"]),
            )
        )
    if "cache_node_type" in value:
        pairs.append((f"{key_prefix}CacheNodeType", str(value["cache_node_type"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "cache_cluster_status" in value:
        pairs.append(
            (f"{key_prefix}CacheClusterStatus", str(value["cache_cluster_status"]))
        )
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
    if "pending_modified_values" in value:
        import capo_elasticache.types.pending_modified_values

        capo_elasticache.types.pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "notification_configuration" in value:
        import capo_elasticache.types.notification_configuration

        capo_elasticache.types.notification_configuration.serialize_query(
            value["notification_configuration"],
            pairs,
            f"{key_prefix}NotificationConfiguration",
        )
    if "cache_security_groups" in value:
        import capo_elasticache.types.cache_security_group_membership_list

        capo_elasticache.types.cache_security_group_membership_list.serialize_query(
            value["cache_security_groups"], pairs, f"{key_prefix}CacheSecurityGroups"
        )
    if "cache_parameter_group" in value:
        import capo_elasticache.types.cache_parameter_group_status

        capo_elasticache.types.cache_parameter_group_status.serialize_query(
            value["cache_parameter_group"], pairs, f"{key_prefix}CacheParameterGroup"
        )
    if "cache_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}CacheSubnetGroupName", str(value["cache_subnet_group_name"]))
        )
    if "cache_nodes" in value:
        import capo_elasticache.types.cache_node_list

        capo_elasticache.types.cache_node_list.serialize_query(
            value["cache_nodes"], pairs, f"{key_prefix}CacheNodes"
        )
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "security_groups" in value:
        import capo_elasticache.types.security_group_membership_list

        capo_elasticache.types.security_group_membership_list.serialize_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
        )
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
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
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))
    if "replication_group_log_delivery_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ReplicationGroupLogDeliveryEnabled",
                "true" if value["replication_group_log_delivery_enabled"] else "false",
            )
        )
    if "log_delivery_configurations" in value:
        import capo_elasticache.types.log_delivery_configuration_list

        capo_elasticache.types.log_delivery_configuration_list.serialize_query(
            value["log_delivery_configurations"],
            pairs,
            f"{key_prefix}LogDeliveryConfigurations",
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


def deserialize_query(el: Element) -> CacheCluster:
    out: CacheCluster = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_configuration_endpoint = el.find("ConfigurationEndpoint")
    if child_configuration_endpoint is not None:
        import capo_elasticache.types.endpoint

        out["configuration_endpoint"] = (
            capo_elasticache.types.endpoint.deserialize_query(
                child_configuration_endpoint
            )
        )
    child_client_download_landing_page = el.find("ClientDownloadLandingPage")
    if child_client_download_landing_page is not None:
        out["client_download_landing_page"] = str(
            child_client_download_landing_page.text or ""
        )
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_cache_cluster_status = el.find("CacheClusterStatus")
    if child_cache_cluster_status is not None:
        out["cache_cluster_status"] = str(child_cache_cluster_status.text or "")
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
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_elasticache.types.pending_modified_values

        out["pending_modified_values"] = (
            capo_elasticache.types.pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_notification_configuration = el.find("NotificationConfiguration")
    if child_notification_configuration is not None:
        import capo_elasticache.types.notification_configuration

        out["notification_configuration"] = (
            capo_elasticache.types.notification_configuration.deserialize_query(
                child_notification_configuration
            )
        )
    child_cache_security_groups = el.find("CacheSecurityGroups")
    if child_cache_security_groups is not None:
        import capo_elasticache.types.cache_security_group_membership_list

        out["cache_security_groups"] = (
            capo_elasticache.types.cache_security_group_membership_list.deserialize_query(
                child_cache_security_groups
            )
        )
    child_cache_parameter_group = el.find("CacheParameterGroup")
    if child_cache_parameter_group is not None:
        import capo_elasticache.types.cache_parameter_group_status

        out["cache_parameter_group"] = (
            capo_elasticache.types.cache_parameter_group_status.deserialize_query(
                child_cache_parameter_group
            )
        )
    child_cache_subnet_group_name = el.find("CacheSubnetGroupName")
    if child_cache_subnet_group_name is not None:
        out["cache_subnet_group_name"] = str(child_cache_subnet_group_name.text or "")
    child_cache_nodes = el.find("CacheNodes")
    if child_cache_nodes is not None:
        import capo_elasticache.types.cache_node_list

        out["cache_nodes"] = capo_elasticache.types.cache_node_list.deserialize_query(
            child_cache_nodes
        )
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_elasticache.types.security_group_membership_list

        out["security_groups"] = (
            capo_elasticache.types.security_group_membership_list.deserialize_query(
                child_security_groups
            )
        )
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_snapshot_retention_limit = el.find("SnapshotRetentionLimit")
    if child_snapshot_retention_limit is not None:
        out["snapshot_retention_limit"] = int(child_snapshot_retention_limit.text or "")
    child_snapshot_window = el.find("SnapshotWindow")
    if child_snapshot_window is not None:
        out["snapshot_window"] = str(child_snapshot_window.text or "")
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
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_replication_group_log_delivery_enabled = el.find(
        "ReplicationGroupLogDeliveryEnabled"
    )
    if child_replication_group_log_delivery_enabled is not None:
        out["replication_group_log_delivery_enabled"] = (
            child_replication_group_log_delivery_enabled.text or ""
        ).lower() == "true"
    child_log_delivery_configurations = el.find("LogDeliveryConfigurations")
    if child_log_delivery_configurations is not None:
        import capo_elasticache.types.log_delivery_configuration_list

        out["log_delivery_configurations"] = (
            capo_elasticache.types.log_delivery_configuration_list.deserialize_query(
                child_log_delivery_configurations
            )
        )
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
    return out

"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.az_mode
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_security_group_name_list
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.log_delivery_configuration_request_list
    import capo_elasticache.types.network_type
    import capo_elasticache.types.outpost_mode
    import capo_elasticache.types.preferred_availability_zone_list
    import capo_elasticache.types.preferred_outpost_arn_list
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.snapshot_arns_list
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CreateCacheClusterMessage(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The node group (shard) identifier. This parameter is stored as a lowercase string.</p> <p> <b>Constraints:</b> </p> <ul> <li> <p>A name must contain from 1 to 50 alphanumeric characters or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>A name cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.</p> <p>If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>"""
    az_mode: NotRequired["capo_elasticache.types.az_mode.AZMode"]
    """<p>Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.</p> <p>This parameter is only supported for Memcached clusters.</p> <p>If the <code>AZMode</code> and <code>PreferredAvailabilityZones</code> are not specified, ElastiCache assumes <code>single-az</code> mode.</p>"""
    preferred_availability_zone: NotRequired["capo_elasticache.types.string.String"]
    """<p>The EC2 Availability Zone in which the cluster is created.</p> <p>All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use <code>PreferredAvailabilityZones</code>.</p> <p>Default: System chosen Availability Zone.</p>"""
    preferred_availability_zones: NotRequired[
        "capo_elasticache.types.preferred_availability_zone_list.PreferredAvailabilityZoneList"
    ]
    """<p>A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.</p> <p>This option is only supported on Memcached.</p> <note> <p>If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.</p> <p>The number of Availability Zones listed must equal the value of <code>NumCacheNodes</code>.</p> </note> <p>If you want all the nodes in the same Availability Zone, use <code>PreferredAvailabilityZone</code> instead, or repeat the Availability Zone multiple times in the list.</p> <p>Default: System chosen Availability Zones.</p>"""
    num_cache_nodes: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The initial number of cache nodes that the cluster has.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p> <p>If you need more than 40 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at <a href="http://aws.amazon.com/contact-us/elasticache-node-limit-request/">http://aws.amazon.com/contact-us/elasticache-node-limit-request/</a>.</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The compute and memory capacity of the nodes in the node group (shard).</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache engine to be used for this cluster.</p> <p>Valid values for this parameter are: <code>memcached</code> | <code>redis</code> </p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version. </p>"""
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has <code>cluster-enabled='yes'</code> when creating a cluster.</p>"""
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the subnet group to be used for the cluster.</p> <p>Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).</p> <important> <p>If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html">Subnets and Subnet Groups</a>.</p> </important>"""
    cache_security_group_names: NotRequired[
        "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
    ]
    """<p>A list of security group names to associate with this cluster.</p> <p>Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).</p>"""
    security_group_ids: NotRequired[
        "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>One or more VPC security groups associated with the cluster.</p> <p>Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource.</p>"""
    snapshot_arns: NotRequired[
        "capo_elasticache.types.snapshot_arns_list.SnapshotArnsList"
    ]
    """<p>A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Valkey or Redis OSS RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note> <p>Example of an Amazon S3 ARN: <code>arn:aws:s3:::my_bucket/snapshot1.rdb</code> </p>"""
    snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of a Valkey or Redis OSS snapshot from which to restore data into the new node group (shard). The snapshot status changes to <code>restoring</code> while the new node group (shard) is being created.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>"""
    preferred_maintenance_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. </p>"""
    port: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The port number on which each of the cache nodes accepts connections.</p>"""
    notification_topic_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be the same as the cluster owner.</p> </note>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p> If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot taken today is retained for 5 days before being deleted.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note> <p>Default: 0 (i.e., automatic backups are disabled for this cache cluster).</p>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>"""
    auth_token: NotRequired["capo_elasticache.types.string.String"]
    """<p> <b>Reserved parameter.</b> The password used to access a password protected server.</p> <p>Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters.</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length.</p> </li> <li> <p>The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.</p> </li> </ul> <p>For more information, see <a href="http://redis.io/commands/AUTH">AUTH password</a> at http://redis.io/commands/AUTH.</p>"""
    outpost_mode: NotRequired["capo_elasticache.types.outpost_mode.OutpostMode"]
    """<p>Specifies whether the nodes in the cluster are created in a single outpost or across multiple outposts.</p>"""
    preferred_outpost_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The outpost ARN in which the cache cluster is created.</p>"""
    preferred_outpost_arns: NotRequired[
        "capo_elasticache.types.preferred_outpost_arn_list.PreferredOutpostArnList"
    ]
    """<p>The outpost ARNs in which the cache cluster is created.</p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
    ]
    """<p>Specifies the destination, format and type of the logs. </p>"""
    transit_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables in-transit encryption when set to true.</p>"""
    network_type: NotRequired["capo_elasticache.types.network_type.NetworkType"]
    """<p>Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>. </p>"""
    ip_discovery: NotRequired["capo_elasticache.types.ip_discovery.IpDiscovery"]
    """<p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCacheClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "az_mode" in value:
        import capo_elasticache.types.az_mode

        capo_elasticache.types.az_mode.serialize_query(
            value["az_mode"], pairs, f"{key_prefix}AZMode"
        )
    if "preferred_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredAvailabilityZone",
                str(value["preferred_availability_zone"]),
            )
        )
    if "preferred_availability_zones" in value:
        import capo_elasticache.types.preferred_availability_zone_list

        capo_elasticache.types.preferred_availability_zone_list.serialize_query(
            value["preferred_availability_zones"],
            pairs,
            f"{key_prefix}PreferredAvailabilityZones",
        )
    if "num_cache_nodes" in value:
        pairs.append((f"{key_prefix}NumCacheNodes", str(value["num_cache_nodes"])))
    if "cache_node_type" in value:
        pairs.append((f"{key_prefix}CacheNodeType", str(value["cache_node_type"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
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
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "snapshot_arns" in value:
        import capo_elasticache.types.snapshot_arns_list

        capo_elasticache.types.snapshot_arns_list.serialize_query(
            value["snapshot_arns"], pairs, f"{key_prefix}SnapshotArns"
        )
    if "snapshot_name" in value:
        pairs.append((f"{key_prefix}SnapshotName", str(value["snapshot_name"])))
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "notification_topic_arn" in value:
        pairs.append(
            (f"{key_prefix}NotificationTopicArn", str(value["notification_topic_arn"]))
        )
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
    if "auth_token" in value:
        pairs.append((f"{key_prefix}AuthToken", str(value["auth_token"])))
    if "outpost_mode" in value:
        import capo_elasticache.types.outpost_mode

        capo_elasticache.types.outpost_mode.serialize_query(
            value["outpost_mode"], pairs, f"{key_prefix}OutpostMode"
        )
    if "preferred_outpost_arn" in value:
        pairs.append(
            (f"{key_prefix}PreferredOutpostArn", str(value["preferred_outpost_arn"]))
        )
    if "preferred_outpost_arns" in value:
        import capo_elasticache.types.preferred_outpost_arn_list

        capo_elasticache.types.preferred_outpost_arn_list.serialize_query(
            value["preferred_outpost_arns"], pairs, f"{key_prefix}PreferredOutpostArns"
        )
    if "log_delivery_configurations" in value:
        import capo_elasticache.types.log_delivery_configuration_request_list

        capo_elasticache.types.log_delivery_configuration_request_list.serialize_query(
            value["log_delivery_configurations"],
            pairs,
            f"{key_prefix}LogDeliveryConfigurations",
        )
    if "transit_encryption_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}TransitEncryptionEnabled",
                "true" if value["transit_encryption_enabled"] else "false",
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


def deserialize_query(el: Element) -> CreateCacheClusterMessage:
    out: CreateCacheClusterMessage = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_az_mode = el.find("AZMode")
    if child_az_mode is not None:
        import capo_elasticache.types.az_mode

        out["az_mode"] = capo_elasticache.types.az_mode.deserialize_query(child_az_mode)
    child_preferred_availability_zone = el.find("PreferredAvailabilityZone")
    if child_preferred_availability_zone is not None:
        out["preferred_availability_zone"] = str(
            child_preferred_availability_zone.text or ""
        )
    child_preferred_availability_zones = el.find("PreferredAvailabilityZones")
    if child_preferred_availability_zones is not None:
        import capo_elasticache.types.preferred_availability_zone_list

        out["preferred_availability_zones"] = (
            capo_elasticache.types.preferred_availability_zone_list.deserialize_query(
                child_preferred_availability_zones
            )
        )
    child_num_cache_nodes = el.find("NumCacheNodes")
    if child_num_cache_nodes is not None:
        out["num_cache_nodes"] = int(child_num_cache_nodes.text or "")
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_cache_subnet_group_name = el.find("CacheSubnetGroupName")
    if child_cache_subnet_group_name is not None:
        out["cache_subnet_group_name"] = str(child_cache_subnet_group_name.text or "")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    child_snapshot_arns = el.find("SnapshotArns")
    if child_snapshot_arns is not None:
        import capo_elasticache.types.snapshot_arns_list

        out["snapshot_arns"] = (
            capo_elasticache.types.snapshot_arns_list.deserialize_query(
                child_snapshot_arns
            )
        )
    child_snapshot_name = el.find("SnapshotName")
    if child_snapshot_name is not None:
        out["snapshot_name"] = str(child_snapshot_name.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_notification_topic_arn = el.find("NotificationTopicArn")
    if child_notification_topic_arn is not None:
        out["notification_topic_arn"] = str(child_notification_topic_arn.text or "")
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
    child_auth_token = el.find("AuthToken")
    if child_auth_token is not None:
        out["auth_token"] = str(child_auth_token.text or "")
    child_outpost_mode = el.find("OutpostMode")
    if child_outpost_mode is not None:
        import capo_elasticache.types.outpost_mode

        out["outpost_mode"] = capo_elasticache.types.outpost_mode.deserialize_query(
            child_outpost_mode
        )
    child_preferred_outpost_arn = el.find("PreferredOutpostArn")
    if child_preferred_outpost_arn is not None:
        out["preferred_outpost_arn"] = str(child_preferred_outpost_arn.text or "")
    child_preferred_outpost_arns = el.find("PreferredOutpostArns")
    if child_preferred_outpost_arns is not None:
        import capo_elasticache.types.preferred_outpost_arn_list

        out["preferred_outpost_arns"] = (
            capo_elasticache.types.preferred_outpost_arn_list.deserialize_query(
                child_preferred_outpost_arns
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
    child_transit_encryption_enabled = el.find("TransitEncryptionEnabled")
    if child_transit_encryption_enabled is not None:
        out["transit_encryption_enabled"] = (
            child_transit_encryption_enabled.text or ""
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
    return out

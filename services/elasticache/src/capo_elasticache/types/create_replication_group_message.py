"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.availability_zones_list
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_security_group_name_list
    import capo_elasticache.types.cluster_mode
    import capo_elasticache.types.durability
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.log_delivery_configuration_request_list
    import capo_elasticache.types.network_type
    import capo_elasticache.types.node_group_configuration_list
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.snapshot_arns_list
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list
    import capo_elasticache.types.transit_encryption_mode
    import capo_elasticache.types.user_group_id_list_input


class CreateReplicationGroupMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The replication group identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>A name must contain from 1 to 40 alphanumeric characters or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>A name cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    replication_group_description: NotRequired["capo_elasticache.types.string.String"]
    """<p>A user-created description for the replication group.</p>"""
    global_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    primary_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of <code>available</code>.</p> <p>This parameter is not required if <code>NumCacheClusters</code>, <code>NumNodeGroups</code>, or <code>ReplicasPerNodeGroup</code> is specified.</p>"""
    automatic_failover_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.</p> <p> <code>AutomaticFailoverEnabled</code> must be enabled for Valkey or Redis OSS (cluster mode enabled) replication groups.</p> <p>Default: false</p>"""
    multi_az_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html">Minimizing Downtime: Multi-AZ</a>.</p>"""
    num_cache_clusters: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of clusters this replication group initially has.</p> <p>This parameter is not used if there is more than one node group (shard). You should use <code>ReplicasPerNodeGroup</code> instead.</p> <p>If <code>AutomaticFailoverEnabled</code> is <code>true</code>, the value of this parameter must be at least 2. If <code>AutomaticFailoverEnabled</code> is <code>false</code> you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.</p> <p>The maximum permitted value for <code>NumCacheClusters</code> is 6 (1 primary plus 5 replicas).</p>"""
    preferred_cache_cluster_a_zs: NotRequired[
        "capo_elasticache.types.availability_zones_list.AvailabilityZonesList"
    ]
    """<p>A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.</p> <p>This parameter is not used if there is more than one node group (shard). You should use <code>NodeGroupConfiguration</code> instead.</p> <note> <p>If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.</p> <p>The number of Availability Zones listed must equal the value of <code>NumCacheClusters</code>.</p> </note> <p>Default: system chosen Availability Zones.</p>"""
    num_node_groups: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>An optional parameter that specifies the number of node groups (shards) for this Valkey or Redis OSS (cluster mode enabled) replication group. For Valkey or Redis OSS (cluster mode disabled) either omit this parameter or set it to 1.</p> <p>Default: 1</p>"""
    replicas_per_node_group: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.</p>"""
    node_group_configuration: NotRequired[
        "capo_elasticache.types.node_group_configuration_list.NodeGroupConfigurationList"
    ]
    """<p>A list of node group (shard) configuration options. Each node group (shard) configuration has the following members: <code>PrimaryAvailabilityZone</code>, <code>ReplicaAvailabilityZones</code>, <code>ReplicaCount</code>, and <code>Slots</code>.</p> <p>If you're creating a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) replication group, you can use this parameter to individually configure each node group (shard), or you can omit this parameter. However, it is required when seeding a Valkey or Redis OSS (cluster mode enabled) cluster from a S3 rdb file. You must configure each node group (shard) using this parameter because you must specify the slots for each node group.</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The compute and memory capacity of the nodes in the node group (shard).</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache engine to be used for the clusters in this replication group. The value must be set to <code>valkey</code> or <code>redis</code>.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the <code>DescribeCacheEngineVersions</code> operation.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>) in the <i>ElastiCache User Guide</i>, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version. </p>"""
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.</p> <p>If you are running Valkey or Redis OSS version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name. </p> <ul> <li> <p>To create a Valkey or Redis OSS (cluster mode disabled) replication group, use <code>CacheParameterGroupName=default.redis3.2</code>.</p> </li> <li> <p>To create a Valkey or Redis OSS (cluster mode enabled) replication group, use <code>CacheParameterGroupName=default.redis3.2.cluster.on</code>.</p> </li> </ul>"""
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache subnet group to be used for the replication group.</p> <important> <p>If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html">Subnets and Subnet Groups</a>.</p> </important>"""
    cache_security_group_names: NotRequired[
        "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
    ]
    """<p>A list of cache security group names to associate with this replication group.</p>"""
    security_group_ids: NotRequired[
        "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>One or more Amazon VPC security groups associated with this replication group.</p> <p>Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=<code>myKey</code>, Value=<code>myKeyValue</code>. You can include multiple tags as shown following: Key=<code>myKey</code>, Value=<code>myKeyValue</code> Key=<code>mySecondKey</code>, Value=<code>mySecondKeyValue</code>. Tags on replication groups will be replicated to all nodes.</p>"""
    snapshot_arns: NotRequired[
        "capo_elasticache.types.snapshot_arns_list.SnapshotArnsList"
    ]
    """<p>A list of Amazon Resource Names (ARN) that uniquely identify the Valkey or Redis OSS RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter <i>NumNodeGroups</i> or the number of node groups configured by <i>NodeGroupConfiguration</i> regardless of the number of ARNs specified here.</p> <p>Example of an Amazon S3 ARN: <code>arn:aws:s3:::my_bucket/snapshot1.rdb</code> </p>"""
    snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to <code>restoring</code> while the new replication group is being created.</p>"""
    preferred_maintenance_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    port: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The port number on which each member of the replication group accepts connections.</p>"""
    notification_topic_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be the same as the cluster owner.</p> </note>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p> If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <p>Default: 0 (i.e., automatic backups are disabled for this cluster).</p>"""
    snapshot_window: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p>"""
    auth_token: NotRequired["capo_elasticache.types.string.String"]
    """<p> <b>Reserved parameter.</b> The password used to access a password protected server.</p> <p> <code>AuthToken</code> can be specified only on replication groups where <code>TransitEncryptionEnabled</code> is <code>true</code>.</p> <important> <p>For HIPAA compliance, you must specify <code>TransitEncryptionEnabled</code> as <code>true</code>, an <code>AuthToken</code>, and a <code>CacheSubnetGroup</code>.</p> </important> <p>Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters.</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length.</p> </li> <li> <p>The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.</p> </li> </ul> <p>For more information, see <a href="http://redis.io/commands/AUTH">AUTH password</a> at http://redis.io/commands/AUTH.</p>"""
    transit_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables in-transit encryption when set to <code>true</code>.</p> <p>This parameter is valid only if the <code>Engine</code> parameter is <code>redis</code>, the <code>EngineVersion</code> parameter is <code>3.2.6</code>, <code>4.x</code> or later, and the cluster is being created in an Amazon VPC.</p> <p>If you enable in-transit encryption, you must also specify a value for <code>CacheSubnetGroup</code>.</p> <p> <b>Required:</b> Only available when creating a replication group in an Amazon VPC using Redis OSS version <code>3.2.6</code>, <code>4.x</code> or later.</p> <p>Default: <code>false</code> </p> <important> <p>For HIPAA compliance, you must specify <code>TransitEncryptionEnabled</code> as <code>true</code>, an <code>AuthToken</code>, and a <code>CacheSubnetGroup</code>.</p> </important>"""
    at_rest_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables encryption at-rest on the replication group when set to <code>true</code>. In some cases, encryption at-rest may be enabled even when this value is false. Use <code>StorageEncryptionType</code> to view the effective encryption state of a cluster.</p> <p>You cannot modify the value of <code>AtRestEncryptionEnabled</code> after the replication group is created.</p> <p>Default: <code>true</code> when using Valkey, <code>false</code> when using Redis OSS</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the disk in the cluster.</p>"""
    user_group_ids: NotRequired[
        "capo_elasticache.types.user_group_id_list_input.UserGroupIdListInput"
    ]
    """<p>The user group to associate with the replication group.</p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
    ]
    """<p>Specifies the destination, format and type of the logs.</p>"""
    data_tiering_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html">Data tiering</a>.</p>"""
    network_type: NotRequired["capo_elasticache.types.network_type.NetworkType"]
    """<p>Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    ip_discovery: NotRequired["capo_elasticache.types.ip_discovery.IpDiscovery"]
    """<p>The network type you choose when creating a replication group, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""
    transit_encryption_mode: NotRequired[
        "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
    ]
    """<p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p> <p>When setting <code>TransitEncryptionEnabled</code> to <code>true</code>, you can set your <code>TransitEncryptionMode</code> to <code>preferred</code> in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Valkey or Redis OSS clients to use encrypted connections you can modify the value to <code>required</code> to allow encrypted connections only.</p> <p>Setting <code>TransitEncryptionMode</code> to <code>required</code> is a two-step process that requires you to first set the <code>TransitEncryptionMode</code> to <code>preferred</code>, after that you can set <code>TransitEncryptionMode</code> to <code>required</code>.</p> <p>This process will not trigger the replacement of the replication group.</p>"""
    cluster_mode: NotRequired["capo_elasticache.types.cluster_mode.ClusterMode"]
    """<p>Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.</p>"""
    serverless_cache_snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the snapshot used to create a replication group. Available for Valkey, Redis OSS only.</p>"""
    durability: NotRequired["capo_elasticache.types.durability.Durability"]
    """<p>Specifies the durability setting for the replication group. When set to <code>default</code>, the service determines the effective durability based on the engine version, cluster mode, and other parameters. The resolved setting is reflected in the <code>EffectiveDurability</code> property of the replication group. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html">Durability</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReplicationGroupMessage, pairs: list[tuple[str, str]], prefix: str
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
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "primary_cluster_id" in value:
        pairs.append(
            (f"{key_prefix}PrimaryClusterId", str(value["primary_cluster_id"]))
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
    if "num_cache_clusters" in value:
        pairs.append(
            (f"{key_prefix}NumCacheClusters", str(value["num_cache_clusters"]))
        )
    if "preferred_cache_cluster_a_zs" in value:
        import capo_elasticache.types.availability_zones_list

        capo_elasticache.types.availability_zones_list.serialize_query(
            value["preferred_cache_cluster_a_zs"],
            pairs,
            f"{key_prefix}PreferredCacheClusterAZs",
        )
    if "num_node_groups" in value:
        pairs.append((f"{key_prefix}NumNodeGroups", str(value["num_node_groups"])))
    if "replicas_per_node_group" in value:
        pairs.append(
            (f"{key_prefix}ReplicasPerNodeGroup", str(value["replicas_per_node_group"]))
        )
    if "node_group_configuration" in value:
        import capo_elasticache.types.node_group_configuration_list

        capo_elasticache.types.node_group_configuration_list.serialize_query(
            value["node_group_configuration"],
            pairs,
            f"{key_prefix}NodeGroupConfiguration",
        )
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
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "user_group_ids" in value:
        import capo_elasticache.types.user_group_id_list_input

        capo_elasticache.types.user_group_id_list_input.serialize_query(
            value["user_group_ids"], pairs, f"{key_prefix}UserGroupIds"
        )
    if "log_delivery_configurations" in value:
        import capo_elasticache.types.log_delivery_configuration_request_list

        capo_elasticache.types.log_delivery_configuration_request_list.serialize_query(
            value["log_delivery_configurations"],
            pairs,
            f"{key_prefix}LogDeliveryConfigurations",
        )
    if "data_tiering_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}DataTieringEnabled",
                "true" if value["data_tiering_enabled"] else "false",
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
    if "serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{key_prefix}ServerlessCacheSnapshotName",
                str(value["serverless_cache_snapshot_name"]),
            )
        )
    if "durability" in value:
        import capo_elasticache.types.durability

        capo_elasticache.types.durability.serialize_query(
            value["durability"], pairs, f"{key_prefix}Durability"
        )


def deserialize_query(el: Element) -> CreateReplicationGroupMessage:
    out: CreateReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_replication_group_description = el.find("ReplicationGroupDescription")
    if child_replication_group_description is not None:
        out["replication_group_description"] = str(
            child_replication_group_description.text or ""
        )
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_primary_cluster_id = el.find("PrimaryClusterId")
    if child_primary_cluster_id is not None:
        out["primary_cluster_id"] = str(child_primary_cluster_id.text or "")
    child_automatic_failover_enabled = el.find("AutomaticFailoverEnabled")
    if child_automatic_failover_enabled is not None:
        out["automatic_failover_enabled"] = (
            child_automatic_failover_enabled.text or ""
        ).lower() == "true"
    child_multi_az_enabled = el.find("MultiAZEnabled")
    if child_multi_az_enabled is not None:
        out["multi_az_enabled"] = (child_multi_az_enabled.text or "").lower() == "true"
    child_num_cache_clusters = el.find("NumCacheClusters")
    if child_num_cache_clusters is not None:
        out["num_cache_clusters"] = int(child_num_cache_clusters.text or "")
    child_preferred_cache_cluster_a_zs = el.find("PreferredCacheClusterAZs")
    if child_preferred_cache_cluster_a_zs is not None:
        import capo_elasticache.types.availability_zones_list

        out["preferred_cache_cluster_a_zs"] = (
            capo_elasticache.types.availability_zones_list.deserialize_query(
                child_preferred_cache_cluster_a_zs
            )
        )
    child_num_node_groups = el.find("NumNodeGroups")
    if child_num_node_groups is not None:
        out["num_node_groups"] = int(child_num_node_groups.text or "")
    child_replicas_per_node_group = el.find("ReplicasPerNodeGroup")
    if child_replicas_per_node_group is not None:
        out["replicas_per_node_group"] = int(child_replicas_per_node_group.text or "")
    child_node_group_configuration = el.find("NodeGroupConfiguration")
    if child_node_group_configuration is not None:
        import capo_elasticache.types.node_group_configuration_list

        out["node_group_configuration"] = (
            capo_elasticache.types.node_group_configuration_list.deserialize_query(
                child_node_group_configuration
            )
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
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_user_group_ids = el.find("UserGroupIds")
    if child_user_group_ids is not None:
        import capo_elasticache.types.user_group_id_list_input

        out["user_group_ids"] = (
            capo_elasticache.types.user_group_id_list_input.deserialize_query(
                child_user_group_ids
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
    child_data_tiering_enabled = el.find("DataTieringEnabled")
    if child_data_tiering_enabled is not None:
        out["data_tiering_enabled"] = (
            child_data_tiering_enabled.text or ""
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
    child_serverless_cache_snapshot_name = el.find("ServerlessCacheSnapshotName")
    if child_serverless_cache_snapshot_name is not None:
        out["serverless_cache_snapshot_name"] = str(
            child_serverless_cache_snapshot_name.text or ""
        )
    child_durability = el.find("Durability")
    if child_durability is not None:
        import capo_elasticache.types.durability

        out["durability"] = capo_elasticache.types.durability.deserialize_query(
            child_durability
        )
    return out

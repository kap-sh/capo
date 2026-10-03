"""Generated from Smithy shape ``com.amazonaws.memorydb#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.acl_name
    import capo_memorydb.types.az_status
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.cluster_pending_updates
    import capo_memorydb.types.data_tiering_status
    import capo_memorydb.types.endpoint
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.ip_discovery
    import capo_memorydb.types.network_type
    import capo_memorydb.types.security_group_membership_list
    import capo_memorydb.types.shard_list
    import capo_memorydb.types.string


class Cluster(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The user-supplied name of the cluster. This identifier is a unique key that identifies a cluster.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description of the cluster</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The status of the cluster. For example, Available, Updating, Creating.</p>"""
    pending_updates: NotRequired[
        "capo_memorydb.types.cluster_pending_updates.ClusterPendingUpdates"
    ]
    """<p>A group of settings that are currently being applied.</p>"""
    multi_region_cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-Region cluster that this cluster belongs to.</p>"""
    number_of_shards: NotRequired[
        "capo_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of shards in the cluster</p>"""
    shards: NotRequired["capo_memorydb.types.shard_list.ShardList"]
    """<p>A list of shards that are members of the cluster.</p>"""
    availability_mode: NotRequired["capo_memorydb.types.az_status.AZStatus"]
    """<p>Indicates if the cluster has a Multi-AZ configuration (multiaz) or not (singleaz).</p>"""
    cluster_endpoint: NotRequired["capo_memorydb.types.endpoint.Endpoint"]
    """<p>The cluster's configuration endpoint</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The cluster's node type</p>"""
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine used by the cluster.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Redis OSS engine version used by the cluster</p>"""
    engine_patch_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Redis OSS engine patch version used by the cluster</p>"""
    parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the parameter group used by the cluster</p>"""
    parameter_group_status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The status of the parameter group used by the cluster, for example 'active' or 'applying'.</p>"""
    security_groups: NotRequired[
        "capo_memorydb.types.security_group_membership_list.SecurityGroupMembershipList"
    ]
    """<p>A list of security groups used by the cluster</p>"""
    subnet_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the subnet group used by the cluster</p>"""
    tls_enabled: NotRequired["capo_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>A flag to indicate if In-transit encryption is enabled</p>"""
    kms_key_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the cluster</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    sns_topic_arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the SNS notification topic</p>"""
    sns_topic_status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The SNS topic must be in Active status to receive notifications</p>"""
    snapshot_retention_limit: NotRequired[
        "capo_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>"""
    maintenance_window: NotRequired["capo_memorydb.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. </p>"""
    snapshot_window: NotRequired["capo_memorydb.types.string.String"]
    """<p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.</p>"""
    acl_name: NotRequired["capo_memorydb.types.acl_name.ACLName"]
    """<p>The name of the Access Control List associated with this cluster.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_memorydb.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to true, the cluster will automatically receive minor engine version upgrades after launch.</p>"""
    data_tiering: NotRequired[
        "capo_memorydb.types.data_tiering_status.DataTieringStatus"
    ]
    """<p>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html">Data tiering</a>.</p>"""
    network_type: NotRequired["capo_memorydb.types.network_type.NetworkType"]
    """<p>The IP address type for the cluster. Returns 'ipv4' for IPv4 only, 'ipv6' for IPv6 only, or 'dual-stack' if the cluster supports both IPv4 and IPv6 addressing.</p>"""
    ip_discovery: NotRequired["capo_memorydb.types.ip_discovery.IpDiscovery"]
    """<p>The mechanism that the cluster uses to discover IP addresses. Returns 'ipv4' when DNS endpoints resolve to IPv4 addresses, or 'ipv6' when DNS endpoints resolve to IPv6 addresses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cluster) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        out["Status"] = value["status"]
    if "pending_updates" in value:
        import capo_memorydb.types.cluster_pending_updates

        out["PendingUpdates"] = (
            capo_memorydb.types.cluster_pending_updates.serialize_aws_json_1_1(
                value["pending_updates"]
            )
        )
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "number_of_shards" in value:
        out["NumberOfShards"] = value["number_of_shards"]
    if "shards" in value:
        import capo_memorydb.types.shard_list

        out["Shards"] = capo_memorydb.types.shard_list.serialize_aws_json_1_1(
            value["shards"]
        )
    if "availability_mode" in value:
        import capo_memorydb.types.az_status

        out["AvailabilityMode"] = capo_memorydb.types.az_status.serialize_aws_json_1_1(
            value["availability_mode"]
        )
    if "cluster_endpoint" in value:
        import capo_memorydb.types.endpoint

        out["ClusterEndpoint"] = capo_memorydb.types.endpoint.serialize_aws_json_1_1(
            value["cluster_endpoint"]
        )
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "engine_patch_version" in value:
        out["EnginePatchVersion"] = value["engine_patch_version"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "parameter_group_status" in value:
        out["ParameterGroupStatus"] = value["parameter_group_status"]
    if "security_groups" in value:
        import capo_memorydb.types.security_group_membership_list

        out["SecurityGroups"] = (
            capo_memorydb.types.security_group_membership_list.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "sns_topic_status" in value:
        out["SnsTopicStatus"] = value["sns_topic_status"]
    if "snapshot_retention_limit" in value:
        out["SnapshotRetentionLimit"] = value["snapshot_retention_limit"]
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "snapshot_window" in value:
        out["SnapshotWindow"] = value["snapshot_window"]
    if "acl_name" in value:
        out["ACLName"] = value["acl_name"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "data_tiering" in value:
        import capo_memorydb.types.data_tiering_status

        out["DataTiering"] = (
            capo_memorydb.types.data_tiering_status.serialize_aws_json_1_1(
                value["data_tiering"]
            )
        )
    if "network_type" in value:
        import capo_memorydb.types.network_type

        out["NetworkType"] = capo_memorydb.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    if "ip_discovery" in value:
        import capo_memorydb.types.ip_discovery

        out["IpDiscovery"] = capo_memorydb.types.ip_discovery.serialize_aws_json_1_1(
            value["ip_discovery"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("PendingUpdates") is not None:
        import capo_memorydb.types.cluster_pending_updates

        out["pending_updates"] = (
            capo_memorydb.types.cluster_pending_updates.deserialize_aws_json_1_1(
                data["PendingUpdates"]
            )
        )
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if data.get("NumberOfShards") is not None:
        out["number_of_shards"] = data["NumberOfShards"]
    if data.get("Shards") is not None:
        import capo_memorydb.types.shard_list

        out["shards"] = capo_memorydb.types.shard_list.deserialize_aws_json_1_1(
            data["Shards"]
        )
    if data.get("AvailabilityMode") is not None:
        import capo_memorydb.types.az_status

        out["availability_mode"] = (
            capo_memorydb.types.az_status.deserialize_aws_json_1_1(
                data["AvailabilityMode"]
            )
        )
    if data.get("ClusterEndpoint") is not None:
        import capo_memorydb.types.endpoint

        out["cluster_endpoint"] = capo_memorydb.types.endpoint.deserialize_aws_json_1_1(
            data["ClusterEndpoint"]
        )
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("EnginePatchVersion") is not None:
        out["engine_patch_version"] = data["EnginePatchVersion"]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if data.get("ParameterGroupStatus") is not None:
        out["parameter_group_status"] = data["ParameterGroupStatus"]
    if data.get("SecurityGroups") is not None:
        import capo_memorydb.types.security_group_membership_list

        out["security_groups"] = (
            capo_memorydb.types.security_group_membership_list.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if data.get("TLSEnabled") is not None:
        out["tls_enabled"] = data["TLSEnabled"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("SnsTopicStatus") is not None:
        out["sns_topic_status"] = data["SnsTopicStatus"]
    if data.get("SnapshotRetentionLimit") is not None:
        out["snapshot_retention_limit"] = data["SnapshotRetentionLimit"]
    if data.get("MaintenanceWindow") is not None:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if data.get("SnapshotWindow") is not None:
        out["snapshot_window"] = data["SnapshotWindow"]
    if data.get("ACLName") is not None:
        out["acl_name"] = data["ACLName"]
    if data.get("AutoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if data.get("DataTiering") is not None:
        import capo_memorydb.types.data_tiering_status

        out["data_tiering"] = (
            capo_memorydb.types.data_tiering_status.deserialize_aws_json_1_1(
                data["DataTiering"]
            )
        )
    if data.get("NetworkType") is not None:
        import capo_memorydb.types.network_type

        out["network_type"] = capo_memorydb.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    if data.get("IpDiscovery") is not None:
        import capo_memorydb.types.ip_discovery

        out["ip_discovery"] = capo_memorydb.types.ip_discovery.deserialize_aws_json_1_1(
            data["IpDiscovery"]
        )
    return out

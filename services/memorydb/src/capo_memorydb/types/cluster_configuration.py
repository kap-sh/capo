"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.shard_details
    import capo_memorydb.types.string


class ClusterConfiguration(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the cluster</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>The description of the cluster configuration</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The node type used for the cluster</p>"""
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine used by the cluster configuration.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Redis OSS engine version used by the cluster</p>"""
    maintenance_window: NotRequired["capo_memorydb.types.string.String"]
    """<p>The specified maintenance window for the cluster</p>"""
    topic_arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the SNS notification topic for the cluster</p>"""
    port: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The port used by the cluster</p>"""
    parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of parameter group used by the cluster</p>"""
    subnet_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the subnet group used by the cluster</p>"""
    vpc_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The ID of the VPC the cluster belongs to</p>"""
    snapshot_retention_limit: NotRequired[
        "capo_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The snapshot retention limit set by the cluster</p>"""
    snapshot_window: NotRequired["capo_memorydb.types.string.String"]
    """<p>The snapshot window set by the cluster</p>"""
    num_shards: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of shards in the cluster</p>"""
    shards: NotRequired["capo_memorydb.types.shard_details.ShardDetails"]
    """<p>The list of shards in the cluster</p>"""
    multi_region_parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-Region parameter group associated with the cluster configuration.</p>"""
    multi_region_cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name for the multi-Region cluster associated with the cluster configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "port" in value:
        out["Port"] = value["port"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "snapshot_retention_limit" in value:
        out["SnapshotRetentionLimit"] = value["snapshot_retention_limit"]
    if "snapshot_window" in value:
        out["SnapshotWindow"] = value["snapshot_window"]
    if "num_shards" in value:
        out["NumShards"] = value["num_shards"]
    if "shards" in value:
        import capo_memorydb.types.shard_details

        out["Shards"] = capo_memorydb.types.shard_details.serialize_aws_json_1_1(
            value["shards"]
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterConfiguration:
    out: ClusterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("MaintenanceWindow") is not None:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SnapshotRetentionLimit") is not None:
        out["snapshot_retention_limit"] = data["SnapshotRetentionLimit"]
    if data.get("SnapshotWindow") is not None:
        out["snapshot_window"] = data["SnapshotWindow"]
    if data.get("NumShards") is not None:
        out["num_shards"] = data["NumShards"]
    if data.get("Shards") is not None:
        import capo_memorydb.types.shard_details

        out["shards"] = capo_memorydb.types.shard_details.deserialize_aws_json_1_1(
            data["Shards"]
        )
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusterConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "port" in value:
        out["Port"] = value["port"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "snapshot_retention_limit" in value:
        out["SnapshotRetentionLimit"] = value["snapshot_retention_limit"]
    if "snapshot_window" in value:
        out["SnapshotWindow"] = value["snapshot_window"]
    if "num_shards" in value:
        out["NumShards"] = value["num_shards"]
    if "shards" in value:
        import capo_memorydb.types.shard_details

        out["Shards"] = capo_memorydb.types.shard_details.serialize_cbor(
            value["shards"]
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    return out


def deserialize_cbor(data: dict) -> ClusterConfiguration:
    out: ClusterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("MaintenanceWindow") is not None:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SnapshotRetentionLimit") is not None:
        out["snapshot_retention_limit"] = data["SnapshotRetentionLimit"]
    if data.get("SnapshotWindow") is not None:
        out["snapshot_window"] = data["SnapshotWindow"]
    if data.get("NumShards") is not None:
        out["num_shards"] = data["NumShards"]
    if data.get("Shards") is not None:
        import capo_memorydb.types.shard_details

        out["shards"] = capo_memorydb.types.shard_details.deserialize_cbor(
            data["Shards"]
        )
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    return out

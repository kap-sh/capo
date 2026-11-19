"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.regional_cluster_list
    import capo_memorydb.types.string


class MultiRegionCluster(TypedDict, closed=True):
    multi_region_cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-Region cluster.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>The description of the multi-Region cluster.</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The current status of the multi-Region cluster.</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The node type used by the multi-Region cluster.</p>"""
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine used by the multi-Region cluster.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The version of the engine used by the multi-Region cluster.</p>"""
    number_of_shards: NotRequired[
        "capo_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of shards in the multi-Region cluster.</p>"""
    clusters: NotRequired[
        "capo_memorydb.types.regional_cluster_list.RegionalClusterList"
    ]
    """<p>The clusters in this multi-Region cluster.</p>"""
    multi_region_parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-Region parameter group associated with the cluster.</p>"""
    tls_enabled: NotRequired["capo_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>Indiciates if the multi-Region cluster is TLS enabled.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionCluster) -> dict:
    out: dict = {}
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        out["Status"] = value["status"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "number_of_shards" in value:
        out["NumberOfShards"] = value["number_of_shards"]
    if "clusters" in value:
        import capo_memorydb.types.regional_cluster_list

        out["Clusters"] = (
            capo_memorydb.types.regional_cluster_list.serialize_aws_json_1_1(
                value["clusters"]
            )
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionCluster:
    out: MultiRegionCluster = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("NumberOfShards") is not None:
        out["number_of_shards"] = data["NumberOfShards"]
    if data.get("Clusters") is not None:
        import capo_memorydb.types.regional_cluster_list

        out["clusters"] = (
            capo_memorydb.types.regional_cluster_list.deserialize_aws_json_1_1(
                data["Clusters"]
            )
        )
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("TLSEnabled") is not None:
        out["tls_enabled"] = data["TLSEnabled"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MultiRegionCluster) -> dict:
    out: dict = {}
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        out["Status"] = value["status"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "number_of_shards" in value:
        out["NumberOfShards"] = value["number_of_shards"]
    if "clusters" in value:
        import capo_memorydb.types.regional_cluster_list

        out["Clusters"] = capo_memorydb.types.regional_cluster_list.serialize_cbor(
            value["clusters"]
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> MultiRegionCluster:
    out: MultiRegionCluster = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("NumberOfShards") is not None:
        out["number_of_shards"] = data["NumberOfShards"]
    if data.get("Clusters") is not None:
        import capo_memorydb.types.regional_cluster_list

        out["clusters"] = capo_memorydb.types.regional_cluster_list.deserialize_cbor(
            data["Clusters"]
        )
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("TLSEnabled") is not None:
        out["tls_enabled"] = data["TLSEnabled"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out

"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateMultiRegionClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string
    import capo_memorydb.types.tag_list


class CreateMultiRegionClusterRequest(TypedDict, closed=True):
    multi_region_cluster_name_suffix: "capo_memorydb.types.string.String"
    """<p>A suffix to be added to the Multi-Region cluster name. Amazon MemoryDB automatically applies a prefix to the Multi-Region cluster Name when it is created. Each Amazon Region has its own prefix. For instance, a Multi-Region cluster Name created in the US-West-1 region will begin with "virxk", along with the suffix name you provide. The suffix guarantees uniqueness of the Multi-Region cluster name across multiple regions.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description for the multi-Region cluster.</p>"""
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine to be used for the multi-Region cluster.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The version of the engine to be used for the multi-Region cluster.</p>"""
    node_type: "capo_memorydb.types.string.String"
    """<p>The node type to be used for the multi-Region cluster.</p>"""
    multi_region_parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-Region parameter group to be associated with the cluster.</p>"""
    num_shards: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of shards for the multi-Region cluster.</p>"""
    tls_enabled: NotRequired["capo_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>Whether to enable TLS encryption for the multi-Region cluster.</p>"""
    tags: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be applied to the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMultiRegionClusterRequest) -> dict:
    out: dict = {}
    out["MultiRegionClusterNameSuffix"] = value["multi_region_cluster_name_suffix"]
    if "description" in value:
        out["Description"] = value["description"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    out["NodeType"] = value["node_type"]
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "num_shards" in value:
        out["NumShards"] = value["num_shards"]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "tags" in value:
        import capo_memorydb.types.tag_list

        out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMultiRegionClusterRequest:
    out: CreateMultiRegionClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionClusterNameSuffix") is not None:
        out["multi_region_cluster_name_suffix"] = data["MultiRegionClusterNameSuffix"]
    else:
        raise DeserializationError(
            "CreateMultiRegionClusterRequest.multi_region_cluster_name_suffix required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    else:
        raise DeserializationError("CreateMultiRegionClusterRequest.node_type required")
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("NumShards") is not None:
        out["num_shards"] = data["NumShards"]
    if data.get("TLSEnabled") is not None:
        out["tls_enabled"] = data["TLSEnabled"]
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

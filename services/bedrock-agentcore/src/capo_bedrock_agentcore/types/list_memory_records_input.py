"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_metadata_filter_list
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.namespace
    import capo_bedrock_agentcore.types.pagination_token


class ListMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource for which to list memory records.</p>"""
    namespace: NotRequired["capo_bedrock_agentcore.types.namespace.Namespace"]
    """<p>The exact namespace to filter memory records by. Returns all memory records that matches the provided namespace. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>"""
    namespace_path: NotRequired["capo_bedrock_agentcore.types.namespace.Namespace"]
    """<p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>"""
    memory_strategy_id: NotRequired[
        "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.</p>"""
    max_results: NotRequired["capo_bedrock_agentcore.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    metadata_filters: NotRequired[
        "capo_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
    ]
    """<p>A list of metadata filter expressions to scope the returned memory records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryRecordsInput) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "namespace_path" in value:
        out["namespacePath"] = value["namespace_path"]
    if "memory_strategy_id" in value:
        out["memoryStrategyId"] = value["memory_strategy_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "metadata_filters" in value:
        import capo_bedrock_agentcore.types.memory_metadata_filter_list

        out["metadataFilters"] = (
            capo_bedrock_agentcore.types.memory_metadata_filter_list.serialize_json(
                value["metadata_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMemoryRecordsInput:
    out: ListMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("namespacePath") is not None:
        out["namespace_path"] = data["namespacePath"]
    if data.get("memoryStrategyId") is not None:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("metadataFilters") is not None:
        import capo_bedrock_agentcore.types.memory_metadata_filter_list

        out["metadata_filters"] = (
            capo_bedrock_agentcore.types.memory_metadata_filter_list.deserialize_json(
                data["metadataFilters"]
            )
        )
    return out

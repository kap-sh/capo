"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SearchCriteria``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_metadata_filter_list
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.sensitive_string


class SearchCriteria(TypedDict, closed=True):
    search_query: "capo_bedrock_agentcore.types.sensitive_string.SensitiveString"
    """<p>The search query to use for finding relevant memory records.</p>"""
    memory_strategy_id: NotRequired[
        "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The memory strategy identifier to filter memory records by.</p>"""
    top_k: "int"
    """<p>The maximum number of top-scoring memory records to return. This value is used for semantic search ranking.</p>"""
    metadata_filters: NotRequired[
        "capo_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
    ]
    """<p>Filters to apply to metadata associated with a memory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCriteria) -> dict:
    out: dict = {}
    out["searchQuery"] = value["search_query"]
    if "memory_strategy_id" in value:
        out["memoryStrategyId"] = value["memory_strategy_id"]
    out["topK"] = value.get("top_k", 10)
    if "metadata_filters" in value:
        import capo_bedrock_agentcore.types.memory_metadata_filter_list

        out["metadataFilters"] = (
            capo_bedrock_agentcore.types.memory_metadata_filter_list.serialize_json(
                value["metadata_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchCriteria:
    out: SearchCriteria = {}  # type: ignore[typeddict-item]
    if data.get("searchQuery") is not None:
        out["search_query"] = data["searchQuery"]
    else:
        out["search_query"] = ""
    if data.get("memoryStrategyId") is not None:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    if data.get("topK") is not None:
        out["top_k"] = data["topK"]
    else:
        out["top_k"] = 10
    if data.get("metadataFilters") is not None:
        import capo_bedrock_agentcore.types.memory_metadata_filter_list

        out["metadata_filters"] = (
            capo_bedrock_agentcore.types.memory_metadata_filter_list.deserialize_json(
                data["metadataFilters"]
            )
        )
    return out


def redact_sensitive(value: SearchCriteria) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "search_query" in value:
        out["search_query"] = "*** Sensitive Data Redacted ***"
    return out

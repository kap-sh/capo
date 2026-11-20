"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemorySearchSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.memory_type
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.sensitive_content
    import capo_opensearchmemory.types.source_event_id_list
    import capo_opensearchmemory.types.strategy_name
    import capo_opensearchmemory.types.system_metadata


class MemorySearchSummary(TypedDict, closed=True):
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The memory's ID, assigned by the service. Always present.</p>"""
    memory_type: NotRequired["capo_opensearchmemory.types.memory_type.MemoryType"]
    """<p>The memory type of the result.</p>"""
    strategy_name: NotRequired["capo_opensearchmemory.types.strategy_name.StrategyName"]
    """<p>The name of the strategy the memory belongs to, for example <code>user-facts</code>: the strategy <code>memoryStrategies</code> selects on in <code>SearchMemories</code>. Absent when the memory's strategy is no longer declared on the space, for example right after the strategy is deleted.</p>"""
    content: NotRequired[
        "capo_opensearchmemory.types.sensitive_content.SensitiveContent"
    ]
    """<p>The memory text.</p>"""
    score: NotRequired["float"]
    """<p>The relevance score of the result. A higher score is more relevant. Scores aren't normalized to a fixed range and can be greater than 1, so use them only to order results.</p>"""
    system_metadata: NotRequired[
        "capo_opensearchmemory.types.system_metadata.SystemMetadata"
    ]
    """<p>Provenance for the memory: the actor and session that own it, and when it was created and last updated. It is the same block that <code>ListMemories</code>, <code>GetMemory</code>, and <code>SearchEvents</code> return.</p> <p>In a query, filter or sort on the timestamps as <code>system_metadata.created_at</code> and <code>system_metadata.updated_at</code>. Scope by owner with the top-level <code>actorId</code>, not in the query. Searching memories doesn't filter by session.</p> <p>Absent when the service has no provenance for the memory.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The memory's metadata tags. All values are strings. In a query, filter on a tag as <code>metadata.&lt;key&gt;</code>.</p>"""
    source_event_ids: NotRequired[
        "capo_opensearchmemory.types.source_event_id_list.SourceEventIdList"
    ]
    """<p>The IDs of the events the memory was derived from, without duplicates. Use them with <code>GetEvent</code> or <code>BatchGetEvent</code>, or to search those events' content with <code>SearchEvents</code> by filtering on <code>event_ids</code> in the query. Absent for a memory created directly with <code>CreateMemory</code>. A memory can be derived from several events. The service sets this value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemorySearchSummary) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    if "memory_type" in value:
        import capo_opensearchmemory.types.memory_type

        out["memoryType"] = (
            capo_opensearchmemory.types.memory_type.serialize_aws_json_1_0(
                value["memory_type"]
            )
        )
    if "strategy_name" in value:
        out["strategyName"] = value["strategy_name"]
    if "content" in value:
        out["content"] = value["content"]
    if "score" in value:
        out["score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "system_metadata" in value:
        import capo_opensearchmemory.types.system_metadata

        out["systemMetadata"] = (
            capo_opensearchmemory.types.system_metadata.serialize_aws_json_1_0(
                value["system_metadata"]
            )
        )
    if "metadata" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    if "source_event_ids" in value:
        import capo_opensearchmemory.types.source_event_id_list

        out["sourceEventIds"] = (
            capo_opensearchmemory.types.source_event_id_list.serialize_aws_json_1_0(
                value["source_event_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MemorySearchSummary:
    out: MemorySearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    if data.get("memoryType") is not None:
        import capo_opensearchmemory.types.memory_type

        out["memory_type"] = (
            capo_opensearchmemory.types.memory_type.deserialize_aws_json_1_0(
                data["memoryType"]
            )
        )
    if data.get("strategyName") is not None:
        out["strategy_name"] = data["strategyName"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    if data.get("systemMetadata") is not None:
        import capo_opensearchmemory.types.system_metadata

        out["system_metadata"] = (
            capo_opensearchmemory.types.system_metadata.deserialize_aws_json_1_0(
                data["systemMetadata"]
            )
        )
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    if data.get("sourceEventIds") is not None:
        import capo_opensearchmemory.types.source_event_id_list

        out["source_event_ids"] = (
            capo_opensearchmemory.types.source_event_id_list.deserialize_aws_json_1_0(
                data["sourceEventIds"]
            )
        )
    return out


def redact_sensitive(value: MemorySearchSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out

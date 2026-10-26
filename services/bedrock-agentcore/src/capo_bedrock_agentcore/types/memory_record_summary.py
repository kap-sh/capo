"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.memory_content
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.memory_record_metadata_map
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.namespaces_list


class MemoryRecordSummary(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique identifier of the memory record.</p>"""
    content: "capo_bedrock_agentcore.types.memory_content.MemoryContent"
    """<p>The content of the memory record.</p>"""
    memory_strategy_id: (
        "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    )
    """<p>The identifier of the memory strategy associated with this record.</p>"""
    namespaces: "capo_bedrock_agentcore.types.namespaces_list.NamespacesList"
    """<p>The namespaces associated with this memory record.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the memory record was created.</p>"""
    score: NotRequired["float"]
    """<p>The relevance score of the memory record when returned as part of a search result. Higher values indicate greater relevance to the search query.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp based on which the memory record was ingested. This reflects the time of the source content that the record was derived from, which can differ from <code>createdAt</code>, the time the record itself was written.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agentcore.types.memory_record_metadata_map.MemoryRecordMetadataMap"
    ]
    """<p>A map of metadata key-value pairs associated with a memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordSummary) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    import capo_bedrock_agentcore.types.memory_content

    out["content"] = capo_bedrock_agentcore.types.memory_content.serialize_json(
        value["content"]
    )
    out["memoryStrategyId"] = value["memory_strategy_id"]
    import capo_bedrock_agentcore.types.namespaces_list

    out["namespaces"] = capo_bedrock_agentcore.types.namespaces_list.serialize_json(
        value["namespaces"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
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
    if "timestamp" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["timestamp"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            capo_bedrock_agentcore.types.memory_record_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordSummary:
    out: MemoryRecordSummary = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordId") is not None:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        out["memory_record_id"] = ""
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("memoryStrategyId") is not None:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    else:
        out["memory_strategy_id"] = ""
    if data.get("namespaces") is not None:
        import capo_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = (
            capo_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        out["namespaces"] = []
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    if data.get("timestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            capo_bedrock_agentcore.types.memory_record_metadata_map.deserialize_json(
                data["metadata"]
            )
        )
    return out


def redact_sensitive(value: MemoryRecordSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.redact_sensitive(
            value["content"]
        )
    return out

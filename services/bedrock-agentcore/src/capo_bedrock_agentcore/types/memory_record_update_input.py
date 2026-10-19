"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordUpdateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.memory_content
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.memory_record_metadata_map
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.namespaces_list


class MemoryRecordUpdateInput(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique ID of the memory record to be updated.</p>"""
    timestamp: "datetime.datetime"
    """<p>Time at which the memory record was updated</p>"""
    content: NotRequired["capo_bedrock_agentcore.types.memory_content.MemoryContent"]
    """<p>The content to be stored within the memory record.</p>"""
    namespaces: NotRequired[
        "capo_bedrock_agentcore.types.namespaces_list.NamespacesList"
    ]
    """<p>The updated list of namespace identifiers for categorizing the memory record.</p>"""
    source_namespaces: NotRequired[
        "capo_bedrock_agentcore.types.namespaces_list.NamespacesList"
    ]
    """<p>The namespaces of the source memory record being updated. This value is used for IAM condition key authorization.</p>"""
    memory_strategy_id: NotRequired[
        "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The updated ID of the memory strategy that defines how this memory record is grouped.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agentcore.types.memory_record_metadata_map.MemoryRecordMetadataMap"
    ]
    """<p>Metadata key-value pairs to be stored with the memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordUpdateInput) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["timestamp"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "content" in value:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.serialize_json(
            value["content"]
        )
    if "namespaces" in value:
        import capo_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = capo_bedrock_agentcore.types.namespaces_list.serialize_json(
            value["namespaces"]
        )
    if "source_namespaces" in value:
        import capo_bedrock_agentcore.types.namespaces_list

        out["sourceNamespaces"] = (
            capo_bedrock_agentcore.types.namespaces_list.serialize_json(
                value["source_namespaces"]
            )
        )
    if "memory_strategy_id" in value:
        out["memoryStrategyId"] = value["memory_strategy_id"]
    if "metadata" in value:
        import capo_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            capo_bedrock_agentcore.types.memory_record_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordUpdateInput:
    out: MemoryRecordUpdateInput = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordId") is not None:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        out["memory_record_id"] = ""
    if data.get("timestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.deserialize_json(
            data["content"]
        )
    if data.get("namespaces") is not None:
        import capo_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = (
            capo_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["namespaces"]
            )
        )
    if data.get("sourceNamespaces") is not None:
        import capo_bedrock_agentcore.types.namespaces_list

        out["source_namespaces"] = (
            capo_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["sourceNamespaces"]
            )
        )
    if data.get("memoryStrategyId") is not None:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    if data.get("metadata") is not None:
        import capo_bedrock_agentcore.types.memory_record_metadata_map

        out["metadata"] = (
            capo_bedrock_agentcore.types.memory_record_metadata_map.deserialize_json(
                data["metadata"]
            )
        )
    return out


def redact_sensitive(value: MemoryRecordUpdateInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.redact_sensitive(
            value["content"]
        )
    return out

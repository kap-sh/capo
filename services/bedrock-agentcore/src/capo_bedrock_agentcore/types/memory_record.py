"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecord``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.memory_content
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.memory_record_metadata_map
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.namespaces_list


class MemoryRecord(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique identifier of the memory record.</p>"""
    content: "capo_bedrock_agentcore.types.memory_content.MemoryContent"
    """<p>The content of the memory record.</p>"""
    memory_strategy_id: (
        "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    )
    """<p>The identifier of the memory strategy associated with this record.</p>"""
    namespaces: "capo_bedrock_agentcore.types.namespaces_list.NamespacesList"
    """<p>The namespaces associated with this memory record. Namespaces help organize and categorize memory records.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the memory record was created.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp based on which the memory record was ingested. This reflects the time of the source content that the record was derived from, which can differ from <code>createdAt</code>, the time the record itself was written.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agentcore.types.memory_record_metadata_map.MemoryRecordMetadataMap"
    ]
    """<p>A map of metadata key-value pairs associated with a memory record.</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the memory record expires and becomes eligible for deletion. This value is set when a record expiry (long-term memory time-to-live) applies to the record, either from the strategy the record belongs to or from a record expiry provided on the batch request that created or updated it. If the record has no expiry configured, this value is not present and the record does not expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecord) -> dict:
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
    if "expires_at" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["expiresAt"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["expires_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecord:
    out: MemoryRecord = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordId") is not None:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        raise DeserializationError("MemoryRecord.memory_record_id required")
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("MemoryRecord.content required")
    if data.get("memoryStrategyId") is not None:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    else:
        raise DeserializationError("MemoryRecord.memory_strategy_id required")
    if data.get("namespaces") is not None:
        import capo_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = (
            capo_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("MemoryRecord.namespaces required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("MemoryRecord.created_at required")
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
    if data.get("expiresAt") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["expires_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["expiresAt"]
            )
        )
    return out


def redact_sensitive(value: MemoryRecord) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.redact_sensitive(
            value["content"]
        )
    return out

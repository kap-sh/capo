"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordCreateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.memory_content
    import capo_bedrock_agentcore.types.memory_record_metadata_map
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.namespaces_list
    import capo_bedrock_agentcore.types.request_identifier


class MemoryRecordCreateInput(TypedDict, closed=True):
    request_identifier: (
        "capo_bedrock_agentcore.types.request_identifier.RequestIdentifier"
    )
    """<p>A client-provided identifier for tracking this specific record creation request.</p>"""
    namespaces: "capo_bedrock_agentcore.types.namespaces_list.NamespacesList"
    """<p>A list of namespace identifiers that categorize or group the memory record.</p>"""
    content: "capo_bedrock_agentcore.types.memory_content.MemoryContent"
    """<p>The content to be stored within the memory record.</p>"""
    timestamp: "datetime.datetime"
    """<p>Time at which the memory record was created.</p>"""
    memory_strategy_id: NotRequired[
        "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The ID of the memory strategy that defines how this memory record is grouped.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agentcore.types.memory_record_metadata_map.MemoryRecordMetadataMap"
    ]
    """<p>Metadata key-value pairs to be stored with the memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordCreateInput) -> dict:
    out: dict = {}
    out["requestIdentifier"] = value["request_identifier"]
    import capo_bedrock_agentcore.types.namespaces_list

    out["namespaces"] = capo_bedrock_agentcore.types.namespaces_list.serialize_json(
        value["namespaces"]
    )
    import capo_bedrock_agentcore.types.memory_content

    out["content"] = capo_bedrock_agentcore.types.memory_content.serialize_json(
        value["content"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["timestamp"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["timestamp"]
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


def deserialize_json(data: dict) -> MemoryRecordCreateInput:
    out: MemoryRecordCreateInput = {}  # type: ignore[typeddict-item]
    if data.get("requestIdentifier") is not None:
        out["request_identifier"] = data["requestIdentifier"]
    else:
        raise DeserializationError(
            "MemoryRecordCreateInput.request_identifier required"
        )
    if data.get("namespaces") is not None:
        import capo_bedrock_agentcore.types.namespaces_list

        out["namespaces"] = (
            capo_bedrock_agentcore.types.namespaces_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordCreateInput.namespaces required")
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("MemoryRecordCreateInput.content required")
    if data.get("timestamp") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["timestamp"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordCreateInput.timestamp required")
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


def redact_sensitive(value: MemoryRecordCreateInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.memory_content

        out["content"] = capo_bedrock_agentcore.types.memory_content.redact_sensitive(
            value["content"]
        )
    return out

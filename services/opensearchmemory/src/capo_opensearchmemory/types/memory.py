"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#Memory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.memory_type
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.sensitive_content
    import capo_opensearchmemory.types.strategy_name
    import capo_opensearchmemory.types.system_metadata


class Memory(TypedDict, closed=True):
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The memory's ID, assigned by the service.</p>"""
    memory_type: "capo_opensearchmemory.types.memory_type.MemoryType"
    """<p>The memory type.</p>"""
    strategy_name: NotRequired["capo_opensearchmemory.types.strategy_name.StrategyName"]
    """<p>The name of the strategy the memory belongs to, for example <code>user-facts</code>. A space can hold several strategies of the same type, so this tells them apart. Absent when the memory's strategy is no longer declared on the space, for example right after the strategy is deleted.</p>"""
    content: "capo_opensearchmemory.types.sensitive_content.SensitiveContent"
    """<p>The memory text.</p>"""
    system_metadata: "capo_opensearchmemory.types.system_metadata.SystemMetadata"
    """<p>Provenance for the memory: the owning actor and session, and when it was created and last updated. Always present. <code>updatedAt</code> equals <code>createdAt</code> for a memory that has never been updated.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The memory's metadata tags. All values are strings. May be empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Memory) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    import capo_opensearchmemory.types.memory_type

    out["memoryType"] = capo_opensearchmemory.types.memory_type.serialize_aws_json_1_0(
        value["memory_type"]
    )
    if "strategy_name" in value:
        out["strategyName"] = value["strategy_name"]
    out["content"] = value["content"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> Memory:
    out: Memory = {}  # type: ignore[typeddict-item]
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
    else:
        import typing

        out["memory_type"] = typing.cast(
            "capo_opensearchmemory.types.memory_type.MemoryType", ""
        )
    if data.get("strategyName") is not None:
        out["strategy_name"] = data["strategyName"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("systemMetadata") is not None:
        import capo_opensearchmemory.types.system_metadata

        out["system_metadata"] = (
            capo_opensearchmemory.types.system_metadata.deserialize_aws_json_1_0(
                data["systemMetadata"]
            )
        )
    else:
        raise DeserializationError("Memory.system_metadata required")
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    return out


def redact_sensitive(value: Memory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryListSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.memory_type
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.strategy_name
    import capo_opensearchmemory.types.system_metadata


class MemoryListSummary(TypedDict, closed=True):
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The memory's ID, assigned by the service. IDs are opaque, can contain hyphens and underscores, and can be up to 512 characters long.</p>"""
    memory_type: "capo_opensearchmemory.types.memory_type.MemoryType"
    """<p>The memory type.</p>"""
    strategy_name: NotRequired["capo_opensearchmemory.types.strategy_name.StrategyName"]
    """<p>The name of the strategy the memory belongs to, for example <code>user-facts</code>: the strategy <code>memoryStrategies</code> selects on in <code>ListMemories</code>. Absent when the memory's strategy is no longer declared on the space, for example right after the strategy is deleted.</p>"""
    system_metadata: "capo_opensearchmemory.types.system_metadata.SystemMetadata"
    """<p>Provenance for the memory: the owning actor and session, and when it was created and last updated. Always present, with both timestamps.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The memory's metadata tags. All values are strings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryListSummary) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    import capo_opensearchmemory.types.memory_type

    out["memoryType"] = capo_opensearchmemory.types.memory_type.serialize_aws_json_1_0(
        value["memory_type"]
    )
    if "strategy_name" in value:
        out["strategyName"] = value["strategy_name"]
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


def deserialize_aws_json_1_0(data: dict) -> MemoryListSummary:
    out: MemoryListSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("systemMetadata") is not None:
        import capo_opensearchmemory.types.system_metadata

        out["system_metadata"] = (
            capo_opensearchmemory.types.system_metadata.deserialize_aws_json_1_0(
                data["systemMetadata"]
            )
        )
    else:
        raise DeserializationError("MemoryListSummary.system_metadata required")
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    return out

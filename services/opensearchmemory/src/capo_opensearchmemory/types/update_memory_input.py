"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UpdateMemoryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.memory_update_content
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.metadata_mode
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.strategy_name


class UpdateMemoryInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space that owns the memory, for example <code>sp-02864597b164</code>.</p>"""
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The ID of the memory to update.</p>"""
    content: NotRequired[
        "capo_opensearchmemory.types.memory_update_content.MemoryUpdateContent"
    ]
    """<p>Replacement memory text. Supplying it re-embeds the memory. Omit to leave the text unchanged.</p>"""
    metadata: NotRequired["capo_opensearchmemory.types.metadata_map.MetadataMap"]
    """<p>The metadata tags to apply. By default this map replaces the stored metadata, and any key not present is removed. Set <code>metadataMode</code> to <code>MERGE</code> to keep the keys you don't supply. Limits apply to the resulting metadata, not to the request. Keys that begin with <code>x-amz-</code> and the key <code>documentS3Source</code> are reserved: a request that sets one fails with <code>ValidationException</code>.</p> <p>A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with <code>ValidationException</code>. Reuse an existing key instead.</p>"""
    metadata_mode: NotRequired["capo_opensearchmemory.types.metadata_mode.MetadataMode"]
    """<p>How <code>metadata</code> combines with what is stored. The default is <code>REPLACE</code>.</p>"""
    actor_id: NotRequired["capo_opensearchmemory.types.actor_id.ActorId"]
    """<p>The ID of the actor that the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>"""
    strategy_name: NotRequired["capo_opensearchmemory.types.strategy_name.StrategyName"]
    """<p>The name of the strategy that the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateMemoryInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["memoryId"] = value["memory_id"]
    if "content" in value:
        out["content"] = value["content"]
    if "metadata" in value:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    if "metadata_mode" in value:
        import capo_opensearchmemory.types.metadata_mode

        out["metadataMode"] = (
            capo_opensearchmemory.types.metadata_mode.serialize_aws_json_1_0(
                value["metadata_mode"]
            )
        )
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "strategy_name" in value:
        out["strategyName"] = value["strategy_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateMemoryInput:
    out: UpdateMemoryInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("metadata") is not None:
        import capo_opensearchmemory.types.metadata_map

        out["metadata"] = (
            capo_opensearchmemory.types.metadata_map.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    if data.get("metadataMode") is not None:
        import capo_opensearchmemory.types.metadata_mode

        out["metadata_mode"] = (
            capo_opensearchmemory.types.metadata_mode.deserialize_aws_json_1_0(
                data["metadataMode"]
            )
        )
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    if data.get("strategyName") is not None:
        out["strategy_name"] = data["strategyName"]
    return out


def redact_sensitive(value: UpdateMemoryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out

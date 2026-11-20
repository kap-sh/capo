"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#GetMemoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.strategy_name


class GetMemoryInput(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space that holds the memory.</p>"""
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The memory's ID, as returned by <code>SearchMemories</code> or <code>ListMemories</code>.</p>"""
    actor_id: NotRequired["capo_opensearchmemory.types.actor_id.ActorId"]
    """<p>The ID of the actor the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>"""
    strategy_name: NotRequired["capo_opensearchmemory.types.strategy_name.StrategyName"]
    """<p>The name of the strategy the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMemoryInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["memoryId"] = value["memory_id"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "strategy_name" in value:
        out["strategyName"] = value["strategy_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMemoryInput:
    out: GetMemoryInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    if data.get("strategyName") is not None:
        out["strategy_name"] = data["strategyName"]
    return out

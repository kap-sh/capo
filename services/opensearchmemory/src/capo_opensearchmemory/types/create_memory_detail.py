"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateMemoryDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.strategy_name


class CreateMemoryDetail(TypedDict, closed=True):
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The final ID of the memory. Until the memory is indexed, <code>GetMemory</code>, <code>UpdateMemory</code>, and <code>DeleteMemory</code> return <code>ResourceNotFoundException</code> for it.</p>"""
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    name: "capo_opensearchmemory.types.strategy_name.StrategyName"
    """<p>The name of the strategy the memory belongs to.</p>"""
    actor_id: "capo_opensearchmemory.types.actor_id.ActorId"
    """<p>The ID of the actor the memory belongs to.</p>"""
    session_id: "capo_opensearchmemory.types.session_id.SessionId"
    """<p>The ID of the session the memory belongs to, including one the service generated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateMemoryDetail) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    out["spaceId"] = value["space_id"]
    out["name"] = value["name"]
    out["actorId"] = value["actor_id"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateMemoryDetail:
    out: CreateMemoryDetail = {}  # type: ignore[typeddict-item]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteMemoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.memory_status


class DeleteMemoryOutput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the deleted AgentCore Memory resource.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore_control.types.memory_status.MemoryStatus"
    ]
    """<p>The current status of the AgentCore Memory resource deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryOutput) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    if "status" in value:
        import capo_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.memory_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteMemoryOutput:
    out: DeleteMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.memory_status.deserialize_json(
                data["status"]
            )
        )
    return out

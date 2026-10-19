"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetMemoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.memory_view


class GetMemoryInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory to retrieve.</p>"""
    view: NotRequired["capo_bedrock_agentcore_control.types.memory_view.MemoryView"]
    """<p>The level of detail to return for the memory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMemoryInput:
    out: GetMemoryInput = {}  # type: ignore[typeddict-item]
    return out

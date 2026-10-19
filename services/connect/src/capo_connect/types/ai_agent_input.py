"""Generated from Smithy shape ``com.amazonaws.connect#AiAgentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.ai_agent_id


class AiAgentInput(TypedDict, closed=True):
    ai_agent_id: "capo_connect.types.ai_agent_id.AiAgentId"
    """<p>The identifier of the AI agent that participates in the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AiAgentInput) -> dict:
    out: dict = {}
    out["AiAgentId"] = value["ai_agent_id"]
    return out


def deserialize_json(data: dict) -> AiAgentInput:
    out: AiAgentInput = {}  # type: ignore[typeddict-item]
    if data.get("AiAgentId") is not None:
        out["ai_agent_id"] = data["AiAgentId"]
    else:
        out["ai_agent_id"] = ""
    return out

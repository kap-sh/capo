"""Generated from Smithy shape ``com.amazonaws.qconnect#SuggestedMessageReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.uuid


class SuggestedMessageReference(TypedDict, closed=True):
    ai_agent_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the AI Agent that generated the suggested message.</p>"""
    ai_agent_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI Agent that generated the suggested message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedMessageReference) -> dict:
    out: dict = {}
    out["aiAgentId"] = value["ai_agent_id"]
    out["aiAgentArn"] = value["ai_agent_arn"]
    return out


def deserialize_json(data: dict) -> SuggestedMessageReference:
    out: SuggestedMessageReference = {}  # type: ignore[typeddict-item]
    if data.get("aiAgentId") is not None:
        out["ai_agent_id"] = data["aiAgentId"]
    else:
        out["ai_agent_id"] = ""
    if data.get("aiAgentArn") is not None:
        out["ai_agent_arn"] = data["aiAgentArn"]
    else:
        out["ai_agent_arn"] = ""
    return out

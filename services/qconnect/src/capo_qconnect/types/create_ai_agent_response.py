"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_data


class CreateAIAgentResponse(TypedDict, closed=True):
    ai_agent: NotRequired["capo_qconnect.types.ai_agent_data.AIAgentData"]
    """<p>The data of the created AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIAgentResponse) -> dict:
    out: dict = {}
    if "ai_agent" in value:
        import capo_qconnect.types.ai_agent_data

        out["aiAgent"] = capo_qconnect.types.ai_agent_data.serialize_json(
            value["ai_agent"]
        )
    return out


def deserialize_json(data: dict) -> CreateAIAgentResponse:
    out: CreateAIAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiAgent") is not None:
        import capo_qconnect.types.ai_agent_data

        out["ai_agent"] = capo_qconnect.types.ai_agent_data.deserialize_json(
            data["aiAgent"]
        )
    return out


def redact_sensitive(value: CreateAIAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_agent" in value:
        import capo_qconnect.types.ai_agent_data

        out["ai_agent"] = capo_qconnect.types.ai_agent_data.redact_sensitive(
            value["ai_agent"]
        )
    return out

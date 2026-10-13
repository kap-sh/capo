"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAIAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_data
    import capo_qconnect.types.version


class GetAIAgentResponse(TypedDict, closed=True):
    ai_agent: NotRequired["capo_qconnect.types.ai_agent_data.AIAgentData"]
    """<p>The data of the AI Agent.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number of the AI Agent version (returned if an AI Agent version was specified via use of a qualifier for the <code>aiAgentId</code> on the request). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAIAgentResponse) -> dict:
    out: dict = {}
    if "ai_agent" in value:
        import capo_qconnect.types.ai_agent_data

        out["aiAgent"] = capo_qconnect.types.ai_agent_data.serialize_json(
            value["ai_agent"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> GetAIAgentResponse:
    out: GetAIAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiAgent") is not None:
        import capo_qconnect.types.ai_agent_data

        out["ai_agent"] = capo_qconnect.types.ai_agent_data.deserialize_json(
            data["aiAgent"]
        )
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    return out


def redact_sensitive(value: GetAIAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_agent" in value:
        import capo_qconnect.types.ai_agent_data

        out["ai_agent"] = capo_qconnect.types.ai_agent_data.redact_sensitive(
            value["ai_agent"]
        )
    return out

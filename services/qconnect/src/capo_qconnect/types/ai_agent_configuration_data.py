"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentConfigurationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_with_qualifier


class AIAgentConfigurationData(TypedDict, closed=True):
    ai_agent_id: "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    """<p>The ID of the AI Agent to be configured.</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the AI Agent configured for this AI Agent type is enabled. When this value is omitted or set to true, the configured AI Agent runs; when set to false, the AI Agent ID is retained but no AI Agent runs for the AI Agent type. Setting this value to false is currently supported only for the <code>ANSWER_RECOMMENDATION</code> AI Agent type; other requests to set it to false are rejected with a validation error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentConfigurationData) -> dict:
    out: dict = {}
    out["aiAgentId"] = value["ai_agent_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AIAgentConfigurationData:
    out: AIAgentConfigurationData = {}  # type: ignore[typeddict-item]
    if data.get("aiAgentId") is not None:
        out["ai_agent_id"] = data["aiAgentId"]
    else:
        out["ai_agent_id"] = ""
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out

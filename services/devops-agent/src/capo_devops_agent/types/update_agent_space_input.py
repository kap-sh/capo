"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAgentSpaceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.agent_space_name
    import capo_devops_agent.types.agent_space_preferences
    import capo_devops_agent.types.description
    import capo_devops_agent.types.locale


class UpdateAgentSpaceInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    name: NotRequired["capo_devops_agent.types.agent_space_name.AgentSpaceName"]
    """<p>The updated name of the AgentSpace.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>The updated description of the AgentSpace.</p>"""
    locale: NotRequired["capo_devops_agent.types.locale.Locale"]
    """<p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>"""
    preferences: NotRequired[
        "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
    ]
    """<p>The preferences to configure on the agent space. When provided, this replaces the full set of configured preferences; preferences not included revert to their default values. When omitted, the current preferences are left unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentSpaceInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "preferences" in value:
        import capo_devops_agent.types.agent_space_preferences

        out["preferences"] = (
            capo_devops_agent.types.agent_space_preferences.serialize_json(
                value["preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentSpaceInput:
    out: UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("preferences") is not None:
        import capo_devops_agent.types.agent_space_preferences

        out["preferences"] = (
            capo_devops_agent.types.agent_space_preferences.deserialize_json(
                data["preferences"]
            )
        )
    return out


def redact_sensitive(value: UpdateAgentSpaceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

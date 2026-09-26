"""Generated from Smithy shape ``com.amazonaws.agentregistry#AgentSkillsAdditionalData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.agent_skills_md_descriptor


class AgentSkillsAdditionalData(TypedDict, closed=True):
    skill_md: NotRequired[
        "capo_agent_registry.types.agent_skills_md_descriptor.AgentSkillsMdDescriptor"
    ]
    """<p> The agent skills markdown descriptor associated with the agent skills definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSkillsAdditionalData) -> dict:
    out: dict = {}
    if "skill_md" in value:
        import capo_agent_registry.types.agent_skills_md_descriptor

        out["skillMd"] = (
            capo_agent_registry.types.agent_skills_md_descriptor.serialize_json(
                value["skill_md"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentSkillsAdditionalData:
    out: AgentSkillsAdditionalData = {}  # type: ignore[typeddict-item]
    if data.get("skillMd") is not None:
        import capo_agent_registry.types.agent_skills_md_descriptor

        out["skill_md"] = (
            capo_agent_registry.types.agent_skills_md_descriptor.deserialize_json(
                data["skillMd"]
            )
        )
    return out

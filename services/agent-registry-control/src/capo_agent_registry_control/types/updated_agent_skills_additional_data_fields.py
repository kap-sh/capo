"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAgentSkillsAdditionalDataFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_agent_skills_md_descriptor


class UpdatedAgentSkillsAdditionalDataFields(TypedDict, closed=True):
    skill_md: NotRequired[
        "capo_agent_registry_control.types.updated_agent_skills_md_descriptor.UpdatedAgentSkillsMdDescriptor"
    ]
    """<p>The patch for the agent skills markdown descriptor field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgentSkillsAdditionalDataFields) -> dict:
    out: dict = {}
    if "skill_md" in value:
        import capo_agent_registry_control.types.updated_agent_skills_md_descriptor

        out["skillMd"] = (
            capo_agent_registry_control.types.updated_agent_skills_md_descriptor.serialize_json(
                value["skill_md"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgentSkillsAdditionalDataFields:
    out: UpdatedAgentSkillsAdditionalDataFields = {}  # type: ignore[typeddict-item]
    if data.get("skillMd") is not None:
        import capo_agent_registry_control.types.updated_agent_skills_md_descriptor

        out["skill_md"] = (
            capo_agent_registry_control.types.updated_agent_skills_md_descriptor.deserialize_json(
                data["skillMd"]
            )
        )
    return out

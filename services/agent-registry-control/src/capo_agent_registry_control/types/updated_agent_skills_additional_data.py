"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAgentSkillsAdditionalData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_agent_skills_additional_data_fields


class UpdatedAgentSkillsAdditionalData(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.updated_agent_skills_additional_data_fields.UpdatedAgentSkillsAdditionalDataFields"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgentSkillsAdditionalData) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.updated_agent_skills_additional_data_fields

        out["optionalValue"] = (
            capo_agent_registry_control.types.updated_agent_skills_additional_data_fields.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgentSkillsAdditionalData:
    out: UpdatedAgentSkillsAdditionalData = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.updated_agent_skills_additional_data_fields

        out["optional_value"] = (
            capo_agent_registry_control.types.updated_agent_skills_additional_data_fields.deserialize_json(
                data["optionalValue"]
            )
        )
    return out

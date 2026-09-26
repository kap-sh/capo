"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAgentSkillsDefinitionDescriptorFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_agent_skills_additional_data
    import capo_agent_registry_control.types.updated_data_schema_version
    import capo_agent_registry_control.types.updated_descriptor_data


class UpdatedAgentSkillsDefinitionDescriptorFields(TypedDict, closed=True):
    data: NotRequired[
        "capo_agent_registry_control.types.updated_descriptor_data.UpdatedDescriptorData"
    ]
    """<p>The patch for the descriptor's data field.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry_control.types.updated_data_schema_version.UpdatedDataSchemaVersion"
    ]
    """<p>The patch for the descriptor's data schema version field.</p>"""
    additional_data: NotRequired[
        "capo_agent_registry_control.types.updated_agent_skills_additional_data.UpdatedAgentSkillsAdditionalData"
    ]
    """<p>The patch for the descriptor's additional data field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgentSkillsDefinitionDescriptorFields) -> dict:
    out: dict = {}
    if "data" in value:
        import capo_agent_registry_control.types.updated_descriptor_data

        out["data"] = (
            capo_agent_registry_control.types.updated_descriptor_data.serialize_json(
                value["data"]
            )
        )
    if "data_schema_version" in value:
        import capo_agent_registry_control.types.updated_data_schema_version

        out["dataSchemaVersion"] = (
            capo_agent_registry_control.types.updated_data_schema_version.serialize_json(
                value["data_schema_version"]
            )
        )
    if "additional_data" in value:
        import capo_agent_registry_control.types.updated_agent_skills_additional_data

        out["additionalData"] = (
            capo_agent_registry_control.types.updated_agent_skills_additional_data.serialize_json(
                value["additional_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgentSkillsDefinitionDescriptorFields:
    out: UpdatedAgentSkillsDefinitionDescriptorFields = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_agent_registry_control.types.updated_descriptor_data

        out["data"] = (
            capo_agent_registry_control.types.updated_descriptor_data.deserialize_json(
                data["data"]
            )
        )
    if data.get("dataSchemaVersion") is not None:
        import capo_agent_registry_control.types.updated_data_schema_version

        out["data_schema_version"] = (
            capo_agent_registry_control.types.updated_data_schema_version.deserialize_json(
                data["dataSchemaVersion"]
            )
        )
    if data.get("additionalData") is not None:
        import capo_agent_registry_control.types.updated_agent_skills_additional_data

        out["additional_data"] = (
            capo_agent_registry_control.types.updated_agent_skills_additional_data.deserialize_json(
                data["additionalData"]
            )
        )
    return out

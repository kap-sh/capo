"""Generated from Smithy shape ``com.amazonaws.agentregistry#AgentSkillsDefinitionDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.agent_skills_additional_data
    import capo_agent_registry.types.data_schema_version
    import capo_agent_registry.types.descriptor_data


class AgentSkillsDefinitionDescriptor(TypedDict, closed=True):
    data: NotRequired["capo_agent_registry.types.descriptor_data.DescriptorData"]
    """<p> The agent skills definition content, serialized as descriptor payload data.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry.types.data_schema_version.DataSchemaVersion"
    ]
    """<p> The schema version of the descriptor payload.</p>"""
    additional_data: NotRequired[
        "capo_agent_registry.types.agent_skills_additional_data.AgentSkillsAdditionalData"
    ]
    """<p> Additional data for the agent skills definition, such as the skills markdown descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSkillsDefinitionDescriptor) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    if "data_schema_version" in value:
        out["dataSchemaVersion"] = value["data_schema_version"]
    if "additional_data" in value:
        import capo_agent_registry.types.agent_skills_additional_data

        out["additionalData"] = (
            capo_agent_registry.types.agent_skills_additional_data.serialize_json(
                value["additional_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentSkillsDefinitionDescriptor:
    out: AgentSkillsDefinitionDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("dataSchemaVersion") is not None:
        out["data_schema_version"] = data["dataSchemaVersion"]
    if data.get("additionalData") is not None:
        import capo_agent_registry.types.agent_skills_additional_data

        out["additional_data"] = (
            capo_agent_registry.types.agent_skills_additional_data.deserialize_json(
                data["additionalData"]
            )
        )
    return out

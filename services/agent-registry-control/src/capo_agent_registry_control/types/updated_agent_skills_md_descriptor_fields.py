"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedAgentSkillsMdDescriptorFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_data_schema_version
    import capo_agent_registry_control.types.updated_descriptor_data
    import capo_agent_registry_control.types.updated_descriptor_source


class UpdatedAgentSkillsMdDescriptorFields(TypedDict, closed=True):
    data: NotRequired[
        "capo_agent_registry_control.types.updated_descriptor_data.UpdatedDescriptorData"
    ]
    """<p>The patch for the descriptor's data field.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry_control.types.updated_data_schema_version.UpdatedDataSchemaVersion"
    ]
    """<p>The patch for the descriptor's data schema version field.</p>"""
    source: NotRequired[
        "capo_agent_registry_control.types.updated_descriptor_source.UpdatedDescriptorSource"
    ]
    """<p>The patch for the descriptor's source field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAgentSkillsMdDescriptorFields) -> dict:
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
    if "source" in value:
        import capo_agent_registry_control.types.updated_descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.updated_descriptor_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAgentSkillsMdDescriptorFields:
    out: UpdatedAgentSkillsMdDescriptorFields = {}  # type: ignore[typeddict-item]
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
    if data.get("source") is not None:
        import capo_agent_registry_control.types.updated_descriptor_source

        out["source"] = (
            capo_agent_registry_control.types.updated_descriptor_source.deserialize_json(
                data["source"]
            )
        )
    return out

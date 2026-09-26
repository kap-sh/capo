"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedMcpToolsDescriptorFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_data_schema_version
    import capo_agent_registry_control.types.updated_descriptor_data


class UpdatedMcpToolsDescriptorFields(TypedDict, closed=True):
    data: NotRequired[
        "capo_agent_registry_control.types.updated_descriptor_data.UpdatedDescriptorData"
    ]
    """<p>The patch for the descriptor's data field.</p>"""
    data_schema_version: NotRequired[
        "capo_agent_registry_control.types.updated_data_schema_version.UpdatedDataSchemaVersion"
    ]
    """<p>The patch for the descriptor's data schema version field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedMcpToolsDescriptorFields) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdatedMcpToolsDescriptorFields:
    out: UpdatedMcpToolsDescriptorFields = {}  # type: ignore[typeddict-item]
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
    return out

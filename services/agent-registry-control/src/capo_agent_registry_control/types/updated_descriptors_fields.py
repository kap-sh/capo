"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedDescriptorsFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_a2a_agent_card_descriptor
    import capo_agent_registry_control.types.updated_ag_ui_descriptor
    import capo_agent_registry_control.types.updated_agent_skills_definition_descriptor
    import capo_agent_registry_control.types.updated_custom_descriptor
    import capo_agent_registry_control.types.updated_http_descriptor
    import capo_agent_registry_control.types.updated_mcp_server_descriptor


class UpdatedDescriptorsFields(TypedDict, closed=True):
    mcp_server: NotRequired[
        "capo_agent_registry_control.types.updated_mcp_server_descriptor.UpdatedMcpServerDescriptor"
    ]
    """<p>The patch for the MCP server descriptor.</p>"""
    a2a_agent_card: NotRequired[
        "capo_agent_registry_control.types.updated_a2a_agent_card_descriptor.UpdatedA2aAgentCardDescriptor"
    ]
    """<p>The patch for the A2A agent card descriptor.</p>"""
    agent_skills_definition: NotRequired[
        "capo_agent_registry_control.types.updated_agent_skills_definition_descriptor.UpdatedAgentSkillsDefinitionDescriptor"
    ]
    """<p>The patch for the agent skills definition descriptor.</p>"""
    custom: NotRequired[
        "capo_agent_registry_control.types.updated_custom_descriptor.UpdatedCustomDescriptor"
    ]
    """<p>The patch for the custom descriptor.</p>"""
    http: NotRequired[
        "capo_agent_registry_control.types.updated_http_descriptor.UpdatedHttpDescriptor"
    ]
    """<p>The patch for the HTTP descriptor.</p>"""
    agui: NotRequired[
        "capo_agent_registry_control.types.updated_ag_ui_descriptor.UpdatedAgUiDescriptor"
    ]
    """<p>The patch for the AG-UI descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescriptorsFields) -> dict:
    out: dict = {}
    if "mcp_server" in value:
        import capo_agent_registry_control.types.updated_mcp_server_descriptor

        out["mcpServer"] = (
            capo_agent_registry_control.types.updated_mcp_server_descriptor.serialize_json(
                value["mcp_server"]
            )
        )
    if "a2a_agent_card" in value:
        import capo_agent_registry_control.types.updated_a2a_agent_card_descriptor

        out["a2aAgentCard"] = (
            capo_agent_registry_control.types.updated_a2a_agent_card_descriptor.serialize_json(
                value["a2a_agent_card"]
            )
        )
    if "agent_skills_definition" in value:
        import capo_agent_registry_control.types.updated_agent_skills_definition_descriptor

        out["agentSkillsDefinition"] = (
            capo_agent_registry_control.types.updated_agent_skills_definition_descriptor.serialize_json(
                value["agent_skills_definition"]
            )
        )
    if "custom" in value:
        import capo_agent_registry_control.types.updated_custom_descriptor

        out["custom"] = (
            capo_agent_registry_control.types.updated_custom_descriptor.serialize_json(
                value["custom"]
            )
        )
    if "http" in value:
        import capo_agent_registry_control.types.updated_http_descriptor

        out["http"] = (
            capo_agent_registry_control.types.updated_http_descriptor.serialize_json(
                value["http"]
            )
        )
    if "agui" in value:
        import capo_agent_registry_control.types.updated_ag_ui_descriptor

        out["agui"] = (
            capo_agent_registry_control.types.updated_ag_ui_descriptor.serialize_json(
                value["agui"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedDescriptorsFields:
    out: UpdatedDescriptorsFields = {}  # type: ignore[typeddict-item]
    if data.get("mcpServer") is not None:
        import capo_agent_registry_control.types.updated_mcp_server_descriptor

        out["mcp_server"] = (
            capo_agent_registry_control.types.updated_mcp_server_descriptor.deserialize_json(
                data["mcpServer"]
            )
        )
    if data.get("a2aAgentCard") is not None:
        import capo_agent_registry_control.types.updated_a2a_agent_card_descriptor

        out["a2a_agent_card"] = (
            capo_agent_registry_control.types.updated_a2a_agent_card_descriptor.deserialize_json(
                data["a2aAgentCard"]
            )
        )
    if data.get("agentSkillsDefinition") is not None:
        import capo_agent_registry_control.types.updated_agent_skills_definition_descriptor

        out["agent_skills_definition"] = (
            capo_agent_registry_control.types.updated_agent_skills_definition_descriptor.deserialize_json(
                data["agentSkillsDefinition"]
            )
        )
    if data.get("custom") is not None:
        import capo_agent_registry_control.types.updated_custom_descriptor

        out["custom"] = (
            capo_agent_registry_control.types.updated_custom_descriptor.deserialize_json(
                data["custom"]
            )
        )
    if data.get("http") is not None:
        import capo_agent_registry_control.types.updated_http_descriptor

        out["http"] = (
            capo_agent_registry_control.types.updated_http_descriptor.deserialize_json(
                data["http"]
            )
        )
    if data.get("agui") is not None:
        import capo_agent_registry_control.types.updated_ag_ui_descriptor

        out["agui"] = (
            capo_agent_registry_control.types.updated_ag_ui_descriptor.deserialize_json(
                data["agui"]
            )
        )
    return out

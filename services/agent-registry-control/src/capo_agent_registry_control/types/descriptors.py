"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#Descriptors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.a2a_agent_card_descriptor
    import capo_agent_registry_control.types.ag_ui_descriptor
    import capo_agent_registry_control.types.agent_skills_definition_descriptor
    import capo_agent_registry_control.types.custom_descriptor
    import capo_agent_registry_control.types.http_descriptor
    import capo_agent_registry_control.types.mcp_server_descriptor


class Descriptors(TypedDict, closed=True):
    mcp_server: NotRequired[
        "capo_agent_registry_control.types.mcp_server_descriptor.McpServerDescriptor"
    ]
    """<p>The MCP server descriptor, populated when the record type is MCP.</p>"""
    a2a_agent_card: NotRequired[
        "capo_agent_registry_control.types.a2a_agent_card_descriptor.A2aAgentCardDescriptor"
    ]
    """<p>The A2A agent card descriptor, populated when the record type is AGENT.</p>"""
    agent_skills_definition: NotRequired[
        "capo_agent_registry_control.types.agent_skills_definition_descriptor.AgentSkillsDefinitionDescriptor"
    ]
    """<p>The agent skills definition descriptor, populated when the record type is SKILL.</p>"""
    custom: NotRequired[
        "capo_agent_registry_control.types.custom_descriptor.CustomDescriptor"
    ]
    """<p>The custom descriptor, populated when the record type is CUSTOM.</p>"""
    http: NotRequired[
        "capo_agent_registry_control.types.http_descriptor.HttpDescriptor"
    ]
    """<p>The HTTP descriptor, populated for records detected from an HTTP protocol source.</p>"""
    agui: NotRequired[
        "capo_agent_registry_control.types.ag_ui_descriptor.AgUiDescriptor"
    ]
    """<p>The AG-UI descriptor, populated for records detected from an AG-UI protocol source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Descriptors) -> dict:
    out: dict = {}
    if "mcp_server" in value:
        import capo_agent_registry_control.types.mcp_server_descriptor

        out["mcpServer"] = (
            capo_agent_registry_control.types.mcp_server_descriptor.serialize_json(
                value["mcp_server"]
            )
        )
    if "a2a_agent_card" in value:
        import capo_agent_registry_control.types.a2a_agent_card_descriptor

        out["a2aAgentCard"] = (
            capo_agent_registry_control.types.a2a_agent_card_descriptor.serialize_json(
                value["a2a_agent_card"]
            )
        )
    if "agent_skills_definition" in value:
        import capo_agent_registry_control.types.agent_skills_definition_descriptor

        out["agentSkillsDefinition"] = (
            capo_agent_registry_control.types.agent_skills_definition_descriptor.serialize_json(
                value["agent_skills_definition"]
            )
        )
    if "custom" in value:
        import capo_agent_registry_control.types.custom_descriptor

        out["custom"] = (
            capo_agent_registry_control.types.custom_descriptor.serialize_json(
                value["custom"]
            )
        )
    if "http" in value:
        import capo_agent_registry_control.types.http_descriptor

        out["http"] = capo_agent_registry_control.types.http_descriptor.serialize_json(
            value["http"]
        )
    if "agui" in value:
        import capo_agent_registry_control.types.ag_ui_descriptor

        out["agui"] = capo_agent_registry_control.types.ag_ui_descriptor.serialize_json(
            value["agui"]
        )
    return out


def deserialize_json(data: dict) -> Descriptors:
    out: Descriptors = {}  # type: ignore[typeddict-item]
    if data.get("mcpServer") is not None:
        import capo_agent_registry_control.types.mcp_server_descriptor

        out["mcp_server"] = (
            capo_agent_registry_control.types.mcp_server_descriptor.deserialize_json(
                data["mcpServer"]
            )
        )
    if data.get("a2aAgentCard") is not None:
        import capo_agent_registry_control.types.a2a_agent_card_descriptor

        out["a2a_agent_card"] = (
            capo_agent_registry_control.types.a2a_agent_card_descriptor.deserialize_json(
                data["a2aAgentCard"]
            )
        )
    if data.get("agentSkillsDefinition") is not None:
        import capo_agent_registry_control.types.agent_skills_definition_descriptor

        out["agent_skills_definition"] = (
            capo_agent_registry_control.types.agent_skills_definition_descriptor.deserialize_json(
                data["agentSkillsDefinition"]
            )
        )
    if data.get("custom") is not None:
        import capo_agent_registry_control.types.custom_descriptor

        out["custom"] = (
            capo_agent_registry_control.types.custom_descriptor.deserialize_json(
                data["custom"]
            )
        )
    if data.get("http") is not None:
        import capo_agent_registry_control.types.http_descriptor

        out["http"] = (
            capo_agent_registry_control.types.http_descriptor.deserialize_json(
                data["http"]
            )
        )
    if data.get("agui") is not None:
        import capo_agent_registry_control.types.ag_ui_descriptor

        out["agui"] = (
            capo_agent_registry_control.types.ag_ui_descriptor.deserialize_json(
                data["agui"]
            )
        )
    return out

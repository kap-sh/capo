"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#McpServerAdditionalData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.mcp_tools_descriptor


class McpServerAdditionalData(TypedDict, closed=True):
    tools: NotRequired[
        "capo_agent_registry_control.types.mcp_tools_descriptor.McpToolsDescriptor"
    ]
    """<p>The MCP tools descriptor that defines the tools exposed by the MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpServerAdditionalData) -> dict:
    out: dict = {}
    if "tools" in value:
        import capo_agent_registry_control.types.mcp_tools_descriptor

        out["tools"] = (
            capo_agent_registry_control.types.mcp_tools_descriptor.serialize_json(
                value["tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> McpServerAdditionalData:
    out: McpServerAdditionalData = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_agent_registry_control.types.mcp_tools_descriptor

        out["tools"] = (
            capo_agent_registry_control.types.mcp_tools_descriptor.deserialize_json(
                data["tools"]
            )
        )
    return out

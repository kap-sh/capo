"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedMcpServerAdditionalDataFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.updated_mcp_tools_descriptor


class UpdatedMcpServerAdditionalDataFields(TypedDict, closed=True):
    tools: NotRequired[
        "capo_agent_registry_control.types.updated_mcp_tools_descriptor.UpdatedMcpToolsDescriptor"
    ]
    """<p>The patch for the MCP tools descriptor field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedMcpServerAdditionalDataFields) -> dict:
    out: dict = {}
    if "tools" in value:
        import capo_agent_registry_control.types.updated_mcp_tools_descriptor

        out["tools"] = (
            capo_agent_registry_control.types.updated_mcp_tools_descriptor.serialize_json(
                value["tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedMcpServerAdditionalDataFields:
    out: UpdatedMcpServerAdditionalDataFields = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_agent_registry_control.types.updated_mcp_tools_descriptor

        out["tools"] = (
            capo_agent_registry_control.types.updated_mcp_tools_descriptor.deserialize_json(
                data["tools"]
            )
        )
    return out

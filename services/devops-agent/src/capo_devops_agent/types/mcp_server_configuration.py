"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_tool_details_list
    import capo_devops_agent.types.mcp_tools_list


class MCPServerConfiguration(TypedDict, closed=True):
    tools: "capo_devops_agent.types.mcp_tools_list.MCPToolsList"
    """<p>List of MCP tools can be used with the association.</p>"""
    tool_details: NotRequired[
        "capo_devops_agent.types.mcp_tool_details_list.MCPToolDetailsList"
    ]
    """<p>List of MCP tools with their access categorization. When provided, the tool names must match those in the tools member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerConfiguration) -> dict:
    out: dict = {}
    import capo_devops_agent.types.mcp_tools_list

    out["tools"] = capo_devops_agent.types.mcp_tools_list.serialize_json(value["tools"])
    if "tool_details" in value:
        import capo_devops_agent.types.mcp_tool_details_list

        out["toolDetails"] = (
            capo_devops_agent.types.mcp_tool_details_list.serialize_json(
                value["tool_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> MCPServerConfiguration:
    out: MCPServerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_devops_agent.types.mcp_tools_list

        out["tools"] = capo_devops_agent.types.mcp_tools_list.deserialize_json(
            data["tools"]
        )
    else:
        out["tools"] = []
    if data.get("toolDetails") is not None:
        import capo_devops_agent.types.mcp_tool_details_list

        out["tool_details"] = (
            capo_devops_agent.types.mcp_tool_details_list.deserialize_json(
                data["toolDetails"]
            )
        )
    return out

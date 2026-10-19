"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerGrafanaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_tool_details_list
    import capo_devops_agent.types.mcp_tools_list


class MCPServerGrafanaConfiguration(TypedDict, closed=True):
    endpoint: "str"
    """<p>Grafana instance URL (e.g., https://your-instance.grafana.net)</p>"""
    organization_id: NotRequired["str"]
    """<p>The Grafana organization ID that can be used.</p>"""
    tools: NotRequired["capo_devops_agent.types.mcp_tools_list.MCPToolsList"]
    """<p>List of MCP tools that can be used.</p>"""
    enabled_elevated_tools: NotRequired[
        "capo_devops_agent.types.mcp_tool_details_list.MCPToolDetailsList"
    ]
    """<p>The subset of elevated-access tools enabled for this integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerGrafanaConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "tools" in value:
        import capo_devops_agent.types.mcp_tools_list

        out["tools"] = capo_devops_agent.types.mcp_tools_list.serialize_json(
            value["tools"]
        )
    if "enabled_elevated_tools" in value:
        import capo_devops_agent.types.mcp_tool_details_list

        out["enabledElevatedTools"] = (
            capo_devops_agent.types.mcp_tool_details_list.serialize_json(
                value["enabled_elevated_tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> MCPServerGrafanaConfiguration:
    out: MCPServerGrafanaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("organizationId") is not None:
        out["organization_id"] = data["organizationId"]
    if data.get("tools") is not None:
        import capo_devops_agent.types.mcp_tools_list

        out["tools"] = capo_devops_agent.types.mcp_tools_list.deserialize_json(
            data["tools"]
        )
    if data.get("enabledElevatedTools") is not None:
        import capo_devops_agent.types.mcp_tool_details_list

        out["enabled_elevated_tools"] = (
            capo_devops_agent.types.mcp_tool_details_list.deserialize_json(
                data["enabledElevatedTools"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MCPGatewayConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mcp_instructions
    import capo_bedrock_agentcore_control.types.mcp_supported_versions
    import capo_bedrock_agentcore_control.types.search_type
    import capo_bedrock_agentcore_control.types.session_configuration
    import capo_bedrock_agentcore_control.types.streaming_configuration


class MCPGatewayConfiguration(TypedDict, closed=True):
    supported_versions: NotRequired[
        "capo_bedrock_agentcore_control.types.mcp_supported_versions.McpSupportedVersions"
    ]
    """<p>The supported versions of the Model Context Protocol. This field specifies which versions of the protocol the gateway can use.</p>"""
    instructions: NotRequired[
        "capo_bedrock_agentcore_control.types.mcp_instructions.McpInstructions"
    ]
    """<p>The instructions for using the Model Context Protocol gateway. These instructions provide guidance on how to interact with the gateway.</p>"""
    search_type: NotRequired[
        "capo_bedrock_agentcore_control.types.search_type.SearchType"
    ]
    """<p>The search type for the Model Context Protocol gateway. This field specifies how the gateway handles search operations.</p>"""
    session_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.session_configuration.SessionConfiguration"
    ]
    """<p>The session configuration for the MCP gateway. This configuration controls session behavior, including session timeout settings.</p>"""
    streaming_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.streaming_configuration.StreamingConfiguration"
    ]
    """<p>The streaming configuration for the MCP gateway. This configuration controls whether response streaming is enabled for the gateway.</p>"""
    disable_mcp_list_tools_pagination: NotRequired["bool"]
    """<p>Specifies whether pagination is disabled for the Model Context Protocol (MCP) <code>tools/list</code> operation. When set to <code>true</code>, the gateway returns the complete list of tools in a single response without a pagination cursor. When set to <code>false</code> or omitted, the gateway returns tools in paginated responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPGatewayConfiguration) -> dict:
    out: dict = {}
    if "supported_versions" in value:
        import capo_bedrock_agentcore_control.types.mcp_supported_versions

        out["supportedVersions"] = (
            capo_bedrock_agentcore_control.types.mcp_supported_versions.serialize_json(
                value["supported_versions"]
            )
        )
    if "instructions" in value:
        out["instructions"] = value["instructions"]
    if "search_type" in value:
        import capo_bedrock_agentcore_control.types.search_type

        out["searchType"] = (
            capo_bedrock_agentcore_control.types.search_type.serialize_json(
                value["search_type"]
            )
        )
    if "session_configuration" in value:
        import capo_bedrock_agentcore_control.types.session_configuration

        out["sessionConfiguration"] = (
            capo_bedrock_agentcore_control.types.session_configuration.serialize_json(
                value["session_configuration"]
            )
        )
    if "streaming_configuration" in value:
        import capo_bedrock_agentcore_control.types.streaming_configuration

        out["streamingConfiguration"] = (
            capo_bedrock_agentcore_control.types.streaming_configuration.serialize_json(
                value["streaming_configuration"]
            )
        )
    if "disable_mcp_list_tools_pagination" in value:
        out["disableMcpListToolsPagination"] = value[
            "disable_mcp_list_tools_pagination"
        ]
    return out


def deserialize_json(data: dict) -> MCPGatewayConfiguration:
    out: MCPGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("supportedVersions") is not None:
        import capo_bedrock_agentcore_control.types.mcp_supported_versions

        out["supported_versions"] = (
            capo_bedrock_agentcore_control.types.mcp_supported_versions.deserialize_json(
                data["supportedVersions"]
            )
        )
    if data.get("instructions") is not None:
        out["instructions"] = data["instructions"]
    if data.get("searchType") is not None:
        import capo_bedrock_agentcore_control.types.search_type

        out["search_type"] = (
            capo_bedrock_agentcore_control.types.search_type.deserialize_json(
                data["searchType"]
            )
        )
    if data.get("sessionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.session_configuration

        out["session_configuration"] = (
            capo_bedrock_agentcore_control.types.session_configuration.deserialize_json(
                data["sessionConfiguration"]
            )
        )
    if data.get("streamingConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.streaming_configuration

        out["streaming_configuration"] = (
            capo_bedrock_agentcore_control.types.streaming_configuration.deserialize_json(
                data["streamingConfiguration"]
            )
        )
    if data.get("disableMcpListToolsPagination") is not None:
        out["disable_mcp_list_tools_pagination"] = data["disableMcpListToolsPagination"]
    return out

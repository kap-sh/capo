"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerSigV4ServiceDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.mcp_server_endpoint
    import capo_devops_agent.types.mcp_server_name
    import capo_devops_agent.types.mcp_server_sig_v4_authorization_config


class MCPServerSigV4ServiceDetails(TypedDict, closed=True):
    name: "capo_devops_agent.types.mcp_server_name.MCPServerName"
    """<p>MCP server name.</p>"""
    endpoint: "capo_devops_agent.types.mcp_server_endpoint.MCPServerEndpoint"
    """<p>MCP server endpoint URL.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>Optional description for the MCP server.</p>"""
    authorization_config: "capo_devops_agent.types.mcp_server_sig_v4_authorization_config.MCPServerSigV4AuthorizationConfig"
    """<p>MCP Server SigV4 authorization configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerSigV4ServiceDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_devops_agent.types.mcp_server_sig_v4_authorization_config

    out["authorizationConfig"] = (
        capo_devops_agent.types.mcp_server_sig_v4_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> MCPServerSigV4ServiceDetails:
    out: MCPServerSigV4ServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authorizationConfig") is not None:
        import capo_devops_agent.types.mcp_server_sig_v4_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.mcp_server_sig_v4_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "MCPServerSigV4ServiceDetails.authorization_config required"
        )
    return out


def redact_sensitive(value: MCPServerSigV4ServiceDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "authorization_config" in value:
        import capo_devops_agent.types.mcp_server_sig_v4_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.mcp_server_sig_v4_authorization_config.redact_sensitive(
                value["authorization_config"]
            )
        )
    return out

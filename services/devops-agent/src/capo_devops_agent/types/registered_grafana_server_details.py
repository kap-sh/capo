"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredGrafanaServerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_server_authorization_method
    import capo_devops_agent.types.mcp_server_endpoint


class RegisteredGrafanaServerDetails(TypedDict, closed=True):
    endpoint: "capo_devops_agent.types.mcp_server_endpoint.MCPServerEndpoint"
    """<p>Grafana instance URL (e.g., https://your-instance.grafana.net)</p>"""
    authorization_method: "capo_devops_agent.types.mcp_server_authorization_method.MCPServerAuthorizationMethod"
    """<p>The authz method used by the MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredGrafanaServerDetails) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    import capo_devops_agent.types.mcp_server_authorization_method

    out["authorizationMethod"] = (
        capo_devops_agent.types.mcp_server_authorization_method.serialize_json(
            value["authorization_method"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisteredGrafanaServerDetails:
    out: RegisteredGrafanaServerDetails = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("authorizationMethod") is not None:
        import capo_devops_agent.types.mcp_server_authorization_method

        out["authorization_method"] = (
            capo_devops_agent.types.mcp_server_authorization_method.deserialize_json(
                data["authorizationMethod"]
            )
        )
    else:
        import typing

        out["authorization_method"] = typing.cast(
            "capo_devops_agent.types.mcp_server_authorization_method.MCPServerAuthorizationMethod",
            "",
        )
    return out

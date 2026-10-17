"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredMCPServerDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.custom_header_names
    import capo_devops_agent.types.description
    import capo_devops_agent.types.mcp_server_authorization_method


class RegisteredMCPServerDetails(TypedDict, closed=True):
    name: "str"
    """<p>The MCP server name.</p>"""
    endpoint: "str"
    """<p>The MCP server endpoint URL.</p>"""
    authorization_method: "capo_devops_agent.types.mcp_server_authorization_method.MCPServerAuthorizationMethod"
    """<p>The MCP server uses this authorization method.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>Optional description for the MCP server.</p>"""
    api_key_header: NotRequired["str"]
    """<p>If the MCP server uses API key authentication, these details are provided.</p>"""
    custom_header_names: NotRequired[
        "capo_devops_agent.types.custom_header_names.CustomHeaderNames"
    ]
    """<p>The configured custom authentication header names when the MCP server uses custom-header authentication. Secret values are not returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredMCPServerDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    import capo_devops_agent.types.mcp_server_authorization_method

    out["authorizationMethod"] = (
        capo_devops_agent.types.mcp_server_authorization_method.serialize_json(
            value["authorization_method"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "api_key_header" in value:
        out["apiKeyHeader"] = value["api_key_header"]
    if "custom_header_names" in value:
        import capo_devops_agent.types.custom_header_names

        out["customHeaderNames"] = (
            capo_devops_agent.types.custom_header_names.serialize_json(
                value["custom_header_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredMCPServerDetails:
    out: RegisteredMCPServerDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisteredMCPServerDetails.name required")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RegisteredMCPServerDetails.endpoint required")
    if data.get("authorizationMethod") is not None:
        import capo_devops_agent.types.mcp_server_authorization_method

        out["authorization_method"] = (
            capo_devops_agent.types.mcp_server_authorization_method.deserialize_json(
                data["authorizationMethod"]
            )
        )
    else:
        raise DeserializationError(
            "RegisteredMCPServerDetails.authorization_method required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("apiKeyHeader") is not None:
        out["api_key_header"] = data["apiKeyHeader"]
    if data.get("customHeaderNames") is not None:
        import capo_devops_agent.types.custom_header_names

        out["custom_header_names"] = (
            capo_devops_agent.types.custom_header_names.deserialize_json(
                data["customHeaderNames"]
            )
        )
    return out


def redact_sensitive(value: RegisteredMCPServerDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

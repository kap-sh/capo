"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerSigV4AuthorizationConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.custom_headers
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.sig_v4_region


class MCPServerSigV4AuthorizationConfig(TypedDict, closed=True):
    region: "capo_devops_agent.types.sig_v4_region.SigV4Region"
    """<p>AWS region for SigV4 signing. Use '*' for SigV4a multi-region signing.</p>"""
    service: "str"
    """<p>AWS service name for SigV4 signing.</p>"""
    role_arn: "str"
    """<p>Deprecated — use mcpRoleArn instead. IAM role ARN to assume for SigV4 signing.</p>"""
    mcp_role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]
    """<p>IAM role ARN to assume for SigV4 signing. Optional — when omitted, credentials are resolved at runtime via a monitor account association.</p>"""
    custom_headers: NotRequired["capo_devops_agent.types.custom_headers.CustomHeaders"]
    """<p>Custom headers for the SigV4 MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerSigV4AuthorizationConfig) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    out["service"] = value["service"]
    out["roleArn"] = value.get("role_arn", "")
    if "mcp_role_arn" in value:
        out["mcpRoleArn"] = value["mcp_role_arn"]
    if "custom_headers" in value:
        import capo_devops_agent.types.custom_headers

        out["customHeaders"] = capo_devops_agent.types.custom_headers.serialize_json(
            value["custom_headers"]
        )
    return out


def deserialize_json(data: dict) -> MCPServerSigV4AuthorizationConfig:
    out: MCPServerSigV4AuthorizationConfig = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("mcpRoleArn") is not None:
        out["mcp_role_arn"] = data["mcpRoleArn"]
    if data.get("customHeaders") is not None:
        import capo_devops_agent.types.custom_headers

        out["custom_headers"] = capo_devops_agent.types.custom_headers.deserialize_json(
            data["customHeaders"]
        )
    return out


def redact_sensitive(value: MCPServerSigV4AuthorizationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_headers" in value:
        import capo_devops_agent.types.custom_headers

        out["custom_headers"] = capo_devops_agent.types.custom_headers.redact_sensitive(
            value["custom_headers"]
        )
    return out

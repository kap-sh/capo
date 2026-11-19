"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessRemoteMcpConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_remote_mcp_outbound_auth
    import capo_bedrock_agentcore_control.types.harness_remote_mcp_url
    import capo_bedrock_agentcore_control.types.http_headers_map


class HarnessRemoteMcpConfig(TypedDict, closed=True):
    url: "capo_bedrock_agentcore_control.types.harness_remote_mcp_url.HarnessRemoteMcpUrl"
    """<p>URL of the MCP endpoint.</p>"""
    headers: NotRequired[
        "capo_bedrock_agentcore_control.types.http_headers_map.HttpHeadersMap"
    ]
    """<p>Custom headers to include when connecting to the remote MCP server.</p>"""
    outbound_auth: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_remote_mcp_outbound_auth.HarnessRemoteMcpOutboundAuth"
    ]
    """<p>How the harness authenticates to this MCP server. Defaults to no authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessRemoteMcpConfig) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "headers" in value:
        import capo_bedrock_agentcore_control.types.http_headers_map

        out["headers"] = (
            capo_bedrock_agentcore_control.types.http_headers_map.serialize_json(
                value["headers"]
            )
        )
    if "outbound_auth" in value:
        import capo_bedrock_agentcore_control.types.harness_remote_mcp_outbound_auth

        out["outboundAuth"] = (
            capo_bedrock_agentcore_control.types.harness_remote_mcp_outbound_auth.serialize_json(
                value["outbound_auth"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessRemoteMcpConfig:
    out: HarnessRemoteMcpConfig = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("headers") is not None:
        import capo_bedrock_agentcore_control.types.http_headers_map

        out["headers"] = (
            capo_bedrock_agentcore_control.types.http_headers_map.deserialize_json(
                data["headers"]
            )
        )
    if data.get("outboundAuth") is not None:
        import capo_bedrock_agentcore_control.types.harness_remote_mcp_outbound_auth

        out["outbound_auth"] = (
            capo_bedrock_agentcore_control.types.harness_remote_mcp_outbound_auth.deserialize_json(
                data["outboundAuth"]
            )
        )
    return out


def redact_sensitive(value: HarnessRemoteMcpConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    if "headers" in value:
        out["headers"] = "*** Sensitive Data Redacted ***"
    return out

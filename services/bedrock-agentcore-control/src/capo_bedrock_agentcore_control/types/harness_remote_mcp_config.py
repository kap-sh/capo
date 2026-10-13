"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessRemoteMcpConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_remote_mcp_url
    import capo_bedrock_agentcore_control.types.http_headers_map


class HarnessRemoteMcpConfig(TypedDict, closed=True):
    url: "capo_bedrock_agentcore_control.types.harness_remote_mcp_url.HarnessRemoteMcpUrl"
    """<p>URL of the MCP endpoint.</p>"""
    headers: NotRequired[
        "capo_bedrock_agentcore_control.types.http_headers_map.HttpHeadersMap"
    ]
    """<p>Custom headers to include when connecting to the remote MCP server.</p>"""


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
    return out


def deserialize_json(data: dict) -> HarnessRemoteMcpConfig:
    out: HarnessRemoteMcpConfig = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("HarnessRemoteMcpConfig.url required")
    if data.get("headers") is not None:
        import capo_bedrock_agentcore_control.types.http_headers_map

        out["headers"] = (
            capo_bedrock_agentcore_control.types.http_headers_map.deserialize_json(
                data["headers"]
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

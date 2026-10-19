"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExternalProxy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.domain_patterns
    import capo_bedrock_agentcore.types.host_name
    import capo_bedrock_agentcore.types.proxy_credentials


class ExternalProxy(TypedDict, closed=True):
    server: "capo_bedrock_agentcore.types.host_name.HostName"
    """<p>The hostname of the proxy server. Must be a valid DNS hostname (maximum 253 characters).</p>"""
    port: "int"
    """<p>The port number of the proxy server. Valid range: 1-65535.</p>"""
    domain_patterns: NotRequired[
        "capo_bedrock_agentcore.types.domain_patterns.DomainPatterns"
    ]
    """<p>Optional array of domain patterns that should route through this specific proxy. Supports <code>.example.com</code> for subdomain matching (matches any subdomain of example.com) or <code>example.com</code> for exact domain matching. If omitted, this proxy acts as a catch-all for domains not matched by other proxies. Maximum 100 patterns per proxy, each up to 253 characters.</p>"""
    credentials: NotRequired[
        "capo_bedrock_agentcore.types.proxy_credentials.ProxyCredentials"
    ]
    """<p>Optional authentication credentials for the proxy server. If omitted, the proxy is accessed without authentication (useful for IP-allowlisted proxies).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalProxy) -> dict:
    out: dict = {}
    out["server"] = value["server"]
    out["port"] = value["port"]
    if "domain_patterns" in value:
        import capo_bedrock_agentcore.types.domain_patterns

        out["domainPatterns"] = (
            capo_bedrock_agentcore.types.domain_patterns.serialize_json(
                value["domain_patterns"]
            )
        )
    if "credentials" in value:
        import capo_bedrock_agentcore.types.proxy_credentials

        out["credentials"] = (
            capo_bedrock_agentcore.types.proxy_credentials.serialize_json(
                value["credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalProxy:
    out: ExternalProxy = {}  # type: ignore[typeddict-item]
    if data.get("server") is not None:
        out["server"] = data["server"]
    else:
        out["server"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("domainPatterns") is not None:
        import capo_bedrock_agentcore.types.domain_patterns

        out["domain_patterns"] = (
            capo_bedrock_agentcore.types.domain_patterns.deserialize_json(
                data["domainPatterns"]
            )
        )
    if data.get("credentials") is not None:
        import capo_bedrock_agentcore.types.proxy_credentials

        out["credentials"] = (
            capo_bedrock_agentcore.types.proxy_credentials.deserialize_json(
                data["credentials"]
            )
        )
    return out

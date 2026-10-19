"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProxyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.proxies
    import capo_bedrock_agentcore.types.proxy_bypass


class ProxyConfiguration(TypedDict, closed=True):
    proxies: "capo_bedrock_agentcore.types.proxies.Proxies"
    """<p>An array of 1-5 proxy server configurations for domain-based routing. Each proxy can specify which domains it handles via <code>domainPatterns</code>, enabling flexible routing of different traffic through different proxies based on destination domain.</p>"""
    bypass: NotRequired["capo_bedrock_agentcore.types.proxy_bypass.ProxyBypass"]
    """<p>Optional configuration for domains that should bypass all proxies and connect directly to their destination, like the internet. Takes precedence over all proxy routing rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProxyConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.proxies

    out["proxies"] = capo_bedrock_agentcore.types.proxies.serialize_json(
        value["proxies"]
    )
    if "bypass" in value:
        import capo_bedrock_agentcore.types.proxy_bypass

        out["bypass"] = capo_bedrock_agentcore.types.proxy_bypass.serialize_json(
            value["bypass"]
        )
    return out


def deserialize_json(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("proxies") is not None:
        import capo_bedrock_agentcore.types.proxies

        out["proxies"] = capo_bedrock_agentcore.types.proxies.deserialize_json(
            data["proxies"]
        )
    else:
        out["proxies"] = []
    if data.get("bypass") is not None:
        import capo_bedrock_agentcore.types.proxy_bypass

        out["bypass"] = capo_bedrock_agentcore.types.proxy_bypass.deserialize_json(
            data["bypass"]
        )
    return out

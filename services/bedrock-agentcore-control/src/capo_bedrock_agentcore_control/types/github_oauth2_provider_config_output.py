"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GithubOauth2ProviderConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_id_type
    import capo_bedrock_agentcore_control.types.oauth2_discovery


class GithubOauth2ProviderConfigOutput(TypedDict, closed=True):
    oauth_discovery: (
        "capo_bedrock_agentcore_control.types.oauth2_discovery.Oauth2Discovery"
    )
    """<p>The OAuth2 discovery information for the GitHub provider.</p>"""
    client_id: NotRequired[
        "capo_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    ]
    """<p>The client ID for the GitHub OAuth2 provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GithubOauth2ProviderConfigOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.oauth2_discovery

    out["oauthDiscovery"] = (
        capo_bedrock_agentcore_control.types.oauth2_discovery.serialize_json(
            value["oauth_discovery"]
        )
    )
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> GithubOauth2ProviderConfigOutput:
    out: GithubOauth2ProviderConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("oauthDiscovery") is not None:
        import capo_bedrock_agentcore_control.types.oauth2_discovery

        out["oauth_discovery"] = (
            capo_bedrock_agentcore_control.types.oauth2_discovery.deserialize_json(
                data["oauthDiscovery"]
            )
        )
    else:
        out["oauth_discovery"] = {"$unknown": {"name": ""}}
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    return out

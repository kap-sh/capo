"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomOauth2ProviderConfigOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_authentication_method_type
    import capo_bedrock_agentcore_control.types.client_id_type
    import capo_bedrock_agentcore_control.types.oauth2_discovery
    import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.private_endpoint_overrides
    import capo_bedrock_agentcore_control.types.private_key_jwt_config


class CustomOauth2ProviderConfigOutput(TypedDict, closed=True):
    oauth_discovery: (
        "capo_bedrock_agentcore_control.types.oauth2_discovery.Oauth2Discovery"
    )
    """<p>The OAuth2 discovery information for the custom provider.</p>"""
    client_id: NotRequired[
        "capo_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    ]
    """<p>The client ID for the custom OAuth2 provider.</p>"""
    on_behalf_of_token_exchange_config: NotRequired[
        "capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.OnBehalfOfTokenExchangeConfigType"
    ]
    """<p>The configuration for on-behalf-of token exchange.</p>"""
    client_authentication_method: NotRequired[
        "capo_bedrock_agentcore_control.types.client_authentication_method_type.ClientAuthenticationMethodType"
    ]
    """<p>The client authentication method used when authenticating with the token endpoint.</p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.</p>"""
    private_endpoint_overrides: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint_overrides.PrivateEndpointOverrides"
    ]
    """<p>The private endpoint overrides for the custom OAuth2 provider configuration.</p>"""
    private_key_jwt_config: NotRequired[
        "capo_bedrock_agentcore_control.types.private_key_jwt_config.PrivateKeyJwtConfig"
    ]
    """<p>The configuration for private_key_jwt client authentication used by this OAuth2 credential provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOauth2ProviderConfigOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.oauth2_discovery

    out["oauthDiscovery"] = (
        capo_bedrock_agentcore_control.types.oauth2_discovery.serialize_json(
            value["oauth_discovery"]
        )
    )
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "on_behalf_of_token_exchange_config" in value:
        import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type

        out["onBehalfOfTokenExchangeConfig"] = (
            capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.serialize_json(
                value["on_behalf_of_token_exchange_config"]
            )
        )
    if "client_authentication_method" in value:
        import capo_bedrock_agentcore_control.types.client_authentication_method_type

        out["clientAuthenticationMethod"] = (
            capo_bedrock_agentcore_control.types.client_authentication_method_type.serialize_json(
                value["client_authentication_method"]
            )
        )
    if "private_endpoint" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    if "private_endpoint_overrides" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint_overrides

        out["privateEndpointOverrides"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_overrides.serialize_json(
                value["private_endpoint_overrides"]
            )
        )
    if "private_key_jwt_config" in value:
        import capo_bedrock_agentcore_control.types.private_key_jwt_config

        out["privateKeyJwtConfig"] = (
            capo_bedrock_agentcore_control.types.private_key_jwt_config.serialize_json(
                value["private_key_jwt_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomOauth2ProviderConfigOutput:
    out: CustomOauth2ProviderConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("oauthDiscovery") is not None:
        import capo_bedrock_agentcore_control.types.oauth2_discovery

        out["oauth_discovery"] = (
            capo_bedrock_agentcore_control.types.oauth2_discovery.deserialize_json(
                data["oauthDiscovery"]
            )
        )
    else:
        import capo_bedrock_agentcore_control.types._unknown

        out["oauth_discovery"] = (
            capo_bedrock_agentcore_control.types._unknown.UnknownUnionMember("")
        )
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("onBehalfOfTokenExchangeConfig") is not None:
        import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type

        out["on_behalf_of_token_exchange_config"] = (
            capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.deserialize_json(
                data["onBehalfOfTokenExchangeConfig"]
            )
        )
    if data.get("clientAuthenticationMethod") is not None:
        import capo_bedrock_agentcore_control.types.client_authentication_method_type

        out["client_authentication_method"] = (
            capo_bedrock_agentcore_control.types.client_authentication_method_type.deserialize_json(
                data["clientAuthenticationMethod"]
            )
        )
    if data.get("privateEndpoint") is not None:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    if data.get("privateEndpointOverrides") is not None:
        import capo_bedrock_agentcore_control.types.private_endpoint_overrides

        out["private_endpoint_overrides"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_overrides.deserialize_json(
                data["privateEndpointOverrides"]
            )
        )
    if data.get("privateKeyJwtConfig") is not None:
        import capo_bedrock_agentcore_control.types.private_key_jwt_config

        out["private_key_jwt_config"] = (
            capo_bedrock_agentcore_control.types.private_key_jwt_config.deserialize_json(
                data["privateKeyJwtConfig"]
            )
        )
    return out


def redact_sensitive(value: CustomOauth2ProviderConfigOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_key_jwt_config" in value:
        import capo_bedrock_agentcore_control.types.private_key_jwt_config

        out["private_key_jwt_config"] = (
            capo_bedrock_agentcore_control.types.private_key_jwt_config.redact_sensitive(
                value["private_key_jwt_config"]
            )
        )
    return out

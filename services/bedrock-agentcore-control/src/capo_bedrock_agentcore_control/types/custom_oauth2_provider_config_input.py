"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomOauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_authentication_method_type
    import capo_bedrock_agentcore_control.types.default_client_id_type
    import capo_bedrock_agentcore_control.types.default_client_secret_type
    import capo_bedrock_agentcore_control.types.oauth2_discovery
    import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.private_endpoint_overrides
    import capo_bedrock_agentcore_control.types.private_key_jwt_config
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type


class CustomOauth2ProviderConfigInput(TypedDict, closed=True):
    oauth_discovery: (
        "capo_bedrock_agentcore_control.types.oauth2_discovery.Oauth2Discovery"
    )
    """<p>The OAuth2 discovery information for the custom provider.</p>"""
    client_id: "capo_bedrock_agentcore_control.types.default_client_id_type.DefaultClientIdType"
    """<p>The client ID for the custom OAuth2 provider.</p>"""
    client_secret: "capo_bedrock_agentcore_control.types.default_client_secret_type.DefaultClientSecretType"
    """<p>The client secret for the custom OAuth2 provider.</p>"""
    client_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when <code>clientSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    client_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the client secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    on_behalf_of_token_exchange_config: NotRequired[
        "capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_config_type.OnBehalfOfTokenExchangeConfigType"
    ]
    """<p>The configuration for on-behalf-of token exchange. This enables authentication flows that use RFC 8693 token exchange or RFC 7523 JWT authorization grants.</p>"""
    client_authentication_method: NotRequired[
        "capo_bedrock_agentcore_control.types.client_authentication_method_type.ClientAuthenticationMethodType"
    ]
    """<p>The client authentication method to use when authenticating with the token endpoint.</p>"""
    private_key_jwt_config: NotRequired[
        "capo_bedrock_agentcore_control.types.private_key_jwt_config.PrivateKeyJwtConfig"
    ]
    """<p>The private_key_jwt client authentication configuration for this credential provider. When specified, the credential provider uses JWT client assertions to authenticate with the token endpoint.</p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.</p>"""
    private_endpoint_overrides: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint_overrides.PrivateEndpointOverrides"
    ]
    """<p>The private endpoint overrides for the custom OAuth2 provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOauth2ProviderConfigInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.oauth2_discovery

    out["oauthDiscovery"] = (
        capo_bedrock_agentcore_control.types.oauth2_discovery.serialize_json(
            value["oauth_discovery"]
        )
    )
    out["clientId"] = value.get("client_id", "")
    out["clientSecret"] = value.get("client_secret", "")
    if "client_secret_config" in value:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["clientSecretConfig"] = (
            capo_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["client_secret_config"]
            )
        )
    if "client_secret_source" in value:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["clientSecretSource"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["client_secret_source"]
            )
        )
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
    if "private_key_jwt_config" in value:
        import capo_bedrock_agentcore_control.types.private_key_jwt_config

        out["privateKeyJwtConfig"] = (
            capo_bedrock_agentcore_control.types.private_key_jwt_config.serialize_json(
                value["private_key_jwt_config"]
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
    return out


def deserialize_json(data: dict) -> CustomOauth2ProviderConfigInput:
    out: CustomOauth2ProviderConfigInput = {}  # type: ignore[typeddict-item]
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
    else:
        out["client_id"] = ""
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        out["client_secret"] = ""
    if data.get("clientSecretConfig") is not None:
        import capo_bedrock_agentcore_control.types.secret_reference

        out["client_secret_config"] = (
            capo_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["clientSecretConfig"]
            )
        )
    if data.get("clientSecretSource") is not None:
        import capo_bedrock_agentcore_control.types.secret_source_type

        out["client_secret_source"] = (
            capo_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["clientSecretSource"]
            )
        )
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
    if data.get("privateKeyJwtConfig") is not None:
        import capo_bedrock_agentcore_control.types.private_key_jwt_config

        out["private_key_jwt_config"] = (
            capo_bedrock_agentcore_control.types.private_key_jwt_config.deserialize_json(
                data["privateKeyJwtConfig"]
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
    return out


def redact_sensitive(value: CustomOauth2ProviderConfigInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    if "private_key_jwt_config" in value:
        import capo_bedrock_agentcore_control.types.private_key_jwt_config

        out["private_key_jwt_config"] = (
            capo_bedrock_agentcore_control.types.private_key_jwt_config.redact_sensitive(
                value["private_key_jwt_config"]
            )
        )
    return out

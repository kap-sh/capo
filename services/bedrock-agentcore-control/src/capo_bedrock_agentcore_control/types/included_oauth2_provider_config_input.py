"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IncludedOauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorization_endpoint_type
    import capo_bedrock_agentcore_control.types.client_id_type
    import capo_bedrock_agentcore_control.types.default_client_secret_type
    import capo_bedrock_agentcore_control.types.issuer_url_type
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type
    import capo_bedrock_agentcore_control.types.token_endpoint_type


class IncludedOauth2ProviderConfigInput(TypedDict, closed=True):
    client_id: "capo_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    """<p>The client ID for the supported OAuth2 provider. This identifier is assigned by the OAuth2 provider when you register your application.</p>"""
    client_secret: "capo_bedrock_agentcore_control.types.default_client_secret_type.DefaultClientSecretType"
    """<p>The client secret for the supported OAuth2 provider. This secret is assigned by the OAuth2 provider and used along with the client ID to authenticate your application.</p>"""
    client_secret_config: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when <code>clientSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    client_secret_source: NotRequired[
        "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the client secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>"""
    issuer: NotRequired[
        "capo_bedrock_agentcore_control.types.issuer_url_type.IssuerUrlType"
    ]
    """<p>Token issuer of your isolated OAuth2 application tenant. This URL identifies the authorization server that issues tokens for this provider.</p>"""
    authorization_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.authorization_endpoint_type.AuthorizationEndpointType"
    ]
    """<p>OAuth2 authorization endpoint for your isolated OAuth2 application tenant. This is where users are redirected to authenticate and authorize access to their resources.</p>"""
    token_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.token_endpoint_type.TokenEndpointType"
    ]
    """<p>OAuth2 token endpoint for your isolated OAuth2 application tenant. This is where authorization codes are exchanged for access tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncludedOauth2ProviderConfigInput) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
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
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "authorization_endpoint" in value:
        out["authorizationEndpoint"] = value["authorization_endpoint"]
    if "token_endpoint" in value:
        out["tokenEndpoint"] = value["token_endpoint"]
    return out


def deserialize_json(data: dict) -> IncludedOauth2ProviderConfigInput:
    out: IncludedOauth2ProviderConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "IncludedOauth2ProviderConfigInput.client_id required"
        )
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
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    if data.get("authorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["authorizationEndpoint"]
    if data.get("tokenEndpoint") is not None:
        out["token_endpoint"] = data["tokenEndpoint"]
    return out


def redact_sensitive(value: IncludedOauth2ProviderConfigInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

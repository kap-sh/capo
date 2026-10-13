"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OAuthCredentialProvider``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.o_auth_credential_provider_arn
    import capo_bedrock_agentcore_control.types.o_auth_custom_parameters
    import capo_bedrock_agentcore_control.types.o_auth_default_return_url
    import capo_bedrock_agentcore_control.types.o_auth_grant_type
    import capo_bedrock_agentcore_control.types.o_auth_scopes


class OAuthCredentialProvider(TypedDict, closed=True):
    provider_arn: "capo_bedrock_agentcore_control.types.o_auth_credential_provider_arn.OAuthCredentialProviderArn"
    """<p>The Amazon Resource Name (ARN) of the OAuth credential provider. This ARN identifies the provider in Amazon Web Services.</p>"""
    scopes: "capo_bedrock_agentcore_control.types.o_auth_scopes.OAuthScopes"
    """<p>The OAuth scopes for the credential provider. These scopes define the level of access requested from the OAuth provider.</p>"""
    custom_parameters: NotRequired[
        "capo_bedrock_agentcore_control.types.o_auth_custom_parameters.OAuthCustomParameters"
    ]
    """<p>The custom parameters for the OAuth credential provider. These parameters provide additional configuration for the OAuth authentication process.</p>"""
    grant_type: "capo_bedrock_agentcore_control.types.o_auth_grant_type.OAuthGrantType"
    """<p>Specifies the kind of credentials to use for authorization:</p> <ul> <li> <p> <code>CLIENT_CREDENTIALS</code> - Authorization with a client ID and secret.</p> </li> <li> <p> <code>AUTHORIZATION_CODE</code> - Authorization with a token that is specific to an individual end user.</p> </li> <li> <p> <code>TOKEN_EXCHANGE</code> - Authorization using on-behalf-of token exchange. An inbound user token is exchanged for a downstream access token scoped to the target audience.</p> </li> </ul>"""
    default_return_url: NotRequired[
        "capo_bedrock_agentcore_control.types.o_auth_default_return_url.OAuthDefaultReturnUrl"
    ]
    """<p>The URL where the end user's browser is redirected after obtaining the authorization code. Generally points to the customer's application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthCredentialProvider) -> dict:
    out: dict = {}
    out["providerArn"] = value["provider_arn"]
    import capo_bedrock_agentcore_control.types.o_auth_scopes

    out["scopes"] = capo_bedrock_agentcore_control.types.o_auth_scopes.serialize_json(
        value["scopes"]
    )
    if "custom_parameters" in value:
        import capo_bedrock_agentcore_control.types.o_auth_custom_parameters

        out["customParameters"] = (
            capo_bedrock_agentcore_control.types.o_auth_custom_parameters.serialize_json(
                value["custom_parameters"]
            )
        )
    import capo_bedrock_agentcore_control.types.o_auth_grant_type

    out["grantType"] = (
        capo_bedrock_agentcore_control.types.o_auth_grant_type.serialize_json(
            value.get("grant_type", "CLIENT_CREDENTIALS")
        )
    )
    if "default_return_url" in value:
        out["defaultReturnUrl"] = value["default_return_url"]
    return out


def deserialize_json(data: dict) -> OAuthCredentialProvider:
    out: OAuthCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("providerArn") is not None:
        out["provider_arn"] = data["providerArn"]
    else:
        raise DeserializationError("OAuthCredentialProvider.provider_arn required")
    if data.get("scopes") is not None:
        import capo_bedrock_agentcore_control.types.o_auth_scopes

        out["scopes"] = (
            capo_bedrock_agentcore_control.types.o_auth_scopes.deserialize_json(
                data["scopes"]
            )
        )
    else:
        raise DeserializationError("OAuthCredentialProvider.scopes required")
    if data.get("customParameters") is not None:
        import capo_bedrock_agentcore_control.types.o_auth_custom_parameters

        out["custom_parameters"] = (
            capo_bedrock_agentcore_control.types.o_auth_custom_parameters.deserialize_json(
                data["customParameters"]
            )
        )
    if data.get("grantType") is not None:
        import capo_bedrock_agentcore_control.types.o_auth_grant_type

        out["grant_type"] = (
            capo_bedrock_agentcore_control.types.o_auth_grant_type.deserialize_json(
                data["grantType"]
            )
        )
    else:
        out["grant_type"] = "CLIENT_CREDENTIALS"
    if data.get("defaultReturnUrl") is not None:
        out["default_return_url"] = data["defaultReturnUrl"]
    return out


def redact_sensitive(value: OAuthCredentialProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_parameters" in value:
        import capo_bedrock_agentcore_control.types.o_auth_custom_parameters

        out["custom_parameters"] = (
            capo_bedrock_agentcore_control.types.o_auth_custom_parameters.redact_sensitive(
                value["custom_parameters"]
            )
        )
    return out

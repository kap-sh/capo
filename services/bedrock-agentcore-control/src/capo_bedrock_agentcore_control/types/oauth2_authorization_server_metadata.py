"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2AuthorizationServerMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorization_endpoint_type
    import capo_bedrock_agentcore_control.types.issuer_url_type
    import capo_bedrock_agentcore_control.types.response_list_type
    import capo_bedrock_agentcore_control.types.token_endpoint_auth_methods_type
    import capo_bedrock_agentcore_control.types.token_endpoint_type


class Oauth2AuthorizationServerMetadata(TypedDict, closed=True):
    issuer: "capo_bedrock_agentcore_control.types.issuer_url_type.IssuerUrlType"
    """<p>The issuer URL for the OAuth2 authorization server.</p>"""
    authorization_endpoint: "capo_bedrock_agentcore_control.types.authorization_endpoint_type.AuthorizationEndpointType"
    """<p>The authorization endpoint URL for the OAuth2 authorization server.</p>"""
    token_endpoint: (
        "capo_bedrock_agentcore_control.types.token_endpoint_type.TokenEndpointType"
    )
    """<p>The token endpoint URL for the OAuth2 authorization server.</p>"""
    response_types: NotRequired[
        "capo_bedrock_agentcore_control.types.response_list_type.ResponseListType"
    ]
    """<p>The supported response types for the OAuth2 authorization server.</p>"""
    token_endpoint_auth_methods: NotRequired[
        "capo_bedrock_agentcore_control.types.token_endpoint_auth_methods_type.TokenEndpointAuthMethodsType"
    ]
    """<p>The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2AuthorizationServerMetadata) -> dict:
    out: dict = {}
    out["issuer"] = value["issuer"]
    out["authorizationEndpoint"] = value["authorization_endpoint"]
    out["tokenEndpoint"] = value["token_endpoint"]
    if "response_types" in value:
        import capo_bedrock_agentcore_control.types.response_list_type

        out["responseTypes"] = (
            capo_bedrock_agentcore_control.types.response_list_type.serialize_json(
                value["response_types"]
            )
        )
    if "token_endpoint_auth_methods" in value:
        import capo_bedrock_agentcore_control.types.token_endpoint_auth_methods_type

        out["tokenEndpointAuthMethods"] = (
            capo_bedrock_agentcore_control.types.token_endpoint_auth_methods_type.serialize_json(
                value["token_endpoint_auth_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> Oauth2AuthorizationServerMetadata:
    out: Oauth2AuthorizationServerMetadata = {}  # type: ignore[typeddict-item]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    else:
        out["issuer"] = ""
    if data.get("authorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["authorizationEndpoint"]
    else:
        out["authorization_endpoint"] = ""
    if data.get("tokenEndpoint") is not None:
        out["token_endpoint"] = data["tokenEndpoint"]
    else:
        out["token_endpoint"] = ""
    if data.get("responseTypes") is not None:
        import capo_bedrock_agentcore_control.types.response_list_type

        out["response_types"] = (
            capo_bedrock_agentcore_control.types.response_list_type.deserialize_json(
                data["responseTypes"]
            )
        )
    if data.get("tokenEndpointAuthMethods") is not None:
        import capo_bedrock_agentcore_control.types.token_endpoint_auth_methods_type

        out["token_endpoint_auth_methods"] = (
            capo_bedrock_agentcore_control.types.token_endpoint_auth_methods_type.deserialize_json(
                data["tokenEndpointAuthMethods"]
            )
        )
    return out

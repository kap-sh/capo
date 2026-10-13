"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourceOauth2TokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.audiences_list_type
    import capo_bedrock_agentcore.types.credential_provider_name
    import capo_bedrock_agentcore.types.custom_request_parameters_type
    import capo_bedrock_agentcore.types.oauth2_flow_type
    import capo_bedrock_agentcore.types.request_uri
    import capo_bedrock_agentcore.types.resource_oauth2_return_url_type
    import capo_bedrock_agentcore.types.resources_list_type
    import capo_bedrock_agentcore.types.scopes_list_type
    import capo_bedrock_agentcore.types.state
    import capo_bedrock_agentcore.types.workload_identity_token_type


class GetResourceOauth2TokenRequest(TypedDict, closed=True):
    workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType"
    """<p>The identity token of the workload from which you want to retrieve the OAuth2 token.</p>"""
    resource_credential_provider_name: (
        "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName"
    )
    """<p>The name of the resource's credential provider.</p>"""
    scopes: "capo_bedrock_agentcore.types.scopes_list_type.ScopesListType"
    """<p>The OAuth scopes being requested.</p>"""
    oauth2_flow: "capo_bedrock_agentcore.types.oauth2_flow_type.Oauth2FlowType"
    """<p>The type of flow to be performed.</p>"""
    session_uri: NotRequired["capo_bedrock_agentcore.types.request_uri.RequestUri"]
    """<p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>"""
    resource_oauth2_return_url: NotRequired[
        "capo_bedrock_agentcore.types.resource_oauth2_return_url_type.ResourceOauth2ReturnUrlType"
    ]
    """<p>The callback URL to redirect to after the OAuth 2.0 token retrieval is complete. This URL must be one of the provided URLs configured for the workload identity.</p>"""
    force_authentication: NotRequired["bool"]
    """<p>Indicates whether to always initiate a new three-legged OAuth (3LO) flow, regardless of any existing session.</p>"""
    custom_parameters: NotRequired[
        "capo_bedrock_agentcore.types.custom_request_parameters_type.CustomRequestParametersType"
    ]
    """<p>A map of custom parameters to include in the authorization request to the resource credential provider. These parameters are in addition to the standard OAuth 2.0 flow parameters, and will not override them.</p>"""
    custom_state: NotRequired["capo_bedrock_agentcore.types.state.State"]
    """<p>An opaque string that will be sent back to the callback URL provided in resourceOauth2ReturnUrl. This state should be used to protect the callback URL of your application against CSRF attacks by ensuring the response corresponds to the original request.</p>"""
    resources: NotRequired[
        "capo_bedrock_agentcore.types.resources_list_type.ResourcesListType"
    ]
    """<p>The resources to include in the token request. These are used to specify the target resources for which the OAuth2 token is being requested.</p>"""
    audiences: NotRequired[
        "capo_bedrock_agentcore.types.audiences_list_type.AudiencesListType"
    ]
    """<p>The audiences to include in the token request. These are used to specify the intended recipients of the OAuth2 token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceOauth2TokenRequest) -> dict:
    out: dict = {}
    out["workloadIdentityToken"] = value["workload_identity_token"]
    out["resourceCredentialProviderName"] = value["resource_credential_provider_name"]
    import capo_bedrock_agentcore.types.scopes_list_type

    out["scopes"] = capo_bedrock_agentcore.types.scopes_list_type.serialize_json(
        value["scopes"]
    )
    import capo_bedrock_agentcore.types.oauth2_flow_type

    out["oauth2Flow"] = capo_bedrock_agentcore.types.oauth2_flow_type.serialize_json(
        value["oauth2_flow"]
    )
    if "session_uri" in value:
        out["sessionUri"] = value["session_uri"]
    if "resource_oauth2_return_url" in value:
        out["resourceOauth2ReturnUrl"] = value["resource_oauth2_return_url"]
    if "force_authentication" in value:
        out["forceAuthentication"] = value["force_authentication"]
    if "custom_parameters" in value:
        import capo_bedrock_agentcore.types.custom_request_parameters_type

        out["customParameters"] = (
            capo_bedrock_agentcore.types.custom_request_parameters_type.serialize_json(
                value["custom_parameters"]
            )
        )
    if "custom_state" in value:
        out["customState"] = value["custom_state"]
    if "resources" in value:
        import capo_bedrock_agentcore.types.resources_list_type

        out["resources"] = (
            capo_bedrock_agentcore.types.resources_list_type.serialize_json(
                value["resources"]
            )
        )
    if "audiences" in value:
        import capo_bedrock_agentcore.types.audiences_list_type

        out["audiences"] = (
            capo_bedrock_agentcore.types.audiences_list_type.serialize_json(
                value["audiences"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetResourceOauth2TokenRequest:
    out: GetResourceOauth2TokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadIdentityToken") is not None:
        out["workload_identity_token"] = data["workloadIdentityToken"]
    else:
        raise DeserializationError(
            "GetResourceOauth2TokenRequest.workload_identity_token required"
        )
    if data.get("resourceCredentialProviderName") is not None:
        out["resource_credential_provider_name"] = data[
            "resourceCredentialProviderName"
        ]
    else:
        raise DeserializationError(
            "GetResourceOauth2TokenRequest.resource_credential_provider_name required"
        )
    if data.get("scopes") is not None:
        import capo_bedrock_agentcore.types.scopes_list_type

        out["scopes"] = capo_bedrock_agentcore.types.scopes_list_type.deserialize_json(
            data["scopes"]
        )
    else:
        raise DeserializationError("GetResourceOauth2TokenRequest.scopes required")
    if data.get("oauth2Flow") is not None:
        import capo_bedrock_agentcore.types.oauth2_flow_type

        out["oauth2_flow"] = (
            capo_bedrock_agentcore.types.oauth2_flow_type.deserialize_json(
                data["oauth2Flow"]
            )
        )
    else:
        raise DeserializationError("GetResourceOauth2TokenRequest.oauth2_flow required")
    if data.get("sessionUri") is not None:
        out["session_uri"] = data["sessionUri"]
    if data.get("resourceOauth2ReturnUrl") is not None:
        out["resource_oauth2_return_url"] = data["resourceOauth2ReturnUrl"]
    if data.get("forceAuthentication") is not None:
        out["force_authentication"] = data["forceAuthentication"]
    if data.get("customParameters") is not None:
        import capo_bedrock_agentcore.types.custom_request_parameters_type

        out["custom_parameters"] = (
            capo_bedrock_agentcore.types.custom_request_parameters_type.deserialize_json(
                data["customParameters"]
            )
        )
    if data.get("customState") is not None:
        out["custom_state"] = data["customState"]
    if data.get("resources") is not None:
        import capo_bedrock_agentcore.types.resources_list_type

        out["resources"] = (
            capo_bedrock_agentcore.types.resources_list_type.deserialize_json(
                data["resources"]
            )
        )
    if data.get("audiences") is not None:
        import capo_bedrock_agentcore.types.audiences_list_type

        out["audiences"] = (
            capo_bedrock_agentcore.types.audiences_list_type.deserialize_json(
                data["audiences"]
            )
        )
    return out


def redact_sensitive(value: GetResourceOauth2TokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "workload_identity_token" in value:
        out["workload_identity_token"] = "*** Sensitive Data Redacted ***"
    if "custom_parameters" in value:
        import capo_bedrock_agentcore.types.custom_request_parameters_type

        out["custom_parameters"] = (
            capo_bedrock_agentcore.types.custom_request_parameters_type.redact_sensitive(
                value["custom_parameters"]
            )
        )
    if "custom_state" in value:
        out["custom_state"] = "*** Sensitive Data Redacted ***"
    return out

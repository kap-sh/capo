"""Generated from Smithy shape ``com.amazonaws.sagemaker#OidcConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.authentication_request_extra_params
    import capo_sagemaker.types.client_id
    import capo_sagemaker.types.client_secret
    import capo_sagemaker.types.oidc_endpoint
    import capo_sagemaker.types.scope


class OidcConfig(TypedDict, closed=True):
    client_id: NotRequired["capo_sagemaker.types.client_id.ClientId"]
    """<p>The OIDC IdP client ID used to configure your private workforce.</p>"""
    client_secret: NotRequired["capo_sagemaker.types.client_secret.ClientSecret"]
    """<p>The OIDC IdP client secret used to configure your private workforce.</p>"""
    issuer: NotRequired["capo_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP issuer used to configure your private workforce.</p>"""
    authorization_endpoint: NotRequired[
        "capo_sagemaker.types.oidc_endpoint.OidcEndpoint"
    ]
    """<p>The OIDC IdP authorization endpoint used to configure your private workforce.</p>"""
    token_endpoint: NotRequired["capo_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP token endpoint used to configure your private workforce.</p>"""
    user_info_endpoint: NotRequired["capo_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP user information endpoint used to configure your private workforce.</p>"""
    logout_endpoint: NotRequired["capo_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP logout endpoint used to configure your private workforce.</p>"""
    jwks_uri: NotRequired["capo_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP JSON Web Key Set (Jwks) URI used to configure your private workforce.</p>"""
    scope: NotRequired["capo_sagemaker.types.scope.Scope"]
    """<p>An array of string identifiers used to refer to the specific pieces of user data or claims that the client application wants to access.</p>"""
    authentication_request_extra_params: NotRequired[
        "capo_sagemaker.types.authentication_request_extra_params.AuthenticationRequestExtraParams"
    ]
    """<p>A string to string map of identifiers specific to the custom identity provider (IdP) being used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OidcConfig) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "authorization_endpoint" in value:
        out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    if "token_endpoint" in value:
        out["TokenEndpoint"] = value["token_endpoint"]
    if "user_info_endpoint" in value:
        out["UserInfoEndpoint"] = value["user_info_endpoint"]
    if "logout_endpoint" in value:
        out["LogoutEndpoint"] = value["logout_endpoint"]
    if "jwks_uri" in value:
        out["JwksUri"] = value["jwks_uri"]
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "authentication_request_extra_params" in value:
        import capo_sagemaker.types.authentication_request_extra_params

        out["AuthenticationRequestExtraParams"] = (
            capo_sagemaker.types.authentication_request_extra_params.serialize_aws_json_1_1(
                value["authentication_request_extra_params"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OidcConfig:
    out: OidcConfig = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("Issuer") is not None:
        out["issuer"] = data["Issuer"]
    if data.get("AuthorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    if data.get("TokenEndpoint") is not None:
        out["token_endpoint"] = data["TokenEndpoint"]
    if data.get("UserInfoEndpoint") is not None:
        out["user_info_endpoint"] = data["UserInfoEndpoint"]
    if data.get("LogoutEndpoint") is not None:
        out["logout_endpoint"] = data["LogoutEndpoint"]
    if data.get("JwksUri") is not None:
        out["jwks_uri"] = data["JwksUri"]
    if data.get("Scope") is not None:
        out["scope"] = data["Scope"]
    if data.get("AuthenticationRequestExtraParams") is not None:
        import capo_sagemaker.types.authentication_request_extra_params

        out["authentication_request_extra_params"] = (
            capo_sagemaker.types.authentication_request_extra_params.deserialize_aws_json_1_1(
                data["AuthenticationRequestExtraParams"]
            )
        )
    return out


def redact_sensitive(value: OidcConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

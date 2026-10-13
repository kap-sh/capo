"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.access_token
    import capo_appflow.types.client_credentials_arn
    import capo_appflow.types.connector_o_auth_request
    import capo_appflow.types.jwt_token
    import capo_appflow.types.o_auth2_grant_type
    import capo_appflow.types.refresh_token


class SalesforceConnectorProfileCredentials(TypedDict, closed=True):
    access_token: NotRequired["capo_appflow.types.access_token.AccessToken"]
    """<p> The credentials used to access protected Salesforce resources. </p>"""
    refresh_token: NotRequired["capo_appflow.types.refresh_token.RefreshToken"]
    """<p> The credentials used to acquire new access tokens. </p>"""
    o_auth_request: NotRequired[
        "capo_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]
    """<p> The OAuth requirement needed to request security tokens from the connector endpoint. </p>"""
    client_credentials_arn: NotRequired[
        "capo_appflow.types.client_credentials_arn.ClientCredentialsArn"
    ]
    """<p> The secret manager ARN, which contains the client ID and client secret of the connected app. </p>"""
    o_auth2_grant_type: NotRequired[
        "capo_appflow.types.o_auth2_grant_type.OAuth2GrantType"
    ]
    """<p>Specifies the OAuth 2.0 grant type that Amazon AppFlow uses when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.</p> <p>You can specify one of the following values:</p> <dl> <dt>AUTHORIZATION_CODE</dt> <dd> <p>Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.</p> </dd> <dt>JWT_BEARER</dt> <dd> <p>Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.</p> </dd> </dl> <note> <p>The CLIENT_CREDENTIALS value is not supported for Salesforce.</p> </note>"""
    jwt_token: NotRequired["capo_appflow.types.jwt_token.JwtToken"]
    """<p>A JSON web token (JWT) that authorizes Amazon AppFlow to access your Salesforce records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "o_auth_request" in value:
        import capo_appflow.types.connector_o_auth_request

        out["oAuthRequest"] = (
            capo_appflow.types.connector_o_auth_request.serialize_json(
                value["o_auth_request"]
            )
        )
    if "client_credentials_arn" in value:
        out["clientCredentialsArn"] = value["client_credentials_arn"]
    if "o_auth2_grant_type" in value:
        import capo_appflow.types.o_auth2_grant_type

        out["oAuth2GrantType"] = capo_appflow.types.o_auth2_grant_type.serialize_json(
            value["o_auth2_grant_type"]
        )
    if "jwt_token" in value:
        out["jwtToken"] = value["jwt_token"]
    return out


def deserialize_json(data: dict) -> SalesforceConnectorProfileCredentials:
    out: SalesforceConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    if data.get("refreshToken") is not None:
        out["refresh_token"] = data["refreshToken"]
    if data.get("oAuthRequest") is not None:
        import capo_appflow.types.connector_o_auth_request

        out["o_auth_request"] = (
            capo_appflow.types.connector_o_auth_request.deserialize_json(
                data["oAuthRequest"]
            )
        )
    if data.get("clientCredentialsArn") is not None:
        out["client_credentials_arn"] = data["clientCredentialsArn"]
    if data.get("oAuth2GrantType") is not None:
        import capo_appflow.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            capo_appflow.types.o_auth2_grant_type.deserialize_json(
                data["oAuth2GrantType"]
            )
        )
    if data.get("jwtToken") is not None:
        out["jwt_token"] = data["jwtToken"]
    return out


def redact_sensitive(value: SalesforceConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    if "o_auth_request" in value:
        import capo_appflow.types.connector_o_auth_request

        out["o_auth_request"] = (
            capo_appflow.types.connector_o_auth_request.redact_sensitive(
                value["o_auth_request"]
            )
        )
    if "client_credentials_arn" in value:
        out["client_credentials_arn"] = "*** Sensitive Data Redacted ***"
    if "jwt_token" in value:
        out["jwt_token"] = "*** Sensitive Data Redacted ***"
    return out

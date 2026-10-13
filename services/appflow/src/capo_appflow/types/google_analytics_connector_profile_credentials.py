"""Generated from Smithy shape ``com.amazonaws.appflow#GoogleAnalyticsConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.access_token
    import capo_appflow.types.client_id
    import capo_appflow.types.client_secret
    import capo_appflow.types.connector_o_auth_request
    import capo_appflow.types.refresh_token


class GoogleAnalyticsConnectorProfileCredentials(TypedDict, closed=True):
    client_id: "capo_appflow.types.client_id.ClientId"
    """<p> The identifier for the desired client. </p>"""
    client_secret: "capo_appflow.types.client_secret.ClientSecret"
    """<p> The client secret used by the OAuth client to authenticate to the authorization server. </p>"""
    access_token: NotRequired["capo_appflow.types.access_token.AccessToken"]
    """<p> The credentials used to access protected Google Analytics resources. </p>"""
    refresh_token: NotRequired["capo_appflow.types.refresh_token.RefreshToken"]
    """<p> The credentials used to acquire new access tokens. This is required only for OAuth2 access tokens, and is not required for OAuth1 access tokens. </p>"""
    o_auth_request: NotRequired[
        "capo_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]
    """<p> The OAuth requirement needed to request security tokens from the connector endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoogleAnalyticsConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
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
    return out


def deserialize_json(data: dict) -> GoogleAnalyticsConnectorProfileCredentials:
    out: GoogleAnalyticsConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "GoogleAnalyticsConnectorProfileCredentials.client_id required"
        )
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "GoogleAnalyticsConnectorProfileCredentials.client_secret required"
        )
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
    return out


def redact_sensitive(
    value: GoogleAnalyticsConnectorProfileCredentials,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    if "o_auth_request" in value:
        import capo_appflow.types.connector_o_auth_request

        out["o_auth_request"] = (
            capo_appflow.types.connector_o_auth_request.redact_sensitive(
                value["o_auth_request"]
            )
        )
    return out

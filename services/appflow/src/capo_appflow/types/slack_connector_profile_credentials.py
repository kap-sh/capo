"""Generated from Smithy shape ``com.amazonaws.appflow#SlackConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.access_token
    import capo_appflow.types.client_id
    import capo_appflow.types.client_secret
    import capo_appflow.types.connector_o_auth_request


class SlackConnectorProfileCredentials(TypedDict, closed=True):
    client_id: "capo_appflow.types.client_id.ClientId"
    """<p> The identifier for the client. </p>"""
    client_secret: "capo_appflow.types.client_secret.ClientSecret"
    """<p> The client secret used by the OAuth client to authenticate to the authorization server. </p>"""
    access_token: NotRequired["capo_appflow.types.access_token.AccessToken"]
    """<p> The credentials used to access protected Slack resources. </p>"""
    o_auth_request: NotRequired[
        "capo_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]
    """<p> The OAuth requirement needed to request security tokens from the connector endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "o_auth_request" in value:
        import capo_appflow.types.connector_o_auth_request

        out["oAuthRequest"] = (
            capo_appflow.types.connector_o_auth_request.serialize_json(
                value["o_auth_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlackConnectorProfileCredentials:
    out: SlackConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "SlackConnectorProfileCredentials.client_id required"
        )
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "SlackConnectorProfileCredentials.client_secret required"
        )
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    if data.get("oAuthRequest") is not None:
        import capo_appflow.types.connector_o_auth_request

        out["o_auth_request"] = (
            capo_appflow.types.connector_o_auth_request.deserialize_json(
                data["oAuthRequest"]
            )
        )
    return out


def redact_sensitive(value: SlackConnectorProfileCredentials) -> dict[str, Any]:
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

"""Generated from Smithy shape ``com.amazonaws.appflow#HoneycodeConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.access_token
    import capo_appflow.types.connector_o_auth_request
    import capo_appflow.types.refresh_token


class HoneycodeConnectorProfileCredentials(TypedDict, closed=True):
    access_token: NotRequired["capo_appflow.types.access_token.AccessToken"]
    """<p> The credentials used to access protected Amazon Honeycode resources. </p>"""
    refresh_token: NotRequired["capo_appflow.types.refresh_token.RefreshToken"]
    """<p> The credentials used to acquire new access tokens. </p>"""
    o_auth_request: NotRequired[
        "capo_appflow.types.connector_o_auth_request.ConnectorOAuthRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HoneycodeConnectorProfileCredentials) -> dict:
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
    return out


def deserialize_json(data: dict) -> HoneycodeConnectorProfileCredentials:
    out: HoneycodeConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: HoneycodeConnectorProfileCredentials) -> dict[str, Any]:
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
    return out

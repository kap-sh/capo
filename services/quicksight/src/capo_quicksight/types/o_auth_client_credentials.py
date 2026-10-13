"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthClientCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.o_auth_client_id
    import capo_quicksight.types.o_auth_client_secret
    import capo_quicksight.types.o_auth_username


class OAuthClientCredentials(TypedDict, closed=True):
    client_id: NotRequired["capo_quicksight.types.o_auth_client_id.OAuthClientId"]
    """<p>The client ID of the OAuth 2.0 application that is registered with the data source provider.</p>"""
    client_secret: NotRequired[
        "capo_quicksight.types.o_auth_client_secret.OAuthClientSecret"
    ]
    """<p>The client secret of the OAuth 2.0 application that is registered with the data source provider.</p>"""
    username: NotRequired["capo_quicksight.types.o_auth_username.OAuthUsername"]
    """<p>The username of the account that is used for OAuth 2.0 client credentials authentication with the data source provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthClientCredentials) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "username" in value:
        out["Username"] = value["username"]
    return out


def deserialize_json(data: dict) -> OAuthClientCredentials:
    out: OAuthClientCredentials = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    return out


def redact_sensitive(value: OAuthClientCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out

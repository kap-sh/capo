"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.client_id
    import capo_quicksight.types.client_secret
    import capo_quicksight.types.endpoint


class AuthorizationCodeGrantDetails(TypedDict, closed=True):
    client_id: "capo_quicksight.types.client_id.ClientId"
    """<p>The client ID for the OAuth application.</p>"""
    client_secret: "capo_quicksight.types.client_secret.ClientSecret"
    """<p>The client secret for the OAuth application.</p>"""
    token_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The token endpoint URL for obtaining access tokens.</p>"""
    authorization_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The authorization endpoint URL for the OAuth flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["ClientSecret"] = value["client_secret"]
    out["TokenEndpoint"] = value["token_endpoint"]
    out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    return out


def deserialize_json(data: dict) -> AuthorizationCodeGrantDetails:
    out: AuthorizationCodeGrantDetails = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    else:
        out["client_secret"] = ""
    if data.get("TokenEndpoint") is not None:
        out["token_endpoint"] = data["TokenEndpoint"]
    else:
        out["token_endpoint"] = ""
    if data.get("AuthorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    else:
        out["authorization_endpoint"] = ""
    return out


def redact_sensitive(value: AuthorizationCodeGrantDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

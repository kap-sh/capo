"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsGrantDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.client_id
    import capo_quicksight.types.client_secret
    import capo_quicksight.types.endpoint


class ClientCredentialsGrantDetails(TypedDict, closed=True):
    client_id: "capo_quicksight.types.client_id.ClientId"
    """<p>The client identifier issued to the client during the registration process with the authorization server.</p>"""
    client_secret: "capo_quicksight.types.client_secret.ClientSecret"
    """<p>The client secret issued to the client during the registration process with the authorization server.</p>"""
    token_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain access tokens via the client credentials grant flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["ClientSecret"] = value["client_secret"]
    out["TokenEndpoint"] = value["token_endpoint"]
    return out


def deserialize_json(data: dict) -> ClientCredentialsGrantDetails:
    out: ClientCredentialsGrantDetails = {}  # type: ignore[typeddict-item]
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
    return out


def redact_sensitive(value: ClientCredentialsGrantDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

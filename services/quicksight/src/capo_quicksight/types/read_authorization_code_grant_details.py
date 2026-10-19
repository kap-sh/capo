"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthorizationCodeGrantDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.client_id
    import capo_quicksight.types.endpoint


class ReadAuthorizationCodeGrantDetails(TypedDict, closed=True):
    client_id: "capo_quicksight.types.client_id.ClientId"
    """<p>The client identifier for the OAuth2 authorization code grant flow.</p>"""
    token_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain access tokens via the authorization code grant flow.</p>"""
    authorization_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain authorization codes from the resource owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthorizationCodeGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["TokenEndpoint"] = value["token_endpoint"]
    out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    return out


def deserialize_json(data: dict) -> ReadAuthorizationCodeGrantDetails:
    out: ReadAuthorizationCodeGrantDetails = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("TokenEndpoint") is not None:
        out["token_endpoint"] = data["TokenEndpoint"]
    else:
        out["token_endpoint"] = ""
    if data.get("AuthorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    else:
        out["authorization_endpoint"] = ""
    return out

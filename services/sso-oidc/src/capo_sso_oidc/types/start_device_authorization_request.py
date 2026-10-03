"""Generated from Smithy shape ``com.amazonaws.ssooidc#StartDeviceAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_oidc.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_oidc.types.client_id
    import capo_sso_oidc.types.client_secret
    import capo_sso_oidc.types.uri


class StartDeviceAuthorizationRequest(TypedDict, closed=True):
    client_id: "capo_sso_oidc.types.client_id.ClientId"
    """<p>The unique identifier string for the client that is registered with IAM Identity Center. This value should come from the persisted result of the <a>RegisterClient</a> API operation.</p>"""
    client_secret: "capo_sso_oidc.types.client_secret.ClientSecret"
    """<p>A secret string that is generated for the client. This value should come from the persisted result of the <a>RegisterClient</a> API operation.</p>"""
    start_url: "capo_sso_oidc.types.uri.URI"
    """<p>The URL for the Amazon Web Services access portal. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html">Using the Amazon Web Services access portal</a> in the <i>IAM Identity Center User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeviceAuthorizationRequest) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    out["startUrl"] = value["start_url"]
    return out


def deserialize_json(data: dict) -> StartDeviceAuthorizationRequest:
    out: StartDeviceAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("StartDeviceAuthorizationRequest.client_id required")
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "StartDeviceAuthorizationRequest.client_secret required"
        )
    if data.get("startUrl") is not None:
        out["start_url"] = data["startUrl"]
    else:
        raise DeserializationError("StartDeviceAuthorizationRequest.start_url required")
    return out

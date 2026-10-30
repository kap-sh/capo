"""Generated from Smithy shape ``com.amazonaws.continuum#GitHubAuthorizationConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.authorization_code
    import capo_continuum.types.o_auth_state
    import capo_continuum.types.redirect_url


class GitHubAuthorizationConfiguration(TypedDict, closed=True):
    authorization_code: "capo_continuum.types.authorization_code.AuthorizationCode"
    """The OAuth authorization code returned by GitHub after the user authorizes the application."""
    state: "capo_continuum.types.o_auth_state.OAuthState"
    """The `state` returned by GitHub in the OAuth callback. It must be the state that StartIntegrationAuthorization returned to the same AWS account, and the authorization request must have sent that call's codeChallenge. The state can be redeemed once. A stage that enforces authorization sessions rejects a missing, expired, already used, or other-account state with ValidationException; restart the authorization with StartIntegrationAuthorization."""
    redirect_url: NotRequired["capo_continuum.types.redirect_url.RedirectUrl"]
    """The redirect URL used to obtain the authorization code. Must match one of the redirect URLs registered on the GitHub App. If omitted, the App's default redirect URL is used. Not stored or returned after creation."""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubAuthorizationConfiguration) -> dict:
    out: dict = {}
    out["authorizationCode"] = value["authorization_code"]
    out["state"] = value["state"]
    if "redirect_url" in value:
        out["redirectUrl"] = value["redirect_url"]
    return out


def deserialize_json(data: dict) -> GitHubAuthorizationConfiguration:
    out: GitHubAuthorizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("authorizationCode") is not None:
        out["authorization_code"] = data["authorizationCode"]
    else:
        out["authorization_code"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("redirectUrl") is not None:
        out["redirect_url"] = data["redirectUrl"]
    return out


def redact_sensitive(value: GitHubAuthorizationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_code" in value:
        out["authorization_code"] = "*** Sensitive Data Redacted ***"
    if "state" in value:
        out["state"] = "*** Sensitive Data Redacted ***"
    return out

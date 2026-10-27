"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenRequestBody``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.authorization_code
    import capo_signin.types.client_id
    import capo_signin.types.code_verifier
    import capo_signin.types.grant_type
    import capo_signin.types.redirect_uri
    import capo_signin.types.refresh_token


class CreateOAuth2TokenRequestBody(TypedDict, closed=True):
    client_id: "capo_signin.types.client_id.ClientId"
    """The OAuth 2.0 client identifier. Expected values: "arn:aws:signin:::devtools/same-device" or "arn:aws:signin:::devtools/cross-device"."""
    grant_type: "capo_signin.types.grant_type.GrantType"
    """The OAuth 2.0 grant type. Supported values: - "authorization_code" - Exchange an authorization code for tokens. - "refresh_token" - Use a refresh token to obtain a new access token."""
    code: NotRequired["capo_signin.types.authorization_code.AuthorizationCode"]
    """The authorization code received from the "/v1/authorize" endpoint. Required when "grant_type=authorization_code"."""
    redirect_uri: NotRequired["capo_signin.types.redirect_uri.RedirectUri"]
    """The redirect URI that was used in the original authorization request. Must match exactly. Required when "grant_type=authorization_code"."""
    code_verifier: NotRequired["capo_signin.types.code_verifier.CodeVerifier"]
    """The PKCE code verifier that proves possession of the original code challenge. Required when "grant_type=authorization_code"."""
    refresh_token: NotRequired["capo_signin.types.refresh_token.RefreshToken"]
    """The refresh token issued by a previous token response. Required when "grant_type=refresh_token"."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenRequestBody) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["grantType"] = value["grant_type"]
    if "code" in value:
        out["code"] = value["code"]
    if "redirect_uri" in value:
        out["redirectUri"] = value["redirect_uri"]
    if "code_verifier" in value:
        out["codeVerifier"] = value["code_verifier"]
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenRequestBody:
    out: CreateOAuth2TokenRequestBody = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    if data.get("grantType") is not None:
        out["grant_type"] = data["grantType"]
    else:
        out["grant_type"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("redirectUri") is not None:
        out["redirect_uri"] = data["redirectUri"]
    if data.get("codeVerifier") is not None:
        out["code_verifier"] = data["codeVerifier"]
    if data.get("refreshToken") is not None:
        out["refresh_token"] = data["refreshToken"]
    return out


def redact_sensitive(value: CreateOAuth2TokenRequestBody) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "refresh_token" in value:
        out["refresh_token"] = "*** Sensitive Data Redacted ***"
    return out

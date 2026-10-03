"""Generated from Smithy shape ``com.amazonaws.ssooidc#CreateTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_oidc.types.access_token
    import capo_sso_oidc.types.expiration_in_seconds
    import capo_sso_oidc.types.id_token
    import capo_sso_oidc.types.refresh_token
    import capo_sso_oidc.types.token_type


class CreateTokenResponse(TypedDict, closed=True):
    access_token: NotRequired["capo_sso_oidc.types.access_token.AccessToken"]
    """<p>A bearer token to access Amazon Web Services accounts and applications assigned to a user.</p>"""
    token_type: NotRequired["capo_sso_oidc.types.token_type.TokenType"]
    """<p>Used to notify the client that the returned token is an access token. The supported token type is <code>Bearer</code>.</p>"""
    expires_in: "capo_sso_oidc.types.expiration_in_seconds.ExpirationInSeconds"
    """<p>Indicates the time in seconds when an access token will expire.</p>"""
    refresh_token: NotRequired["capo_sso_oidc.types.refresh_token.RefreshToken"]
    """<p>A token that, if present, can be used to refresh a previously issued access token that might have expired.</p> <p>For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html">IAM Identity Center OIDC API Reference</a>.</p>"""
    id_token: NotRequired["capo_sso_oidc.types.id_token.IdToken"]
    """<p>The <code>idToken</code> is not implemented or supported. For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html">IAM Identity Center OIDC API Reference</a>.</p> <p>A JSON Web Token (JWT) that identifies who is associated with the issued access token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTokenResponse) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "token_type" in value:
        out["tokenType"] = value["token_type"]
    out["expiresIn"] = value.get("expires_in", 0)
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "id_token" in value:
        out["idToken"] = value["id_token"]
    return out


def deserialize_json(data: dict) -> CreateTokenResponse:
    out: CreateTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    if data.get("tokenType") is not None:
        out["token_type"] = data["tokenType"]
    if data.get("expiresIn") is not None:
        out["expires_in"] = data["expiresIn"]
    else:
        out["expires_in"] = 0
    if data.get("refreshToken") is not None:
        out["refresh_token"] = data["refreshToken"]
    if data.get("idToken") is not None:
        out["id_token"] = data["idToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenWithIAMResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signin.types.bearer_token_type
    import capo_signin.types.o_auth_access_token
    import capo_signin.types.token_expires_in


class CreateOAuth2TokenWithIAMResponse(TypedDict, closed=True):
    access_token: "capo_signin.types.o_auth_access_token.OAuthAccessToken"
    """Access token containing principal identity, resource scope, and session metadata."""
    token_type: "capo_signin.types.bearer_token_type.BearerTokenType"
    """The token type. Always "Bearer" as defined in RFC 6749."""
    expires_in: "capo_signin.types.token_expires_in.TokenExpiresIn"
    """Token lifetime in seconds. Value is the minimum of the caller's session validity and 1 hour (3600 seconds)."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenWithIAMResponse) -> dict:
    out: dict = {}
    out["access_token"] = value["access_token"]
    out["token_type"] = value["token_type"]
    out["expires_in"] = value["expires_in"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenWithIAMResponse:
    out: CreateOAuth2TokenWithIAMResponse = {}  # type: ignore[typeddict-item]
    if data.get("access_token") is not None:
        out["access_token"] = data["access_token"]
    else:
        out["access_token"] = ""
    if data.get("token_type") is not None:
        out["token_type"] = data["token_type"]
    else:
        out["token_type"] = ""
    if data.get("expires_in") is not None:
        out["expires_in"] = data["expires_in"]
    else:
        out["expires_in"] = 0
    return out


def redact_sensitive(value: CreateOAuth2TokenWithIAMResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out

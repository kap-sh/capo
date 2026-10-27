"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenWithTokenExchangeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.bearer_token_type
    import capo_signin.types.issued_o_auth_access_token_type
    import capo_signin.types.o_auth_access_token
    import capo_signin.types.token_expires_in


class CreateOAuth2TokenWithTokenExchangeResponse(TypedDict, closed=True):
    access_token: "capo_signin.types.o_auth_access_token.OAuthAccessToken"
    """Access token containing principal identity, resource scope, and session metadata."""
    issued_token_type: NotRequired[
        "capo_signin.types.issued_o_auth_access_token_type.IssuedOAuthAccessTokenType"
    ]
    """The token type of the issued token. Always "urn:ietf:params:oauth:token-type:access_token" as defined in RFC 8693 §2.2.1."""
    token_type: "capo_signin.types.bearer_token_type.BearerTokenType"
    """The token type. Currently only supports "Bearer" as defined in RFC 6749."""
    expires_in: "capo_signin.types.token_expires_in.TokenExpiresIn"
    """Token lifetime in seconds. Value is the minimum of the subject token's validity and 1 hour (3600 seconds)."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenWithTokenExchangeResponse) -> dict:
    out: dict = {}
    out["access_token"] = value["access_token"]
    if "issued_token_type" in value:
        out["issued_token_type"] = value["issued_token_type"]
    out["token_type"] = value["token_type"]
    out["expires_in"] = value["expires_in"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenWithTokenExchangeResponse:
    out: CreateOAuth2TokenWithTokenExchangeResponse = {}  # type: ignore[typeddict-item]
    if data.get("access_token") is not None:
        out["access_token"] = data["access_token"]
    else:
        out["access_token"] = ""
    if data.get("issued_token_type") is not None:
        out["issued_token_type"] = data["issued_token_type"]
    if data.get("token_type") is not None:
        out["token_type"] = data["token_type"]
    else:
        out["token_type"] = ""
    if data.get("expires_in") is not None:
        out["expires_in"] = data["expires_in"]
    else:
        out["expires_in"] = 0
    return out


def redact_sensitive(
    value: CreateOAuth2TokenWithTokenExchangeResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out

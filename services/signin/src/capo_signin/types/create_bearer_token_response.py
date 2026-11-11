"""Generated from Smithy shape ``com.amazonaws.signin#CreateBearerTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signin.types.bearer_token_expires_in
    import capo_signin.types.bearer_token_type
    import capo_signin.types.o_auth_access_token


class CreateBearerTokenResponse(TypedDict, closed=True):
    access_token: "capo_signin.types.o_auth_access_token.OAuthAccessToken"
    """The bearer token. Present it to the AWS service named in the request."""
    token_type: "capo_signin.types.bearer_token_type.BearerTokenType"
    """The token type. Always "Bearer"."""
    expires_in: "capo_signin.types.bearer_token_expires_in.BearerTokenExpiresIn"
    """Token lifetime in seconds."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBearerTokenResponse) -> dict:
    out: dict = {}
    out["access_token"] = value["access_token"]
    out["token_type"] = value["token_type"]
    out["expires_in"] = value["expires_in"]
    return out


def deserialize_json(data: dict) -> CreateBearerTokenResponse:
    out: CreateBearerTokenResponse = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: CreateBearerTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenWithIAMResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.bearer_token_type
    import capo_signin.types.o_auth_access_token
    import capo_signin.types.token_expires_in


class CreateOAuth2TokenWithIAMResponse(TypedDict, closed=True):
    access_token: "capo_signin.types.o_auth_access_token.OAuthAccessToken"
    """JWT access token containing principal identity, resource scope, and session metadata"""
    token_type: "capo_signin.types.bearer_token_type.BearerTokenType"
    """Always "Bearer" per OAuth 2.1 specification"""
    expires_in: "capo_signin.types.token_expires_in.TokenExpiresIn"
    """Token lifetime in seconds. Value is the minimum of session validity and 1 hour."""


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
        raise DeserializationError(
            "CreateOAuth2TokenWithIAMResponse.access_token required"
        )
    if data.get("token_type") is not None:
        out["token_type"] = data["token_type"]
    else:
        raise DeserializationError(
            "CreateOAuth2TokenWithIAMResponse.token_type required"
        )
    if data.get("expires_in") is not None:
        out["expires_in"] = data["expires_in"]
    else:
        raise DeserializationError(
            "CreateOAuth2TokenWithIAMResponse.expires_in required"
        )
    return out

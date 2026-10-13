"""Generated from Smithy shape ``com.amazonaws.signin#IntrospectOAuth2TokenWithIAMRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.introspection_token
    import capo_signin.types.token_type_hint


class IntrospectOAuth2TokenWithIAMRequest(TypedDict, closed=True):
    token: "capo_signin.types.introspection_token.IntrospectionToken"
    """The string value of the token to introspect. May be either an access_token or a refresh_token issued by AWS Sign-In."""
    token_type_hint: NotRequired["capo_signin.types.token_type_hint.TokenTypeHint"]
    """Optional hint about the type of the token submitted for introspection. The server uses this hint to optimize lookup, but still falls back to the other token type on miss. Allowed values: access_token, refresh_token."""


# --- restJson1 ser/de ---
def serialize_json(value: IntrospectOAuth2TokenWithIAMRequest) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    if "token_type_hint" in value:
        out["token_type_hint"] = value["token_type_hint"]
    return out


def deserialize_json(data: dict) -> IntrospectOAuth2TokenWithIAMRequest:
    out: IntrospectOAuth2TokenWithIAMRequest = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        raise DeserializationError("IntrospectOAuth2TokenWithIAMRequest.token required")
    if data.get("token_type_hint") is not None:
        out["token_type_hint"] = data["token_type_hint"]
    return out


def redact_sensitive(value: IntrospectOAuth2TokenWithIAMRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out

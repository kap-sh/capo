"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#RefreshTokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.refresh_token_request_body
    import capo_amplifyuibuilder.types.token_providers


class RefreshTokenRequest(TypedDict, closed=True):
    provider: "capo_amplifyuibuilder.types.token_providers.TokenProviders"
    """<p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>"""
    refresh_token_body: (
        "capo_amplifyuibuilder.types.refresh_token_request_body.RefreshTokenRequestBody"
    )
    """<p>Information about the refresh token request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshTokenRequest) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.refresh_token_request_body

    out["refreshTokenBody"] = (
        capo_amplifyuibuilder.types.refresh_token_request_body.serialize_json(
            value["refresh_token_body"]
        )
    )
    return out


def deserialize_json(data: dict) -> RefreshTokenRequest:
    out: RefreshTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("refreshTokenBody") is not None:
        import capo_amplifyuibuilder.types.refresh_token_request_body

        out["refresh_token_body"] = (
            capo_amplifyuibuilder.types.refresh_token_request_body.deserialize_json(
                data["refreshTokenBody"]
            )
        )
    else:
        raise DeserializationError("RefreshTokenRequest.refresh_token_body required")
    return out


def redact_sensitive(value: RefreshTokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "refresh_token_body" in value:
        import capo_amplifyuibuilder.types.refresh_token_request_body

        out["refresh_token_body"] = (
            capo_amplifyuibuilder.types.refresh_token_request_body.redact_sensitive(
                value["refresh_token_body"]
            )
        )
    return out

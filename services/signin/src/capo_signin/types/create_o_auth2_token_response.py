"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.create_o_auth2_token_response_body


class CreateOAuth2TokenResponse(TypedDict, closed=True):
    token_output: "capo_signin.types.create_o_auth2_token_response_body.CreateOAuth2TokenResponseBody"
    """Flattened token operation outputs The specific response fields depend on the grant_type used in the request"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenResponse) -> dict:
    out: dict = {}
    import capo_signin.types.create_o_auth2_token_response_body

    out["tokenOutput"] = (
        capo_signin.types.create_o_auth2_token_response_body.serialize_json(
            value["token_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenResponse:
    out: CreateOAuth2TokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("tokenOutput") is not None:
        import capo_signin.types.create_o_auth2_token_response_body

        out["token_output"] = (
            capo_signin.types.create_o_auth2_token_response_body.deserialize_json(
                data["tokenOutput"]
            )
        )
    else:
        raise DeserializationError("CreateOAuth2TokenResponse.token_output required")
    return out


def redact_sensitive(value: CreateOAuth2TokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token_output" in value:
        import capo_signin.types.create_o_auth2_token_response_body

        out["token_output"] = (
            capo_signin.types.create_o_auth2_token_response_body.redact_sensitive(
                value["token_output"]
            )
        )
    return out

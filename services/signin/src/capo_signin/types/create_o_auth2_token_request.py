"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.create_o_auth2_token_request_body


class CreateOAuth2TokenRequest(TypedDict, closed=True):
    token_input: "capo_signin.types.create_o_auth2_token_request_body.CreateOAuth2TokenRequestBody"
    """Flattened token operation inputs The specific operation is determined by grant_type in the request body"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenRequest) -> dict:
    out: dict = {}
    import capo_signin.types.create_o_auth2_token_request_body

    out["tokenInput"] = (
        capo_signin.types.create_o_auth2_token_request_body.serialize_json(
            value["token_input"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenRequest:
    out: CreateOAuth2TokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("tokenInput") is not None:
        import capo_signin.types.create_o_auth2_token_request_body

        out["token_input"] = (
            capo_signin.types.create_o_auth2_token_request_body.deserialize_json(
                data["tokenInput"]
            )
        )
    else:
        raise DeserializationError("CreateOAuth2TokenRequest.token_input required")
    return out


def redact_sensitive(value: CreateOAuth2TokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token_input" in value:
        import capo_signin.types.create_o_auth2_token_request_body

        out["token_input"] = (
            capo_signin.types.create_o_auth2_token_request_body.redact_sensitive(
                value["token_input"]
            )
        )
    return out

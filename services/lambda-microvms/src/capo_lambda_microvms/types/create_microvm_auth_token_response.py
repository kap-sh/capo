"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CreateMicrovmAuthTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.token_parts


class CreateMicrovmAuthTokenResponse(TypedDict, closed=True):
    auth_token: "capo_lambda_microvms.types.token_parts.TokenParts"
    """<p>A map containing the authentication token. Use the value at key "X-aws-proxy-auth" as the header value when connecting to the MicroVM endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMicrovmAuthTokenResponse) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.token_parts

    out["authToken"] = capo_lambda_microvms.types.token_parts.serialize_json(
        value["auth_token"]
    )
    return out


def deserialize_json(data: dict) -> CreateMicrovmAuthTokenResponse:
    out: CreateMicrovmAuthTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("authToken") is not None:
        import capo_lambda_microvms.types.token_parts

        out["auth_token"] = capo_lambda_microvms.types.token_parts.deserialize_json(
            data["authToken"]
        )
    else:
        out["auth_token"] = {}
    return out


def redact_sensitive(value: CreateMicrovmAuthTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_token" in value:
        import capo_lambda_microvms.types.token_parts

        out["auth_token"] = capo_lambda_microvms.types.token_parts.redact_sensitive(
            value["auth_token"]
        )
    return out

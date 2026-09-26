"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CreateMicrovmShellAuthTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.token_parts


class CreateMicrovmShellAuthTokenResponse(TypedDict, closed=True):
    auth_token: "capo_lambda_microvms.types.token_parts.TokenParts"
    """<p>The generated shell authentication token key-value pairs for accessing the MicroVM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMicrovmShellAuthTokenResponse) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.token_parts

    out["authToken"] = capo_lambda_microvms.types.token_parts.serialize_json(
        value["auth_token"]
    )
    return out


def deserialize_json(data: dict) -> CreateMicrovmShellAuthTokenResponse:
    out: CreateMicrovmShellAuthTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("authToken") is not None:
        import capo_lambda_microvms.types.token_parts

        out["auth_token"] = capo_lambda_microvms.types.token_parts.deserialize_json(
            data["authToken"]
        )
    else:
        raise DeserializationError(
            "CreateMicrovmShellAuthTokenResponse.auth_token required"
        )
    return out

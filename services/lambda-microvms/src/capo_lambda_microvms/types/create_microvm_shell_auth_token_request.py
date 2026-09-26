"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CreateMicrovmShellAuthTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_identifier
    import capo_lambda_microvms.types.positive_integer


class CreateMicrovmShellAuthTokenRequest(TypedDict, closed=True):
    microvm_identifier: (
        "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier"
    )
    """<p>The ID of the MicroVM to create a shell authentication token for.</p>"""
    expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger"
    """<p>The duration in minutes before the shell authentication token expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMicrovmShellAuthTokenRequest) -> dict:
    out: dict = {}
    out["expirationInMinutes"] = value["expiration_in_minutes"]
    return out


def deserialize_json(data: dict) -> CreateMicrovmShellAuthTokenRequest:
    out: CreateMicrovmShellAuthTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("expirationInMinutes") is not None:
        out["expiration_in_minutes"] = data["expirationInMinutes"]
    else:
        raise DeserializationError(
            "CreateMicrovmShellAuthTokenRequest.expiration_in_minutes required"
        )
    return out

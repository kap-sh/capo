"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ValidateNotifyCodeVerificationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.verification_status


class ValidateNotifyCodeVerificationOutput(TypedDict, closed=True):
    status: "capo_endusermessaging.types.verification_status.VerificationStatus"
    """<p>The outcome of the validation attempt. VALID indicates that the submitted passcode matched an active verification. INVALID indicates that the passcode did not match, expired, or exceeded its attempt limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateNotifyCodeVerificationOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.verification_status

    out["status"] = capo_endusermessaging.types.verification_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ValidateNotifyCodeVerificationOutput:
    out: ValidateNotifyCodeVerificationOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_endusermessaging.types.verification_status

        out["status"] = (
            capo_endusermessaging.types.verification_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateNotifyCodeVerificationOutput.status required"
        )
    return out

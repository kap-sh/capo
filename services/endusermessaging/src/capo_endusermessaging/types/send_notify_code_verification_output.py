"""Generated from Smithy shape ``com.amazonaws.endusermessaging#SendNotifyCodeVerificationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.message_id
    import capo_endusermessaging.types.verification_id


class SendNotifyCodeVerificationOutput(TypedDict, closed=True):
    verification_id: "capo_endusermessaging.types.verification_id.VerificationId"
    """<p>The service-generated identifier for the verification.</p>"""
    message_id: "capo_endusermessaging.types.message_id.MessageId"
    """<p>The service-generated identifier for the message that delivers the one-time passcode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendNotifyCodeVerificationOutput) -> dict:
    out: dict = {}
    out["verificationId"] = value["verification_id"]
    out["messageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendNotifyCodeVerificationOutput:
    out: SendNotifyCodeVerificationOutput = {}  # type: ignore[typeddict-item]
    if data.get("verificationId") is not None:
        out["verification_id"] = data["verificationId"]
    else:
        raise DeserializationError(
            "SendNotifyCodeVerificationOutput.verification_id required"
        )
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    else:
        raise DeserializationError(
            "SendNotifyCodeVerificationOutput.message_id required"
        )
    return out

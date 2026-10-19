"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ValidateNotifyCodeVerificationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.destination_identity
    import capo_endusermessaging.types.reference_id
    import capo_endusermessaging.types.verification_code


class ValidateNotifyCodeVerificationInput(TypedDict, closed=True):
    destination_identity: (
        "capo_endusermessaging.types.destination_identity.DestinationIdentity"
    )
    """<p>The recipient identifier. For the TEXT and VOICE channels, specify an E.164 phone number. For the WhatsApp channel, specify a WhatsApp address.</p>"""
    reference_id: NotRequired["capo_endusermessaging.types.reference_id.ReferenceId"]
    """<p>The caller-supplied reference identifier used to locate the verification. This value must match the value that you supplied to the SendNotifyCodeVerification operation.</p>"""
    code: "capo_endusermessaging.types.verification_code.VerificationCode"
    """<p>The one-time passcode that the recipient submitted for validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateNotifyCodeVerificationInput) -> dict:
    out: dict = {}
    out["destinationIdentity"] = value["destination_identity"]
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ValidateNotifyCodeVerificationInput:
    out: ValidateNotifyCodeVerificationInput = {}  # type: ignore[typeddict-item]
    if data.get("destinationIdentity") is not None:
        out["destination_identity"] = data["destinationIdentity"]
    else:
        out["destination_identity"] = ""
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    return out


def redact_sensitive(value: ValidateNotifyCodeVerificationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination_identity" in value:
        out["destination_identity"] = "*** Sensitive Data Redacted ***"
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    return out

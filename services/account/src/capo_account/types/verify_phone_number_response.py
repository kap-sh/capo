"""Generated from Smithy shape ``com.amazonaws.account#VerifyPhoneNumberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.phone_number_verification_status


class VerifyPhoneNumberResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_account.types.phone_number_verification_status.PhoneNumberVerificationStatus"
    ]
    """<p>The verification status of the phone number in the primary contact information after the submitted one-time passcode is evaluated. Valid values:</p> <ul> <li> <p> <code>PENDING</code> – A one-time passcode has been sent and is waiting to be submitted.</p> </li> <li> <p> <code>VERIFIED</code> – The phone number has been verified.</p> </li> <li> <p> <code>UNVERIFIED</code> – The phone number has not been verified.</p> </li> <li> <p> <code>NOT_SUPPORTED</code> – Phone number verification isn't available for this account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyPhoneNumberResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VerifyPhoneNumberResponse:
    out: VerifyPhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out

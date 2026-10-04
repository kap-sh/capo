"""Generated from Smithy shape ``com.amazonaws.account#GetContactInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.contact_information
    import capo_account.types.phone_number_verification_status


class GetContactInformationResponse(TypedDict, closed=True):
    contact_information: NotRequired[
        "capo_account.types.contact_information.ContactInformation"
    ]
    """<p>Contains the details of the primary contact information associated with an Amazon Web Services account.</p>"""
    verification_status: NotRequired[
        "capo_account.types.phone_number_verification_status.PhoneNumberVerificationStatus"
    ]
    """<p>The verification status of the phone number in the primary contact information associated with an Amazon Web Services account. Valid values:</p> <ul> <li> <p> <code>PENDING</code> – A one-time passcode has been sent and is waiting to be submitted.</p> </li> <li> <p> <code>VERIFIED</code> – The phone number has been verified.</p> </li> <li> <p> <code>UNVERIFIED</code> – The phone number has not been verified.</p> </li> <li> <p> <code>NOT_SUPPORTED</code> – Phone number verification isn't available for this account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactInformationResponse) -> dict:
    out: dict = {}
    if "contact_information" in value:
        import capo_account.types.contact_information

        out["ContactInformation"] = (
            capo_account.types.contact_information.serialize_json(
                value["contact_information"]
            )
        )
    if "verification_status" in value:
        out["VerificationStatus"] = value["verification_status"]
    return out


def deserialize_json(data: dict) -> GetContactInformationResponse:
    out: GetContactInformationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContactInformation") is not None:
        import capo_account.types.contact_information

        out["contact_information"] = (
            capo_account.types.contact_information.deserialize_json(
                data["ContactInformation"]
            )
        )
    if data.get("VerificationStatus") is not None:
        out["verification_status"] = data["VerificationStatus"]
    return out

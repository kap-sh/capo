"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppCallPermissionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_business_scoped_user_id
    import capo_socialmessaging.types.whats_app_destination_phone_number
    import capo_socialmessaging.types.whats_app_phone_number_id


class GetWhatsAppCallPermissionInput(TypedDict, closed=True):
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the business phone number for which to retrieve the calling permission. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>.</p>"""
    destination_phone_number: NotRequired[
        "capo_socialmessaging.types.whats_app_destination_phone_number.WhatsAppDestinationPhoneNumber"
    ]
    """<p>The end user's phone number, in E.164 format, for which to retrieve the calling permission.</p>"""
    end_user_bsuid: NotRequired[
        "capo_socialmessaging.types.whats_app_business_scoped_user_id.WhatsAppBusinessScopedUserId"
    ]
    """<p>The business-scoped user identifier (BSUID) of the end user for which to retrieve the calling permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppCallPermissionInput) -> dict:
    out: dict = {}
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    if "destination_phone_number" in value:
        out["destinationPhoneNumber"] = value["destination_phone_number"]
    if "end_user_bsuid" in value:
        out["endUserBsuid"] = value["end_user_bsuid"]
    return out


def deserialize_json(data: dict) -> GetWhatsAppCallPermissionInput:
    out: GetWhatsAppCallPermissionInput = {}  # type: ignore[typeddict-item]
    if data.get("originationPhoneNumberId") is not None:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        raise DeserializationError(
            "GetWhatsAppCallPermissionInput.origination_phone_number_id required"
        )
    if data.get("destinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["destinationPhoneNumber"]
    if data.get("endUserBsuid") is not None:
        out["end_user_bsuid"] = data["endUserBsuid"]
    return out


def redact_sensitive(value: GetWhatsAppCallPermissionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination_phone_number" in value:
        out["destination_phone_number"] = "*** Sensitive Data Redacted ***"
    if "end_user_bsuid" in value:
        out["end_user_bsuid"] = "*** Sensitive Data Redacted ***"
    return out

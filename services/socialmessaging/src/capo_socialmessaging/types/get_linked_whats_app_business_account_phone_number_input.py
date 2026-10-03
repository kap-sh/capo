"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetLinkedWhatsAppBusinessAccountPhoneNumberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_phone_number_id


class GetLinkedWhatsAppBusinessAccountPhoneNumberInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    """<p>The unique identifier of the phone number. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkedWhatsAppBusinessAccountPhoneNumberInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLinkedWhatsAppBusinessAccountPhoneNumberInput:
    out: GetLinkedWhatsAppBusinessAccountPhoneNumberInput = {}  # type: ignore[typeddict-item]
    return out

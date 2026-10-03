"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DeleteWhatsAppMessageMediaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_media_id
    import capo_socialmessaging.types.whats_app_phone_number_id


class DeleteWhatsAppMessageMediaInput(TypedDict, closed=True):
    media_id: "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId"
    """<p>The unique identifier of the media file to delete. Use the <code>mediaId</code> returned from <a href="https://console.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html">PostWhatsAppMessageMedia</a>.</p>"""
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWhatsAppMessageMediaInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWhatsAppMessageMediaInput:
    out: DeleteWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
    return out

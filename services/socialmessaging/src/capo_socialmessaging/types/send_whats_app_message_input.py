"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SendWhatsAppMessageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_message_blob
    import capo_socialmessaging.types.whats_app_phone_number_id


class SendWhatsAppMessageInput(TypedDict, closed=True):
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The ID of the phone number used to send the WhatsApp message. If you are sending a media file only the <code>originationPhoneNumberId</code> used to upload the file can be used. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>"""
    message: "capo_socialmessaging.types.whats_app_message_blob.WhatsAppMessageBlob"
    """<p>The message to send through WhatsApp. The length is in KB. The message field passes through a WhatsApp Message object, see <a href="https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages">Messages</a> in the <i>WhatsApp Business Platform Cloud API Reference</i>.</p>"""
    meta_api_version: "str"
    """<p>The API version for the request formatted as <code>v{VersionNumber}</code>. For a list of supported API versions and Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html"> <i>Amazon Web Services End User Messaging Social API</i> Service Endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWhatsAppMessageInput) -> dict:
    out: dict = {}
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    import capo_socialmessaging.types.whats_app_message_blob

    out["message"] = capo_socialmessaging.types.whats_app_message_blob.serialize_json(
        value["message"]
    )
    out["metaApiVersion"] = value["meta_api_version"]
    return out


def deserialize_json(data: dict) -> SendWhatsAppMessageInput:
    out: SendWhatsAppMessageInput = {}  # type: ignore[typeddict-item]
    if data.get("originationPhoneNumberId") is not None:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        raise DeserializationError(
            "SendWhatsAppMessageInput.origination_phone_number_id required"
        )
    if data.get("message") is not None:
        import capo_socialmessaging.types.whats_app_message_blob

        out["message"] = (
            capo_socialmessaging.types.whats_app_message_blob.deserialize_json(
                data["message"]
            )
        )
    else:
        raise DeserializationError("SendWhatsAppMessageInput.message required")
    if data.get("metaApiVersion") is not None:
        out["meta_api_version"] = data["metaApiVersion"]
    else:
        raise DeserializationError("SendWhatsAppMessageInput.meta_api_version required")
    return out

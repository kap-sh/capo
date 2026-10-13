"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SendWhatsAppCallEventInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_event_blob
    import capo_socialmessaging.types.whats_app_phone_number_id


class SendWhatsAppCallEventInput(TypedDict, closed=True):
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the origination phone number for the call. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <code>GetLinkedWhatsAppBusinessAccount</code> to find a phone number's ID.</p>"""
    meta_api_version: "str"
    """<p>The version of the Meta Graph API to use for the request.</p>"""
    call_event: (
        "capo_socialmessaging.types.whats_app_call_event_blob.WhatsAppCallEventBlob"
    )
    """<p>The call event payload to send, as a JSON blob in the format defined by the Meta calling API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWhatsAppCallEventInput) -> dict:
    out: dict = {}
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    out["metaApiVersion"] = value["meta_api_version"]
    import capo_socialmessaging.types.whats_app_call_event_blob

    out["callEvent"] = (
        capo_socialmessaging.types.whats_app_call_event_blob.serialize_json(
            value["call_event"]
        )
    )
    return out


def deserialize_json(data: dict) -> SendWhatsAppCallEventInput:
    out: SendWhatsAppCallEventInput = {}  # type: ignore[typeddict-item]
    if data.get("originationPhoneNumberId") is not None:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        raise DeserializationError(
            "SendWhatsAppCallEventInput.origination_phone_number_id required"
        )
    if data.get("metaApiVersion") is not None:
        out["meta_api_version"] = data["metaApiVersion"]
    else:
        raise DeserializationError(
            "SendWhatsAppCallEventInput.meta_api_version required"
        )
    if data.get("callEvent") is not None:
        import capo_socialmessaging.types.whats_app_call_event_blob

        out["call_event"] = (
            capo_socialmessaging.types.whats_app_call_event_blob.deserialize_json(
                data["callEvent"]
            )
        )
    else:
        raise DeserializationError("SendWhatsAppCallEventInput.call_event required")
    return out


def redact_sensitive(value: SendWhatsAppCallEventInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "call_event" in value:
        out["call_event"] = "*** Sensitive Data Redacted ***"
    return out

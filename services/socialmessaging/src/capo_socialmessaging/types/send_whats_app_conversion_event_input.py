"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SendWhatsAppConversionEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.whats_app_conversion_event_blob
    import capo_socialmessaging.types.whats_app_dataset_id


class SendWhatsAppConversionEventInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with the dataset, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""
    dataset_id: "capo_socialmessaging.types.whats_app_dataset_id.WhatsAppDatasetId"
    """<p>The Meta-generated dataset ID to send the event to.</p>"""
    event_data: "capo_socialmessaging.types.whats_app_conversion_event_blob.WhatsAppConversionEventBlob"
    """<p>The raw Meta Conversions API event payload as a JSON blob. See <a href="https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event">Meta's server event parameters</a> for the supported format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWhatsAppConversionEventInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["datasetId"] = value["dataset_id"]
    import capo_socialmessaging.types.whats_app_conversion_event_blob

    out["eventData"] = (
        capo_socialmessaging.types.whats_app_conversion_event_blob.serialize_json(
            value["event_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> SendWhatsAppConversionEventInput:
    out: SendWhatsAppConversionEventInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SendWhatsAppConversionEventInput.id required")
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError(
            "SendWhatsAppConversionEventInput.dataset_id required"
        )
    if data.get("eventData") is not None:
        import capo_socialmessaging.types.whats_app_conversion_event_blob

        out["event_data"] = (
            capo_socialmessaging.types.whats_app_conversion_event_blob.deserialize_json(
                data["eventData"]
            )
        )
    else:
        raise DeserializationError(
            "SendWhatsAppConversionEventInput.event_data required"
        )
    return out

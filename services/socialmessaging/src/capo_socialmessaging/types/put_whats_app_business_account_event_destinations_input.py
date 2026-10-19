"""Generated from Smithy shape ``com.amazonaws.socialmessaging#PutWhatsAppBusinessAccountEventDestinationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.whats_app_business_account_event_destinations


class PutWhatsAppBusinessAccountEventDestinationsInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>"""
    event_destinations: "capo_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations"
    """<p>An array of <code>WhatsAppBusinessAccountEventDestination</code> event destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutWhatsAppBusinessAccountEventDestinationsInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_socialmessaging.types.whats_app_business_account_event_destinations

    out["eventDestinations"] = (
        capo_socialmessaging.types.whats_app_business_account_event_destinations.serialize_json(
            value["event_destinations"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutWhatsAppBusinessAccountEventDestinationsInput:
    out: PutWhatsAppBusinessAccountEventDestinationsInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("eventDestinations") is not None:
        import capo_socialmessaging.types.whats_app_business_account_event_destinations

        out["event_destinations"] = (
            capo_socialmessaging.types.whats_app_business_account_event_destinations.deserialize_json(
                data["eventDestinations"]
            )
        )
    else:
        out["event_destinations"] = []
    return out

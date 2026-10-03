"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DisassociateWhatsAppBusinessAccountInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id


class DisassociateWhatsAppBusinessAccountInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateWhatsAppBusinessAccountInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateWhatsAppBusinessAccountInput:
    out: DisassociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
    return out

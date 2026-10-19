"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppDatasetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id


class CreateWhatsAppDatasetInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to create a dataset for, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppDatasetInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppDatasetInput:
    out: CreateWhatsAppDatasetInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out

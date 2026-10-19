"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_phone_number_id


class UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput(TypedDict, closed=True):
    phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the phone number that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput) -> dict:
    out: dict = {}
    out["phoneNumberId"] = value["phone_number_id"]
    return out


def deserialize_json(
    data: dict,
) -> UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput:
    out: UpdateLinkedWhatsAppBusinessAccountPhoneNumberOutput = {}  # type: ignore[typeddict-item]
    if data.get("phoneNumberId") is not None:
        out["phone_number_id"] = data["phoneNumberId"]
    else:
        out["phone_number_id"] = ""
    return out

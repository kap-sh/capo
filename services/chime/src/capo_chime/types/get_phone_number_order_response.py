"""Generated from Smithy shape ``com.amazonaws.chime#GetPhoneNumberOrderResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.phone_number_order


class GetPhoneNumberOrderResponse(TypedDict, closed=True):
    phone_number_order: NotRequired[
        "capo_chime.types.phone_number_order.PhoneNumberOrder"
    ]
    """<p>The phone number order details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberOrderResponse) -> dict:
    out: dict = {}
    if "phone_number_order" in value:
        import capo_chime.types.phone_number_order

        out["PhoneNumberOrder"] = capo_chime.types.phone_number_order.serialize_json(
            value["phone_number_order"]
        )
    return out


def deserialize_json(data: dict) -> GetPhoneNumberOrderResponse:
    out: GetPhoneNumberOrderResponse = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberOrder") is not None:
        import capo_chime.types.phone_number_order

        out["phone_number_order"] = (
            capo_chime.types.phone_number_order.deserialize_json(
                data["PhoneNumberOrder"]
            )
        )
    return out


def redact_sensitive(value: GetPhoneNumberOrderResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number_order" in value:
        import capo_chime.types.phone_number_order

        out["phone_number_order"] = (
            capo_chime.types.phone_number_order.redact_sensitive(
                value["phone_number_order"]
            )
        )
    return out

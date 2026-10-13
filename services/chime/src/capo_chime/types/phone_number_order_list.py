"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberOrderList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.phone_number_order

PhoneNumberOrderList: TypeAlias = list[
    "capo_chime.types.phone_number_order.PhoneNumberOrder"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberOrderList) -> list:
    import capo_chime.types.phone_number_order

    out: list = []
    for item in value:
        out.append(capo_chime.types.phone_number_order.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberOrderList:
    import capo_chime.types.phone_number_order

    out: PhoneNumberOrderList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime.types.phone_number_order.deserialize_json(item))
    return out


def redact_sensitive(value: PhoneNumberOrderList) -> list[Any]:
    import capo_chime.types.phone_number_order

    return [
        capo_chime.types.phone_number_order.redact_sensitive(item) for item in value
    ]

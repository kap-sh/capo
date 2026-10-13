"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OrderedPhoneNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.ordered_phone_number

OrderedPhoneNumberList: TypeAlias = list[
    "capo_chime_sdk_voice.types.ordered_phone_number.OrderedPhoneNumber"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderedPhoneNumberList) -> list:
    import capo_chime_sdk_voice.types.ordered_phone_number

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.ordered_phone_number.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrderedPhoneNumberList:
    import capo_chime_sdk_voice.types.ordered_phone_number

    out: OrderedPhoneNumberList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_voice.types.ordered_phone_number.deserialize_json(item)
        )
    return out


def redact_sensitive(value: OrderedPhoneNumberList) -> list[Any]:
    import capo_chime_sdk_voice.types.ordered_phone_number

    return [
        capo_chime_sdk_voice.types.ordered_phone_number.redact_sensitive(item)
        for item in value
    ]

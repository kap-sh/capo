"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number

PhoneNumberList: TypeAlias = list["capo_chime_sdk_voice.types.phone_number.PhoneNumber"]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberList) -> list:
    import capo_chime_sdk_voice.types.phone_number

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.phone_number.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberList:
    import capo_chime_sdk_voice.types.phone_number

    out: PhoneNumberList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_voice.types.phone_number.deserialize_json(item))
    return out


def redact_sensitive(value: PhoneNumberList) -> list[Any]:
    import capo_chime_sdk_voice.types.phone_number

    return [
        capo_chime_sdk_voice.types.phone_number.redact_sensitive(item) for item in value
    ]
